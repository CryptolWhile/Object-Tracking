import os
import cv2

def initialize_video(video_path, output_dir):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    name = os.path.basename(video_path).split(".")[0]
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{name}_tracked.mp4")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    return cap, out, out_path, fps
