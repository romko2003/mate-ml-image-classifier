# 🐱🐶 Cats vs Dogs — ML Classification Web App

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![ML](https://img.shields.io/badge/Machine%20Learning-CNN-green)
![Status](https://img.shields.io/badge/Project-Mate%20Academy-orange)

A simple **image classification web application** that predicts whether an uploaded image contains a **cat** or a **dog**.

The machine learning model was trained in **Google Colab** and integrated into a **Flask web interface**.

---

## 🚀 Demo

## 🧠 Model

- **Task:** Binary image classification (Cat vs Dog)
- **Model:** Convolutional Neural Network (CNN)
- **Training:** Google Colab
- **Output:** predicted class + confidence score

Accuracy achieved on test set: **80–95%** (depending on training run).

---

## 📦 Dataset

This project uses a labeled **Cats vs Dogs** image dataset.


Dataset structure:

data/
train/
cats/
dogs/
test/
cats/
dogs/


---

## 🧪 Training

Model training was performed in Google Colab.

Training pipeline:

1. Load dataset
2. Resize and normalize images
3. Build CNN model
4. Train model
5. Evaluate accuracy
6. Save trained model
7. Export model to project

Saved model location:

model/model.pt


---

## 🧱 Project structure

mate-ml-image-classifier/
│
├── app/
│ ├── classifier/
│ │ ├── model.py
│ │ └── predict.py
│ │
│ ├── static/
│ │ └── style.css
│ │
│ ├── templates/
│ │ ├── index.html
│ │ └── result.html
│ │
│ └── main.py
│
├── data/
├── model/
├── notebooks/
│ └── train_colab.ipynb
│
├── requirements.txt
└── README.md


---

## ⚙️ How to run locally

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/mate-ml-image-classifier.git
cd mate-ml-image-classifier
2. Create virtual environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the app
python app/main.py
5. Open in browser
http://127.0.0.1:5000
✨ Features
Upload image via web interface

Real-time prediction

Confidence score display

Clean UI

Separated ML logic from frontend

🔧 Future improvements
Multi-class classification

Drag & drop upload

Cloud deployment

Model optimization

REST API endpoint

👤 Author
Roman Azhniuk
Mate Academy student