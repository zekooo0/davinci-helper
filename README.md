# DaVinci Resolve Linux Transcoder

A simple and lightweight graphical tool to batch-convert `.mp4` and `.mov` video files (H.264/H.265) into **DNxHR HQ** format. 

This tool is designed specifically for Linux users running the **free version of DaVinci Resolve**, which does not natively support H.264/H.265 decoding due to licensing limitations on the Linux platform.

---

## Features

- 📂 **Batch Folder Processing**: Select a folder and let the tool automatically scan and process all compatible videos.
- ⚡ **Non-blocking Multi-threading**: The user interface remains responsive and smooth during transcoding.
- 🖥️ **Integrated Log Terminal**: View real-time transcoding progress and success/failure status within the application.
- 🔄 **Safe Conversion**: Original files are never overwritten; outputs are saved alongside them with a `_ready.mov` suffix.
- ⚙️ **Optimized Outputs**: Uses high-quality **DNxHR HQ** video coding and uncompressed **16-bit PCM** audio.

---

## Prerequisites

Before running the application, ensure you have the following dependencies installed on your system:

### 1. Python 3 & Tkinter
Ensure Python 3 is installed. You will also need the Python Tkinter package:

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

### 2. FFmpeg
Make sure `ffmpeg` is installed and available in your system's PATH.

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

---

## How to Run

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
