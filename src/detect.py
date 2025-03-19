import cv2
from ultralytics import YOLO

# Paths
MODEL_PATH = "path_to_model/best.pt"
VIDEO_INPUT_PATH = "path_to_input_video.mp4"
VIDEO_OUTPUT_PATH = "path_to_output_video.mp4"

# Load model and video
model = YOLO(MODEL_PATH)
cap = cv2.VideoCapture(VIDEO_INPUT_PATH)

# Video properties
width, height = int(cap.get(3)), int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(VIDEO_OUTPUT_PATH, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.5)
    tomato_count = 0  

    for box in results[0].boxes:
        if int(box.cls.item()) == 0:  
            tomato_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 153, 0), 2)

    cv2.putText(frame, f"Tomatoes detected: {tomato_count}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 153, 0), 2)

    out.write(frame)

cap.release()
out.release()

print(f"Processed video saved at: {VIDEO_OUTPUT_PATH}")
