import os
import cv2
from ultralytics import YOLO

model = YOLO("best.pt")  # Model dosyan buraya eklenecek

def run_detection(image_path):
    results = model(image_path)
    result = results[0]

    img = cv2.imread(image_path)
    for box in result.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    output_path = image_path.replace("uploads", "uploads/detected")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, img)
    return output_path
