from ultralytics import YOLO

# model = YOLO('models/best-80.pt') #load model
model = YOLO('yolov8x')

results = model.track('input_video/input_video.mp4', conf=0.2,save=True)