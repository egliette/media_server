# based on https://github.com/roboflow/supervision/blob/develop/examples/time_in_zone/scripts/stream_from_file.py
import os
from glob import glob
from pathlib import Path
import subprocess
from threading import Thread


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


def get_video_files(directory: str) -> list:
    video_files = []
    video_extensions = ["*.mp4", "*.webm", "*.avi", "*.mkv"]
    for extension in video_extensions:
        video_files.extend(glob(os.path.join(directory, extension)))
    return video_files

def stream_videos(video_files: list[str]):
    threads = []
    for video_path in video_files:
        thread = stream_video_to_url(video_path)
        threads.append(thread)
    for thread in threads:
        thread.join()

def stream_video_to_url(video_path: str) -> Thread:
    video_name = Path(video_path).stem
    rtsp_url = f"rtsp://{USERNAME}:{PASSWORD}@media-server:8554/{video_name}"
    command = [
        "ffmpeg", 
        "-re", 
        "-stream_loop", "-1", 
        "-i", video_path,

        # Low‑latency flags
        "-fflags", "nobuffer",
        "-flags", "low_delay",
        "-max_delay", "0",
        "-tune", "zerolatency",

        # Encoder and preset
        "-c:v", "libx264",
        "-preset", "ultrafast",

        # Output format
        "-f", "rtsp", 
        rtsp_url
    ]
    return run_command_in_thread(command)

def run_command_in_thread(command: list) -> Thread:
    thread = Thread(target=run_command, args=(command,))
    thread.start()
    return thread

def run_command(command: list) -> int:
    process = subprocess.run(command)
    return process.returncode


if __name__ == "__main__":
    folder_path = '/videos'
    video_files = get_video_files(folder_path)
    stream_videos(video_files)
