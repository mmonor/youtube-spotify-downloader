from yt_dlp import YoutubeDL
import os

def download(url, desired_format, save_path, progress_hook=None):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
    }

    if progress_hook:
        ydl_opts['progress_hooks'] = [progress_hook]

    if desired_format == 'audio':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ]

    elif desired_format == 'video':
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
        ydl_opts['merge_output_format'] = 'mp4'

    print("Downloading " + url + " in " + save_path)
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])