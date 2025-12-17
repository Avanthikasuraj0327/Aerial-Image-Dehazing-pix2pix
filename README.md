
# 🌫️ Aerial Image Dehazing using Pix2Pix GAN

![Deep Learning](https://img.shields.io/badge/Deep%20Learning-GAN-blue)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-Image%20Dehazing-green)
![Python](https://img.shields.io/badge/Python-3.x-yellow)

---

## 📌 Project Overview

Haze significantly degrades image quality by reducing contrast, distorting colors, and obscuring structural details. This project focuses on **aerial and satellite image dehazing** using a **Pix2Pix Conditional GAN**, enabling effective restoration of haze-free images from hazy inputs.

The work emphasizes **cross-dataset generalization**, **data augmentation**, and **quantitative evaluation** using PSNR and SSIM metrics. A **custom processed dataset** was created by combining multiple benchmark haze datasets.

---

## 📌 Table of Contents

* [Dataset Description](#-dataset-description)
* [Methodology](#-methodology)
* [Evaluation Metrics](#-evaluation-metrics)
* [Results Summary](#-results-summary)
* [Repository Structure](#-repository-structure)
* [How to Run](#-how-to-run)
* [Future Work](#-future-work)
* [Acknowledgment](#-acknowledgment)

---

## 📂 Dataset Description

A **custom processed image dehazing dataset** was built using benchmark datasets obtained from **Kaggle**:

* **O-HAZE** – Real outdoor hazy and haze-free image pairs
* **NH-HAZE** – Non-homogeneous real-world haze dataset
* **Dense-Haze** – Real heavy haze dataset (CVPR 2019)

### Dataset Preparation

* Images were **preprocessed** (resizing, normalization)
* **Data augmentation** was applied to reduce overfitting
* Corresponding **hazy and clear images were concatenated** to form paired samples:

```
[ Hazy Image | Clear Image ]
```

📌 **Note:**
The full dataset is **not included** in this repository due to size and licensing constraints.
Detailed dataset preparation, usage, and citation information is available in
👉 [`data/README.md`](data/README.md)

---

## 🧠 Methodology

* **Model:** Pix2Pix (Conditional GAN)
* **Generator:** U-Net based architecture
* **Discriminator:** PatchGAN
* **Training Strategy:**

  * Multi-dataset training
  * Cross-dataset testing
  * Early stopping to reduce overfitting

### Model Configurations

| Model | Training Dataset     | Testing Dataset |
| ----- | -------------------- | --------------- |
| M1    | Mixed datasets       | O-HAZE          |
| M2    | Mixed datasets       | NH-HAZE         |
| M3    | Mixed datasets       | Dense-Haze      |
| M4    | NH-HAZE + Dense-Haze | O-HAZE          |

---

## 📊 Evaluation Metrics

* **PSNR (Peak Signal-to-Noise Ratio)**
  Measures reconstruction quality and noise suppression.
* **SSIM (Structural Similarity Index)**
  Measures perceptual and structural similarity.

Both metrics were used to analyze **image quality before and after augmentation**.

---

## 📈 Results Summary

### Key Observations

* Initial models showed **overfitting**
* **Data augmentation improved training stability**
* **Model M3** achieved the **best PSNR improvement**
* Some models experienced SSIM reduction, indicating structural trade-offs
* Cross-dataset generalization remains challenging for dense haze scenarios

📌 Sample qualitative and quantitative results are provided in the `results/` folder.

---

## 📁 Repository Structure

```
Aerial-Image-Dehazing-pix2pix/
├── src/
│   ├── model.py
│   ├── dataset.py
│   ├── train.py
│   ├── test.py
│   └── metrics.py
├── data/
│   └── README.md
├── results/
│   ├── qualitative/
│   └── quantitative/
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/Avanthikasuraj0327/Aerial-Image-Dehazing-pix2pix.git
cd Aerial-Image-Dehazing-pix2pix

# Install dependencies
pip install -r requirements.txt

# Prepare dataset (as described in data/README.md)

# Train model
python src/train.py

# Test model
python src/test.py
```

📌 GPU-based training was used during experimentation.

---

## 🔮 Future Work

* Transformer-based dehazing models
* Perceptual loss integration for improved visual quality
* Domain adaptation for real-world deployment
* Integration with downstream tasks (object detection, segmentation)

---

## 🏫 Acknowledgment

This project was carried out as part of an **internship in Artificial Intelligence & Computer Vision** at
**School of Artificial Intelligence, Amrita Vishwa Vidyapeetham, Coimbatore**.

---

## ⭐ Final Note

This repository is intended for **academic and research purposes** and demonstrates dataset engineering, deep learning model training, and evaluation for image dehazing tasks.

---

