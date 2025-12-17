# Processed Image Dehazing Dataset

This dataset was created as part of the project
**"Haze Removal using AI and Computer Vision"**.

The dataset is a **processed and augmented version** of multiple publicly
available haze datasets obtained from Kaggle.

---

## Source Datasets (Kaggle)

The following benchmark datasets were used as source data:

- **O-HAZE** – Real outdoor hazy and haze-free image pairs  
- **NH-HAZE** – Non-homogeneous real-world haze dataset  
- **Dense-Haze** – Real heavy-haze dataset (CVPR 2019)

All datasets were accessed via Kaggle for academic and research use.

---

## Dataset Processing Pipeline

The original datasets were combined and processed using the following steps:

### 1. Preprocessing
- Image resizing to a fixed resolution
- Normalization of pixel values
- Removal of corrupted or inconsistent samples

### 2. Data Augmentation
To reduce overfitting and improve generalization, the following augmentation
techniques were applied:
- Rotation
- Horizontal flipping
- Zooming
- Shearing

### 3. Dataset Concatenation
For supervised learning, **clear (ground truth) images and corresponding hazy images**
were concatenated to form paired training samples suitable for
image-to-image translation models such as Pix2Pix.

**Concatenation format:**
[ Hazy Image | Clear Image ]
This format is suitable for image-to-image translation frameworks such as
Pix2Pix.

---

## 🔹 Dataset Structure (Local)

```text
dataset/
├── train/
│   └── hazy_clear_concat/
├── validation/
└── test/

## 🔹 Access & Licensing
Due to dataset size and licensing constraints, the full processed dataset is not
hosted in this repository.

Users are encouraged to download the original datasets from Kaggle and
reproduce the preprocessing pipeline described above.

This dataset is intended strictly for academic and research purposes.

## 🔹 Usage
This processed dataset was used for:
- Training image dehazing models
- Cross-dataset generalization experiments
- PSNR and SSIM evaluation

## 🔹 Citation
If you use this dataset preparation methodology, please cite the original datasets:
- O-HAZE
- NH-HAZE
- Dense-Haze
