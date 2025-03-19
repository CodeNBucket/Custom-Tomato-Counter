from ultralytics import YOLO

# Paths
DATA_PATH = "path_to_dataset/data.yaml"
SAVE_DIR = "path_to_save_model"

def train():
    model = YOLO("yolov8s.pt")  
    model.train(
        data=DATA_PATH,
        epochs=200,
        device="cuda",  
        project=SAVE_DIR,  
        name="Tomato_Result"  
    )

if __name__ == "__main__":
    train()
