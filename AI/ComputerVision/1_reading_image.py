 # importing opencv library
import cv2

# reading image
img = cv2.imread("sample1.jpg");
# showing image
cv2.imshow("image",img);
# making image to hold for infinite time 
# (if we give some value instead of 0 it will wait for that many milli seconds)
cv2.waitKey(0);
