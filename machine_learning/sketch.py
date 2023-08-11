# This code is made by MRayan Asim
# Packages needed:
# pip install opencv-python
import cv2


def sketch_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply a Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Blend the grayscale image and the blurred image using the "color dodge" blend mode
    sketch = cv2.divide(gray_image, blurred_image, scale=256.0)

    return sketch


# Provide the path to your input image
input_image_path = "image.jpg"

# Generate the sketch
sketch = sketch_image(input_image_path)

# Display the original image and the sketch
cv2.imshow("Original Image", cv2.imread(input_image_path))
cv2.imshow("Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
