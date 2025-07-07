import cv2
from collections import defaultdict
from tqdm import tqdm
from ultralytics import YOLO
from .visualization import draw_tracks
from .video_utils import initialize_video
from .utils import update_track_history

def process_batch(model, batch_frames, track_history, last_seen, frame_count, config):
    results = model.track(batch_frames, persist=True, tracker="botsort.yaml", show=False, verbose=False)
    processed = []

    for idx, result in enumerate(results):
        boxes = result.boxes.xywh.cpu()
        ids = result.boxes.id.int().cpu().tolist() if result.boxes.id is not None else []
        update_track_history(track_history, last_seen, ids, frame_count, len(batch_frames), idx, config["track_history_length"])
        frame = result.plot(font_size=4, line_width=2)
        frame = draw_tracks(frame, boxes, ids, track_history, config)
        processed.append(frame)

    return processed

def run_tracking(video_path, output_dir, config):
    model = YOLO(config["model_path"])
    cap, out, output_path, fps = initialize_video(video_path, output_dir)

    track_history = defaultdict(list)
    last_seen = defaultdict(int)
    batch_frames = []
    frame_count = 0

    with tqdm(desc="Processing video", colour="green") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            batch_frames.append(frame)

            if len(batch_frames) == config["batch_size"]:
                frames = process_batch(model, batch_frames, track_history, last_seen, frame_count, config)
                for f in frames:
                    out.write(f)
                    pbar.update(1)
                batch_frames = []

        if batch_frames:
            frames = process_batch(model, batch_frames, track_history, last_seen, frame_count, config)
            for f in frames:
                out.write(f)
                pbar.update(1)

    cap.release()
    out.release()
    print(f"✅ Done. Output saved to {output_path}")
