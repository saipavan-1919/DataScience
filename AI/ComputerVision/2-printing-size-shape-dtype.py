# importing opencv
import cv2

# reading image
img = cv2.imread("DataScience\AI\ComputerVision\sample1.jpg")

print("size = ",img.size);
print("shape of image = ",img.shape);
print("data type of image = ",img.dtype);