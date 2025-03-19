# 🍅 Custom Tomato Counter – YOLOv8  
This project trains a **YOLOv8 model** to detect and count tomatoes in videos. The dataset was **custom-labeled using Roboflow** and trained on **manually annotated images** for improved accuracy.

---

## 📌 How This Project Was Done  
### 1️⃣ Dataset Creation & Labeling  
- Images were sourced from the **[reference video](https://www.youtube.com/watch?v=A5gJwKFsTj0)**.  
- Each image was **manually labeled in Roboflow** with bounding boxes for tomatoes.  
- **Augmentation** (flipping, rotation, brightness changes) increased dataset size to **350+ images**.  

### 2️⃣ Model Training  
- Trained a **YOLOv8** model from scratch on the custom dataset.  
- Used **200 epochs with GPU acceleration** for optimal results.  

### 3️⃣ Inference & Counting  
- Detects and counts tomatoes in video frames.  
- Bounding boxes are drawn, and the total count is displayed in real-time.

---

## 🚀 Setup & Usage  
### 1️⃣ Clone the repository  
```bash
git clone https://github.com/CodeNBucket/Custom-Tomato-Counter.git
cd Custom-Tomato-Counter
```

### 2️⃣ Install dependencies  
```bash
pip install -r src/requirements.txt
```

### 3️⃣ Train the model  
```bash
python src/train.py
```

### 4️⃣ Run detection on a video  
```bash
python src/detect.py
```

---

## 🎥 Example Videos  
🔹 Two example videos are provided in the **videos/** folder:

---

## 📂 Project Structure  
```
Custom-Tomato-Counter/
├── dataset/                    # Labeled dataset (YOLO format)
├── runs/train/exp/              # YOLO training logs & results
│   ├── weights/                  # Trained YOLO model (best.pt)
├── videos/                      # Example videos
├── src/                         # Source code
│   ├── train.py                  # Training script
│   ├── detect.py                 # Detection script
│   ├── requirements.txt          # Dependencies
├── README.md                     
└── .gitignore                    
```

---


