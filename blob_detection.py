import numpy as np
import cv2
from matplotlib import pyplot as plt

def draw_keypoints_on_image(keypoints, image):
    for kp in keypoints:
        x, y = int(kp.pt[0]), int(kp.pt[1])  # center
        r = int(kp.size / 2)  # radius
        cv2.circle(image, (x, y), r, (0, 255, 0), thickness=3)
    return image

FILE_1 = "images/polka_dots_1.png"
og_image = cv2.imread(FILE_1)
rgb_img = cv2.cvtColor(og_image, cv2.COLOR_BGR2RGB)

para = cv2.SimpleBlobDetector_Params()

para.minThreshold = 10   
para.maxThreshold = 250  
para.thresholdStep = 10
para.filterByArea = False
para.filterByCircularity = True
para.minCircularity = 0.7
para.filterByConvexity = False
para.filterByInertia = False
para.filterByColor = True
para.blobColor = 0

detector = cv2.SimpleBlobDetector_create(para)
keypoints = detector.detect(rgb_img)

output = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)

output = draw_keypoints_on_image(keypoints, output)

plt.imshow(output)
plt.axis("off")
plt.show()