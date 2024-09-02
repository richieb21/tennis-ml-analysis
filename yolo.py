from ultralytics import YOLO

model = YOLO('yolov8x') #load model

results = model.predict('input_video.mp4', save=True)
print(results)
for box in results[0].boxes:
    print(box)