from src.tracking import run_tracking
from config.config_loader import load_config

if __name__ == "__main__":
    video_path = "samples/vietnam.mp4"
    output_dir = "outputs"

    config = load_config("config/config.yaml")
    run_tracking(video_path, output_dir, config)
