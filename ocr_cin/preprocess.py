import cv2
from matplotlib import pyplot as plt

# opening the image
image_file = "temp/resized_identity_card.jpg"
img = cv2.imread(image_file)

# display the image
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()

#invert the image 
inverted_image = cv2.bitwise_not(img)
cv2.imwrite("temp/inverted.jpg", inverted_image)

# convert image to GrayScale
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(inverted_image)
cv2.imwrite("temp/gray.jpg", gray_image)

# Apply binary thresholding to the grayscale image
#thresh, im_bw = cv2.threshold(gray_image,110, 255, cv2.THRESH_BINARY )

    # apply thresholding

border_size = 60
min_brightness = gray_image[border_size:-border_size, border_size:-border_size].mean()
    
threshold_value = min_brightness + 52
print(threshold_value)
    
    # Apply inverse binary thresholding
_, bw_im = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imwrite("temp/bw_image.jpg", bw_im)

display("temp/bw_image.jpg")

#noise removal
def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=3)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=10)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 1)
    return (image)

no_noise = noise_removal(bw_im)
cv2.imwrite("temp/no_noise.jpg", no_noise)

display("temp/no_noise.jpg")