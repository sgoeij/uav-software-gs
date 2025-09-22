import cv2
import numpy as np

def mask(lower_bound, upper_bound, window_name="img"):
    """returns an image with only a certain color (as determined by bounds)"""
    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)
    masked_img = cv2.bitwise_and(default_img, default_img, mask=mask)
    cv2.imshow(window_name, masked_img)
    return masked_img

# take input and showing the input image
print("Input image path:")
img_path = input()
default_img = cv2.imread(img_path) # which file to read
cv2.imshow("original", default_img)

# convert to hsv
hsv_img = cv2.cvtColor(default_img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv_img)

# categorizing each color, creating masks
w_lower_thresh = np.array([0, 0, 200])
w_upper_thresh = np.array([255, 30, 255])
white_mask = mask(w_lower_thresh, w_upper_thresh, "white extract")

r_lower_thresh = np.array([-15, 30, 0])
r_upper_thresh = np.array([5, 255, 255])
red_mask = mask(r_lower_thresh, r_upper_thresh, "red extract")

y_lower_thresh = np.array([5, 20, 0])
y_upper_thresh = np.array([30, 255, 255])
yellow_mask = mask(y_lower_thresh, y_upper_thresh, "yellow extract")

b_lower_thresh = np.array([90, 25, 0])
b_upper_thresh = np.array([150, 255, 255])
blue_mask = mask(b_lower_thresh, b_upper_thresh, "blue extract")

g_lower_thresh = np.array([30, 25, 0])
g_upper_thresh = np.array([80, 255, 255])
green_mask = mask(g_lower_thresh, g_upper_thresh, "green extract")

cv2.waitKey(0)
cv2.destroyAllWindows()