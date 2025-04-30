import tensorflow as tf
import cv2
from pathlib import Path
from ultralytics import YOLO
import cv2

yolo_model = YOLO(Path('model','yolov8s.pt'))

model = tf.keras.models.load_model(
    filepath = Path('model','best_model.keras')
)

def load_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, (64, 64))  # Resize to a consistent size
    image = image / 255.0  # Normalize pixel values to [0, 1]
    return image

def predict_angle(image_path):
    image = load_image(image_path)
    example_image_expanded = tf.expand_dims(image, axis=0)  # Add batch dimension
    predicted_angle = model.predict(example_image_expanded)
    return predicted_angle[0][0]

def detect_and_draw_boxes(input_image_path, output_image_path, add_label = False):
    # Perform detection
    results = yolo_model(input_image_path)
    
    # Check if any detections were made
    if results[0].boxes is None:
        print("No detections made")
        return

    # Load the original image
    img = cv2.imread(input_image_path)
    
    # Loop through detections and draw bounding boxes with class names
    for box in results[0].boxes:
        # Get the box coordinates
        xyxy = box.xyxy[0].cpu().numpy()  # Convert to numpy array for easier access
        conf = box.conf[0].cpu().numpy()  # Confidence score
        cls = int(box.cls[0].cpu().numpy())  # Class ID
        
        # Draw bounding box
        cv2.rectangle(img, 
                      (int(xyxy[0]), int(xyxy[1])), 
                      (int(xyxy[2]), int(xyxy[3])), 
                      (0, 255, 0), 2)  # Green box with thickness of 2
        
        if add_label:
            class_name = model.names[cls]  # Get class name from model
            label = f"{class_name} {conf:.2f}"
            label = f"{class_name}"
            cv2.putText(img, label, 
                        (int(xyxy[0]), int(xyxy[1]) - 5),  # Text position (above the box)
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
                        (255, 0, 0), 1)  # Blue text with thickness of 2
    
    # Save the output image
    cv2.imwrite(output_image_path, img)

def video_prediction(video_path):
    steer = cv2.imread(Path('sample_data','steering_wheel_image.jpg'), 0)
    rows, cols = steer.shape
    smoothed_angle = 0
    cap = cv2.VideoCapture(video_path)
    while (cap.isOpened()):
        ret, frame = cap.read()
        cv2.imwrite("sample.jpg",frame)
        steering_angle = predict_angle("sample.jpg")
        detect_and_draw_boxes("sample.jpg", "sample.jpg", add_label = False)
        frame = cv2.imread("sample.jpg")
        print(steering_angle)
        cv2.imshow('frame', cv2.resize(frame, (600, 400), interpolation=cv2.INTER_AREA))
        smoothed_angle += 0.2 * pow(abs((steering_angle - smoothed_angle)), 2.0 / 3.0) * (
            steering_angle - smoothed_angle) / abs(
            steering_angle - smoothed_angle)
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -smoothed_angle, 1)
        dst = cv2.warpAffine(steer, M, (cols, rows))
        cv2.imshow("steering wheel", dst)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_prediction(Path('sample_data','output_video_2.mp4'))  # Replace with your video file path
