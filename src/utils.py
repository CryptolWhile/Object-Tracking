def update_track_history(history, last_seen, ids, frame_count, batch_size, idx, max_len):
    current = set(ids)
    for tid in list(history.keys()):
        if tid in current:
            last_seen[tid] = frame_count - (batch_size - idx - 1)
        elif frame_count - last_seen[tid] > max_len:
            del history[tid]
            del last_seen[tid]
