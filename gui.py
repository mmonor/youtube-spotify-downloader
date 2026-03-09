import customtkinter as ctk
import threading
import re
from download import download


class DownloadApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Downloader")
        self.geometry("550x600")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.title_label = ctk.CTkLabel(self, text="YouTube Downloader", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        self.url_entry = ctk.CTkEntry(self, placeholder_text="Paste your playlist/video link", width=300, height=40)
        self.url_entry.pack(pady=10)

        self.folder_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.folder_frame.pack(pady=10)

        self.folder_entry = ctk.CTkEntry(self.folder_frame, placeholder_text="Choose save folder...", width=200,
                                         height=40)
        self.folder_entry.pack(side="left", padx=(0, 10))

        self.browse_button = ctk.CTkButton(self.folder_frame, text="Browse", width=90, height=40,
                                           command=self.browse_folder)
        self.browse_button.pack(side="right")

        self.format_var = ctk.StringVar(value="Audio")
        self.format_menu = ctk.CTkOptionMenu(self, variable=self.format_var, values=["Audio", "Video"], width=300,
                                             height=40)
        self.format_menu.pack(pady=15)

        self.download_button = ctk.CTkButton(self, text="Download", font=("Arial", 14, "bold"),
                                             command=self.start_download, height=50, width=300)
        self.download_button.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self, width=300)
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def browse_folder(self):
        selected_folder = ctk.filedialog.askdirectory(title="Select Save Folder")
        if selected_folder:
            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, selected_folder)

    def update_progress(self, d):
        if d['status'] == 'downloading':
            try:
                percent_str = re.sub(r'\x1b\[[0-9;]*m', '', d['_percent_str']).strip().replace('%', '')
                percent = float(percent_str) / 100.0
                self.progress_bar.set(percent)

                speed = d.get('_speed_str', 'N/A').strip()
                clean_speed = re.sub(r'\x1b\[[0-9;]*m', '', speed)

                self.after(0, lambda: self.status_label.configure(
                    text=f"Downloading... {percent * 100:.1f}% (Speed: {clean_speed})"))
            except Exception:
                pass
        elif d['status'] == 'finished':
            self.after(0, lambda: self.status_label.configure(text="Processing... Please wait"))
            self.after(0, lambda: self.progress_bar.set(1))

    def start_download(self):
        url = self.url_entry.get()
        desired_format = self.format_var.get().lower()
        save_path = self.folder_entry.get()

        if not url:
            self.status_label.configure(text="Please enter a valid URL")
            return
        if not save_path:
            self.status_label.configure(text="Please select a save folder")
            return

        self.status_label.configure(text="Starting download...")
        self.download_button.configure(state="disabled")

        self.progress_bar.pack(pady=5, before=self.status_label)
        self.progress_bar.set(0)

        thread = threading.Thread(target=self.try_download, args=(url, desired_format, save_path))
        thread.start()

    def try_download(self, url, desired_format, save_path):
        try:
            download(url, desired_format, save_path, progress_hook=self.update_progress)
            self.after(0, lambda: self.status_label.configure(text="Successfully downloaded"))
        except Exception as e:
            self.after(0, lambda: self.status_label.configure(text="Failed to download"))
            print(e)
        finally:
            self.after(0, lambda: self.download_button.configure(state="normal"))
            self.after(0, lambda: self.url_entry.delete(0, "end"))


