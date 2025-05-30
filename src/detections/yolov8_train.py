from ultralytics import YOLO

def train_yolov8():
    model = YOLO("yolov8n.yaml")

    model.train(
        data=r"D:\Vehical type detection and speed estimation\data\images\data.yaml",  
        epochs=50,
        imgsz=640,
        batch=8,
        device="cpu",
        name="vehicle_detector_cpu"
    )

if __name__ == "__main__":
    train_yolov8()
