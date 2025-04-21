import os
from glob import glob
from pathlib import Path
import subprocess
from threading import Thread

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def get_video_files(directory: str) -> list[str]:
    video_files = []
    video_extensions = ["*.mp4", "*.webm", "*.avi", "*.mkv"]
    for ext in video_extensions:
        video_files.extend(glob(os.path.join(directory, ext)))
    return video_files

def stream_videos(video_files: list[str]):
    threads = []
    for video_path in video_files:
        threads.append(stream_video_to_url(video_path))
    for t in threads:
        t.join()

def stream_video_to_url(video_path: str) -> Thread:
    video_name = Path(video_path).stem
    # keep your original media-server URL here
    rtsp_url = f"rtsp://{USERNAME}:{PASSWORD}@media-server:8554/{video_name}"

    # build the GStreamer pipeline command
    command = [
        "gst-launch-1.0",
        "uridecodebin",        f"uri=file://{video_path}", "!",
        "videoconvert",        "!",
        "x264enc",             "tune=zerolatency",
                               "bitrate=1000",
                               "speed-preset=ultrafast",
                               "key-int-max=30",          "!",
        "h264parse",           "!",
        "rtspclientsink",      f"location={rtsp_url}",
                               "latency=0",
                               "protocols=tcp"
    ]

    thread = Thread(target=lambda: subprocess.run(command, check=True))
    thread.start()
    return thread

if __name__ == "__main__":
    folder = "/videos"
    videos = get_video_files(folder)
    stream_videos(videos)
