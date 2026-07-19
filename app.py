import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, ttk


class TranscoderApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Resolve Video Transcoder")
        self.root.geometry("550x350")
        self.root.resizable(False, False)

        # Style setup
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Main Layout
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        self.title_label = ttk.Label(
            self.main_frame,
            text="DaVinci Resolve Linux Transcoder",
            font=("Helvetica", 14, "bold"),
        )
        self.title_label.pack(pady=(0, 10))

        self.desc_label = ttk.Label(
            self.main_frame,
            text="Converts MP4/MOV files to DNxHR HQ for the free version of Resolve.",
            wraplength=500,
        )
        self.desc_label.pack(pady=(0, 20))

        # Folder Selection Button
        self.select_btn = ttk.Button(
            self.main_frame,
            text="Select Folder with Videos",
            command=self.start_transcoding_thread,
        )
        self.select_btn.pack(pady=10)

        # Progress Status
        self.status_label = ttk.Label(
            self.main_frame, text="Status: Idle", font=("Helvetica", 10, "italic")
        )
        self.status_label.pack(pady=10)

        # Terminal Log Console inside the GUI
        self.log_text = tk.Text(
            self.main_frame,
            height=8,
            width=60,
            bg="#1e1e1e",
            fg="#ffffff",
            font=("Courier", 9),
        )
        self.log_text.pack(pady=10)
        self.log_text.insert(tk.END, "Ready to optimize clips...\n")
        self.log_text.config(state=tk.DISABLED)

    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def start_transcoding_thread(self):
        folder = filedialog.askdirectory(title="Select Video Folder")
        if not folder:
            return

        # Disable button during processing
        self.select_btn.config(state=tk.DISABLED)
        # Run in a separate thread so the GUI stays responsive
        threading.Thread(
            target=self.process_videos, args=(folder,), daemon=True
        ).start()

    def process_videos(self, folder):
        valid_extensions = (".mp4", ".mov", ".MP4", ".MOV")
        files = [
            f
            for f in os.listdir(folder)
            if f.endswith(valid_extensions) and not f.endswith("_ready.mov")
        ]

        if not files:
            self.status_label.config(text="Status: No compatible files found.")
            self.select_btn.config(state=tk.NORMAL)
            return

        total_files = len(files)
        self.status_label.config(text=f"Status: Processing 0/{total_files} files")

        for idx, file in enumerate(files, 1):
            input_path = os.path.join(folder, file)
            filename_without_ext = os.path.splitext(file)[0]
            output_path = os.path.join(
                folder, f"{filename_without_ext}_ready.mov"
            )

            self.status_label.config(
                text=f"Status: Processing file {idx}/{total_files}"
            )
            self.log(f"Transcoding: {file} -> DNxHR...")

            # Run FFmpeg command quietly
            cmd = [
                "ffmpeg",
                "-y",  # Overwrite output files without asking
                "-i",
                input_path,
                "-c:v",
                "dnxhd",
                "-profile:v",
                "dnxhr_hq",
                "-pix_fmt",
                "yuv422p",
                "-c:a",
                "pcm_s16le",
                output_path,
            ]

            process = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            if process.returncode == 0:
                self.log(f"✓ Success: {file}")
            else:
                self.log(f"✗ Failed: {file}")

        self.status_label.config(text="Status: All Transcoding Complete!")
        self.log("\nDone! Drag the '_ready.mov' files right into DaVinci.")
        self.select_btn.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = TranscoderApp(root)
    root.mainloop()