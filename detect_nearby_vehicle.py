import cv2
from ultralytics import YOLO
from pathlib import Path

model_path = Path("model","yolov8s.pt")
vehicle_model = YOLO(model_path)

def draw_bounding_boxes_in_range(input_image_path, output_image_path, start_vertical_line, end_vertical_line):
    n_vehicle = 0
    object_distance_dict = {}

    # Load the image
    image = cv2.imread(input_image_path)
    height, width, _ = image.shape

    # Run inference on the image
    results = vehicle_model(input_image_path)

    # Extract bounding box coordinates and labels from results
    boxes = results[0].boxes  # Get the first result (assuming only one image)

    # Calculate the x-coordinates of the start and end vertical lines
    start_x = (start_vertical_line / 100) * width
    end_x = (end_vertical_line / 100) * width

    # Draw vertical reference lines on the image
    cv2.line(image, (int(start_x), 0), (int(start_x), height), (0, 0, 255), 2)  # Red line for start vertical
    cv2.line(image, (int(end_x), 0), (int(end_x), height), (0, 0, 255), 2)  # Red line for end vertical

    # Filter boxes: only keep those within the vertical line range
    filtered_boxes = []
    for idx, box in enumerate(boxes):
        xmin, ymin, xmax, ymax = box.xyxy[0].cpu().numpy()  # Extract coordinates (xyxy format)
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        # Check if the bounding box is within the specified range
        if xmin >= start_x and xmax <= end_x:
            n_vehicle += 1
            filtered_boxes.append((xmin, ymin, xmax, ymax))
            
            # Calculate distance as the inverse of the bounding box area (approximation)
            box_area = (xmax - xmin) * (ymax - ymin)
            distance = 1 / box_area if box_area > 0 else float('inf')  # Avoid division by zero
            object_distance_dict[idx] = (distance) * 100
            
            cv2.putText(image, f"{idx}", (x1, y1 + 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
    
    # Draw bounding boxes for the filtered objects
    for xmin, ymin, xmax, ymax in filtered_boxes:
        cv2.rectangle(image, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)  # Green bounding box

    # Save the output image
    cv2.imwrite(output_image_path, image)

    return n_vehicle, object_distance_dict

if __name__ == "__main__":
    input_image_path = "sample_data/Screenshot from 2024-11-10 12-17-42.png"
    output_image_path = "output_image.jpeg"
    start_vertical_line = 40  # Percentage (e.g., 30%)
    end_vertical_line = 60    # Percentage (e.g., 70%)
    no_of_vehicles = draw_bounding_boxes_in_range(input_image_path, output_image_path, model_path, start_vertical_line, end_vertical_line)
    print(no_of_vehicles)
