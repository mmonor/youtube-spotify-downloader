# YouTube Downloader GUI


##  Prerequisites

Before running the app, you need to have the following installed on your machine:
1. **Python 3.8+** (Make sure to check "Add Python to PATH" during installation)
2. **FFmpeg** (Required for converting audio to MP3 and merging high-quality video/audio streams)

### How to Install FFmpeg 
*Because FFmpeg is a large program and depends on your operating system, it is not included in this repository.*

* **Windows:**
  1. Download the essential build from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).
  2. Extract the `.zip` file.
  3. Go into the extracted `bin` folder.
  4. Copy `ffmpeg.exe` and `ffprobe.exe` and paste them **directly into this project's folder** (next to `main.py`).

* **Mac (using Homebrew):**
  Open your terminal and run: `brew install ffmpeg`

* **Linux (Debian/Ubuntu):**
  Open your terminal and run: `sudo apt install ffmpeg`

## 🚀 How to Run the App

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name