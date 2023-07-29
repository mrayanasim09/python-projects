# This code is made by MRayan Asim
# Packages needed:
# pip install opencv-python
# pip install numpy
import cv2

ip_address = input("Enter the ip address: ")
port = input("Enter the port number: ")
# Replace this with the IP address and port number from the camera app
camera_url = f"http://{ip_address}:{port}/video"

# Create VideoCapture object to read from the camera stream
cap = cv2.VideoCapture(camera_url)

while True:
    # Read frame-by-frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Perform image processing or display the frame
    # Example: Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame
    cv2.imshow("Camera Feed", gray_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
