# Aerial-Image-Dehazing-pix2pix
Image dehazing using Pix2Pix GAN on RESIDE, Dense-Haze, NH-Haze and O-HAZE datasets

# 🌫️ Haze Removal using AI and Computer Vision

### Satellite Image Dehazing using Deep Learning

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Results](#results)
- [How to Run](#how-to-run)
- [Future Work](#future-work)

## 📌 Project Overview

Haze removal (also known as *image dehazing*) is a fundamental problem in computer vision that aims to restore clear images from haze-degraded inputs caused by atmospheric particles such as dust, smoke, fog, and pollution. Haze significantly reduces image contrast, color fidelity, and edge sharpness, affecting applications like autonomous driving, satellite imaging, surveillance, and remote sensing.

This project implements **deep learning–based image dehazing techniques**, focusing on **CNN and GAN-based architectures** to enhance visual quality and restore structural details from hazy images. The work was carried out as part of an **internship at the School of Artificial Intelligence, Amrita Vishwa Vidyapeetham** .

A custom dataset was built by preprocessing, augmenting, and concatenating O-HAZE, NH-HAZE, and Dense-Haze images obtained from Kaggle.


---

## 🎯 Objectives

* Study traditional and deep learning–based haze removal techniques
* Train deep neural networks on multiple benchmark haze datasets
* Analyze overfitting and improve generalization using **data augmentation**
* Evaluate performance using **PSNR** and **SSIM** metrics
* Perform **cross-dataset testing** to assess real-world robustness

---

---

# 🏠 2. UPDATED MAIN `README.md` (Front Page Update)

👉 This goes in the **root `README.md`** of your repository.  
You can **replace or merge** with your existing README.

---

## 📂 Dataset Description

This project uses a **custom processed image dehazing dataset** created by
combining multiple benchmark haze datasets obtained from Kaggle.

The dataset includes images from:
- **O-HAZE**
- **NH-HAZE**
- **Dense-Haze**

The original datasets were **preprocessed, augmented, and concatenated**
to create paired samples suitable for supervised deep learning–based
image dehazing.

### Dataset Highlights
- Multi-dataset training for better generalization
- Data augmentation to reduce overfitting
- Concatenated hazy–clear image pairs for image-to-image translation models

📌 The full dataset is **not included** in this repository due to size and licensing
restrictions.  
Detailed dataset preparation steps are available in [`data/README.md`](data/README.md).

---

## 🧠 Methodology

### 1️⃣ Model Strategy

Multiple deep learning models were trained using **different dataset combinations** to analyze generalization behavior:

| Model | Training Data        | Testing Data |
| ----- | -------------------- | ------------ |
| M1    | Mixed datasets       | O-HAZE       |
| M2    | Mixed datasets       | NH-HAZE      |
| M3    | Mixed datasets       | Dense-Haze   |
| M4    | NH-HAZE + Dense-Haze | O-HAZE       |

These configurations help evaluate how well a model trained on one distribution performs on unseen haze conditions .

---

### 2️⃣ Data Augmentation

To address **overfitting**, augmentation techniques were applied:

* Rotation
* Shearing
* Zoom
* Horizontal flip

This increased the training dataset size from **60 images to 120 images**, leading to more stable training and improved generalization .

---

## 📂 Datasets Used

| Dataset        | Description                         | Usage              |
| -------------- | ----------------------------------- | ------------------ |
| **RESIDE**     | Synthetic indoor & outdoor haze     | Training           |
| **O-HAZE**     | Real outdoor hazy & haze-free pairs | Training & Testing |
| **NH-HAZE**    | Non-homogeneous real haze           | Evaluation         |
| **Dense-Haze** | Heavy real-world haze (CVPR 2019)   | Benchmark testing  |

📌 **Note:** Datasets are **not included** in this repository.
Please refer to `data/README.md` for download links and folder structure.

---

## 📊 Evaluation Metrics

### 🔹 PSNR (Peak Signal-to-Noise Ratio)

* Measures reconstruction quality
* Higher PSNR = better noise suppression

### 🔹 SSIM (Structural Similarity Index)

* Measures perceptual and structural similarity
* Higher SSIM = better structure preservation

Both metrics were used to analyze **quantitative performance before and after augmentation** .

---

## 📊 Results Summary
Sample qualitative and quantitative results are provided in the `results/` folder,
demonstrating improvement in visibility and image quality after dehazing.


### 🔸 Key Observations

* All models showed **overfitting before augmentation**
* Data augmentation improved training stability
* **Model M3** showed the **best PSNR improvement** after augmentation
* **M1 and M4** suffered SSIM reduction, indicating structural degradation
* Cross-dataset generalization remains challenging for dense haze conditions 

---

### 🔸 Sample PSNR / SSIM (After Augmentation)

| Model  | PSNR (dB)  | SSIM  |
| ------ | ---------- | ----- |
| M1     | ~28.01     | ↓     |
| M2     | ~27.97     | ↓     |
| **M3** | **~28.79** | **↑** |
| M4     | ~28.00     | ↓     |

📌 Detailed tables and plots are available in the **internship report**.

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* CNN & UNet architectures
* GAN-based learning
* Image Augmentation
* PSNR & SSIM metrics
* GPU-based training

---

## 🔍 Key Learnings

* Data augmentation plays a crucial role in reducing overfitting
* Training on mixed datasets improves robustness but may affect structure
* PSNR alone is insufficient — SSIM is critical for perceptual quality
* Cross-dataset evaluation is essential for real-world deployment .

---

## 🚀 Future Work

* Incorporating **perceptual loss** for better visual quality
* Transformer-based dehazing architectures
* Domain adaptation for real satellite imagery
* Integration with downstream tasks (object detection, segmentation)

---

## ⭐ Final Note

This repository is intended for **academic, research, and learning purposes**.
Feel free to explore, extend, or adapt the methodology.

---
