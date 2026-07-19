# DaVinci Resolve Linux Transcoder

A simple and lightweight graphical tool to batch-convert `.mp4` and `.mov` video files (H.264/H.265) into **DNxHR HQ** format. 

This tool is designed specifically for Linux users running the **free version of DaVinci Resolve**, which does not natively support H.264/H.265 decoding due to licensing limitations on the Linux platform.

---

## Features

- 📦 **Pre-compiled Binary**: Download the standalone executable (`ResolveTranscoder`) directly from GitHub Releases without needing Python or Tkinter installed.
- 📂 **Batch Folder Processing**: Select a folder and let the tool automatically scan and process all compatible videos.
- ⚡ **Non-blocking Multi-threading**: The user interface remains responsive and smooth during transcoding.
- 🖥️ **Integrated Log Terminal**: View real-time transcoding progress and success/failure status within the application.
- 🔄 **Safe Conversion**: Original files are never overwritten; outputs are saved alongside them with a `_ready.mov` suffix.
- ⚙️ **Optimized Outputs**: Uses high-quality **DNxHR HQ** video coding and uncompressed **16-bit PCM** audio.

---

## Prerequisites

### 1. FFmpeg (Required)
Regardless of how you run the app, make sure `ffmpeg` is installed and available in your system's PATH.

* **Debian/Ubuntu/Pop!_OS**:
  ```bash
  sudo apt install ffmpeg
  ```
* **Fedora**:
  ```bash
  sudo dnf install ffmpeg
  ```
* **Arch Linux**:
  ```bash
  sudo pacman -S ffmpeg
  ```

### 2. Python 3 & Tkinter (Only if running from source)
If you run the application directly from the source code, you will need Python 3 and Tkinter:

* **Debian/Ubuntu/Pop!_OS**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-tk
  ```
* **Fedora**:
  ```bash
  sudo dnf install python3 python3-tkinter
  ```
* **Arch Linux**:
  ```bash
  sudo pacman -S python tk
  ```

---

## Installation & Running

You can run the application either using the pre-compiled standalone executable or directly from source.

### Option A: Using the Standalone Executable (Recommended)
1. Go to the **GitHub Releases** page of your repository.
2. Download the `ResolveTranscoder` executable.
3. Make the file executable via terminal:
   ```bash
   chmod +x ResolveTranscoder
   ```
4. Run it:
   ```bash
   ./ResolveTranscoder
   ```

### Option B: Running from Source
1. Clone or download this repository.
2. Open a terminal in the folder containing `app.py`.
3. Run the application:
   ```bash
   python3 app.py
   ```

---

## How to Use

1. Click on the **"Select Folder with Videos"** button.
2. Select the directory containing your `.mp4` or `.mov` camera clips.
3. The transcoder will start processing the files one-by-one.
4. Once completed, you will find files named `<original_name>_ready.mov` in the same directory.
5. Simply drag and drop the `_ready.mov` files directly into your DaVinci Resolve media pool!

---

## Technical Specifications

The conversion runs the following `ffmpeg` command under the hood:

```bash
ffmpeg -y -i <input_file> -c:v dnxhd -profile:v dnxhr_hq -pix_fmt yuv422p -c:a pcm_s16le <output_file>_ready.mov
```

### Stream Details:
* **Video Stream**: Transcoded to DNxHR High Quality (`dnxhr_hq`), with pixel format `yuv422p`.
* **Audio Stream**: Transcoded to uncompressed 16-bit little-endian PCM (`pcm_s16le`).
* **Container**: QuickTime/MOV (`.mov`).
