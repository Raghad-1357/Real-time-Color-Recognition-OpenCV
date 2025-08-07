import cv2
import numpy as np

# A list of colors and their HSV ranges
# These ranges are approximate and may need tuning based on lighting conditions
colors_hsv = {
    # Colors defined primarily by Hue
    "Red": ([0, 100, 100], [10, 255, 255]),
    "Orange": ([10, 100, 20], [25, 255, 255]),
    "Yellow": ([25, 100, 100], [35, 255, 255]),
    "Green": ([36, 100, 100], [86, 255, 255]),
    "Blue": ([94, 80, 2], [126, 255, 255]),
    "Purple": ([130, 100, 100], [150, 255, 255]),
    "Pink": ([160, 100, 100], [179, 255, 255]),
    # Colors defined by Saturation and Value
    "White": ([0, 0, 200], [179, 30, 255]),  
    "Black": ([0, 0, 0], [179, 255, 30]),  
    "Grey": ([0, 0, 50], [179, 50, 200]),   
    "Brown": ([10, 100, 50], [20, 255, 150]),
}

def get_color_name(hsv_color):
    """
    Returns the name of a color based on its HSV value.
    """
    for color_name, (lower, upper) in colors_hsv.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # Check if the HSV color is within the defined range
        if np.all(lower <= hsv_color) and np.all(hsv_color <= upper):
            return color_name

    return "Unknown"

# Start video capture from webcam (0 is for the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("Webcam opened successfully. Press 'q' to quit.")

while cap.isOpened():
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    # If a frame was not captured, break the loop
    if not ret:
        break

    # Convert the BGR image to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the height and width of the frame
    height, width, _ = frame.shape
    
    # Calculate the center of the frame
    center_x = int(width / 2)
    center_y = int(height / 2)
    
    # Get the HSV color of the center pixel
    center_hsv_color = hsv_frame[center_y, center_x]

    # Draw a circle at the center for visualization
    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

    # Get the name of the color at the center
    color_name = get_color_name(center_hsv_color)

    # Display the color name on the frame
    cv2.putText(frame, "Color: " + color_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Real-time Color Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()