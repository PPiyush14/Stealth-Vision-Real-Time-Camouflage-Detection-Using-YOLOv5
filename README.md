#  Stealth Vision — Real-Time Camouflage Detection Using YOLOv5

> A lightweight, real-time camouflage detection system fine-tuned on YOLOv5 and deployed on Raspberry Pi 5 for autonomous, offline edge inference across diverse terrains.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![YOLOv5](https://img.shields.io/badge/YOLOv5-Ultralytics-00FFFF?style=flat)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=flat&logo=raspberrypi&logoColor=white)

---

##  What It Does

Traditional object detection fails when targets intentionally blend into their surroundings. This system detects camouflaged people by identifying subtle **texture, edge, and color inconsistencies** between the target and its background — even in forests, arctic, urban, and arid terrains.

The model runs **fully offline on a Raspberry Pi 5** with a simple UI for image upload and real-time detection output.

---

##  System Architecture

```
Camera / Image Input
        │
        ▼
┌──────────────────────────────┐
│  Pre-Processing (OpenCV)     │  ← Resize 640×640, normalize, RGB convert
│  + Brightness / Contrast     │    Optional enhancement for low-contrast scenes
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│  YOLOv5 Detection Model      │
│  ├── Backbone  (feature ext) │
│  ├── Neck      (multi-scale) │
│  └── Head      (bbox + conf) │
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│  Post-Processing             │  ← NMS, confidence threshold (0.25–0.3)
└──────────────────────────────┘
        │
        ▼
  Annotated Output + Bounding Boxes
  (UI / saved image / live stream)
```

---

##  Results

| Environment | Detection | Confidence Score |
|-------------|-----------|-----------------|
| Arctic / Snowy | ✅ Detected (2 targets) | 0.69, 0.91 |
| Arctic / Snowy (complex) | ✅ Detected | 0.92 |
| Forest / Woodland | ✅ Detected (extreme background) | 0.92 |

The model reliably identifies camouflaged targets by learning **non-natural edges, outlines, and textures** rather than color alone — consistent high confidence scores across all terrain types.

---

##  Dataset

- **~10,000 images** collected across woodland, arid, arctic, and urban terrains
- **Single class:** `camouflage` (person wearing camouflage)
- **Annotation:** Bounding boxes labeled using LabelImg

| Split | Size |
|-------|------|
| Training | 80% |
| Validation | 10% |
| Testing | 10% |

---

##  Training Configuration

| Parameter | Value |
|-----------|-------|
| Architecture | YOLOv5 (fine-tuned) |
| Input Resolution | 640×640 |
| Optimizer | SGD |
| Batch Size | 16 |
| Loss Functions | Regression + Objectness + Classification |

**Data Augmentation:**
- Geometric: Scaling, Mosaic, Translation, Horizontal Flip
- Photometric: Brightness, Contrast, Saturation adjustments

---

##  Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/PPiyush14/Stealth-Vision-Camouflage-Detection-Using-YOLOv5.git
cd Stealth-Vision-Camouflage-Detection-Using-YOLOv5
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run detection
```bash
python new_deeplearning.py --source test1.jpg
```

> For webcam: `--source 0`  
> For a folder of images: `--source path/to/images/`

---

##  Hardware & Software

| Component | Details |
|-----------|---------|
| Edge Platform | Raspberry Pi 5 |
| CPU | Quad-core ARM Cortex-A72 |
| OS | Raspberry Pi OS / Ubuntu 22.04 |
| Language | Python 3.9 |
| Libraries | PyTorch, OpenCV, NumPy, Matplotlib |
| Input Resolution | 640×640 px |
| FPS (Raspberry Pi) | 10–12 FPS |
| FPS (GPU system) | ~45 FPS |

---

##  Key Features

- **Edge deployable** — runs fully offline on Raspberry Pi, no cloud needed
- **Real-time inference** — optimized YOLOv5 for low-power hardware
- **Multi-terrain** — trained on forest, arctic, urban, and arid environments
- **Simple UI** — upload an image and view detection output on-device
- **Scalable** — architecture can integrate with drones or surveillance systems

---

##  Future Scope

- **Thermal camera fusion** — integrate IR for 24/7 night detection
- **Model quantization/pruning** — improve FPS for smoother video streams
- **Real-time alert system** — trigger alarms when camouflaged target detected
- **Monitoring dashboard** — live view of deployed units

---

##  Authors

**Piyush Rajvaidya**
[![GitHub](https://img.shields.io/badge/GitHub-PPiyush14-black?logo=github)](https://github.com/PPiyush14)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Piyush%20Rajvaidya-blue?logo=linkedin)](https://www.linkedin.com/in/piyush-rajvaidya/)

**Tanishq Ratdiya · Rajat Dwivedi · Trijal Singh Babbar**  
*Department of AI & ML, Symbiosis Institute of Technology, Pune*
