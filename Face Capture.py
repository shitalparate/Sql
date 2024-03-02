# # FAce capture
#
#
# import time
#
# import cv2
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
#
# # Check if the webcam is opened correctly
# if not cap.isOpened():
#     raise IOError("Cannot open webcam")
#
# ret, frame = cap.read()  # Capture a single frame
# if ret:
#     # Display the captured image
#     cv2.imshow('Captured Image', frame)
#
#
#     # Save the captured image to file
#     cv2.imwrite('captured_image.jpg', frame)
#
#     # Wait for a key press
#     cv2.waitKey(0)
#
#
#
# # Release the VideoCapture object
# cap.release()
#
# # Close all OpenCV windows
# cv2.destroyAllWindows()

#=========================================================
import cv2
import time
import os

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

try:
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Failed to grab frame")
            break

        # Get the current time for the filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"captured_image_{timestamp}.jpg"

        # Save the captured image to file
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")

        # Display the captured image
        cv2.imshow('Captured Image', frame)

        # Wait for 5 seconds
        time.sleep(5)

        # Check if the 'q' key was pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    # Handle any manual interruption with Ctrl+C
    print("Interrupted by user")

finally:
    # Release the VideoCapture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
