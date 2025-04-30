from ultralytics import YOLO
import cv2
import math
from pathlib import Path

model_path = Path("model","signal.pt")
signal_model = YOLO(model_path)

# Define object classes
classNames = ["green", "red", "yellow"]

def detect_signal_color(image_path, output_path):
    signal_detected = {}

    img = cv2.imread(image_path)

    results = signal_model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for idx,box in enumerate(boxes):
            # Bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Get confidence and class index
            confidence = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            # Print signal color based on detected class
            signal_color = classNames[cls]
            signal_detected[idx] = signal_color
            print(f"Detected signal color: {signal_color} with confidence {confidence}")

            # Draw bounding box and label on the image
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.putText(img, f"{idx}", (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)

    # Save output image with highlighted objects
    cv2.imwrite(output_path, img)

    return signal_detected

if __name__ == "__main__":
    input_image_path = "sample_data/Screenshot from 2024-11-10 12-17-42.png"
    output_image_path = "output_image.jpeg"
    signal_detected = detect_signal_color(input_image_path, output_image_path)
    print(signal_detected)

