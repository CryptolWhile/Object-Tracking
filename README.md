
# 🎯 YOLOv8 Multi-Object Tracking with BoT-SORT

Track multiple objects in video streams using YOLOv8 + BoT-SORT with efficient batching and dynamic motion visualization.

![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)
![Top Lang](https://img.shields.io/github/languages/top/CryptolWhile/Object-Tracking?style=flat-square)
![License](https://img.shields.io/github/license/CryptolWhile/Object-Tracking?style=flat-square)

---

## 🔍 Overview

This repository provides a clean, efficient, and scalable pipeline to perform **multi-object tracking** on videos using **Ultralytics YOLOv8** and **BoT-SORT**.

Features:

- ✅ YOLOv8 inference with persistent BoT-SORT tracking
- 🧵 Batch processing for performance
- 🎞️ Historical motion trails per object
- ⚙️ Modularized codebase for easy customization
- 💻 Works both locally and on Google Colab (with GPU)

---

## 🧩 Folder Structure

```bash
Object-Tracking/
├── main.py                   # Main tracking script
├── requirements.txt          # Python dependencies
├── models/                   # Pretrained YOLO models
│   └── yolo11x.pt
├── samples/                  # Input video files
│   └── vietnam.mp4
├── outputs/                  # Output tracking videos
│   └── vietnam_tracked.mp4
├── src/
│   └── utils.py              # Logging/helper functions
├── notebooks/
│   └── Object_Tracking.ipynb # Google Colab-ready notebook
└── README.md
````

---

## 🚀 Quick Start

### 1️⃣ Clone and Install

```bash
git clone https://github.com/CryptolWhile/Object-Tracking.git
cd Object-Tracking
pip install -r requirements.txt
```

> 💡 *Optional: use a Python virtual environment for isolation*

---

### 2️⃣ Add Inputs

* 🎥 Put your input video in `samples/` (e.g., `vietnam.mp4`)
* 🧠 Place your YOLO model in `models/` (e.g., `yolo11x.pt`)

---

### 3️⃣ Run Locally

```bash
python main.py --video-path samples/vietnam.mp4
```

🎬 Output will be saved to `outputs/vietnam_tracked.mp4`.

---

### ☁️ Run on Google Colab

📌 Use `notebooks/Object_Tracking.ipynb` to run tracking in Colab with GPU.

Includes:

* 🔗 Google Drive integration
* 📁 Model + video upload
* 🧠 YOLOv8 + BoT-SORT batching
* 📤 Output video saved back to Drive

---

## ⚙️ Config Example

You can adjust configuration directly in `main.py` or a config module:

```python
return {
    "model_path": "models/yolo11x.pt",
    "track_history_length": 120,
    "batch_size": 64,
    "line_thickness": 4,
    "track_color": (230, 230, 230),
}
```

👉 To process the full video (not just first 3 seconds), replace:

```python
frames_to_process = int(fps * 3)
```

with:

```python
frames_to_process = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
```

---

## 📦 Requirements

```txt
ultralytics==8.3.162
opencv-python==4.11.0
numpy==2.0.2
tqdm==4.67.1
PyYAML==6.0.2
```

Install via:

```bash
pip install -r requirements.txt
```

---

## 🎬 Example Output

<p align="center">
  <img src="assets/tracking_preview.gif" width="640" alt="Tracking Demo Preview"/>
</p>

> Output sample from `outputs/vietnam_tracked.mp4`, showing tracked objects with trail lines using YOLOv8 + BoT-SORT.

---

## 📄 License

MIT License — See [`LICENSE`](LICENSE)

---

## 🌟 Contribute

Contributions, issues and feature requests are welcome!

If you find this project useful, please consider giving it a ⭐ on GitHub!

---
