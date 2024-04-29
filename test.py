from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO('yolov8n-oiv7.pt')
results = model("D:\\S4\\Conduite\\Object\\2165-155327596_tiny.mp4",show=True,save=True)