from ultralytics import YOLO

# Load YOLOv10n model from scratch
model = YOLO("yolov8m.pt")

# Train the model
model.train(data="pizza.yaml", epochs=500, batch=36, device=0, patience=20, resume=False)
