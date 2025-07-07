import cv2
import numpy as np

def draw_tracks(frame, boxes, ids, history, config):
    if not ids:
        return frame
    for box, tid in zip(boxes, ids):
        x, y, w, h = box
        track = history[tid]
        track.append((float(x), float(y)))
        if len(track) > config["track_history_length"]:
            track.pop(0)
        points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [points], isClosed=False, color=config["track_color"], thickness=config["line_thickness"])
    return frame
