import detect_nearby_vehicle, signal_detection, wheel_angle_prediction

start_vertical_line = 25
end_vertical_line = 75

def get_results(input_image_file_path, output_image_file_path):
    # Predict wheel angle
    detected_angle = wheel_angle_prediction.predict_angle(input_image_file_path)
    
    # Detect signal color
    signal_detected = signal_detection.detect_signal_color(input_image_file_path, output_image_file_path)
    
    # Detect nearby vehicles and draw bounding boxes
    no_of_vehicle_detected, object_distance_dict = detect_nearby_vehicle.draw_bounding_boxes_in_range(output_image_file_path, output_image_file_path, start_vertical_line, end_vertical_line)

    # Return results as a dictionary
    results = {
        "detected_angle": detected_angle,
        "signal_detected": signal_detected,
        "no_of_object_detected": no_of_vehicle_detected,
        "object_distance": object_distance_dict
    }

    return results
