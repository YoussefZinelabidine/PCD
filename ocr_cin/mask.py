import cv2
import numpy as np

image = cv2.imread('temp/no_noise.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform Gaussian smoothing
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Create a binary mask with the edges
mask = np.zeros_like(gray)
mask1 = np.zeros_like(gray)
# Draw the regions you want to keep visible on the mask using white color
cv2.rectangle(mask1, (250, 145), (430, 190), (255, 255, 255), -1)

masked_image1 = cv2.bitwise_and(image,image, mask=mask1)

cv2.imwrite('masked_image1.jpg', masked_image1)


cv2.rectangle(mask, (250, 210), (557, 250), (255, 255, 255), -1)
cv2.rectangle(mask, (250, 250), (560, 290), (255, 255, 255), -1)
cv2.rectangle(mask, (250, 288), (625, 320), (255, 255, 255), -1)
cv2.rectangle(mask, (250, 320), (515, 365), (255, 255, 255), -1)
cv2.rectangle(mask, (250, 365), (570, 410), (255, 255, 255), -1)

masked_image = cv2.bitwise_and(image,image, mask=mask)

cv2.imwrite('masked_image.jpg', masked_image)
