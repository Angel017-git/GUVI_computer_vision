import cv2

import matplotlib.pyplot as plt 2

img = cv2.imread("sample.jpg")

# SIFT 4

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

sift = cv2.SIFT_create() 6

 kp, des sift.detectAndCompute (gray, None)

 sift_img = cv2.drawKeypoints (gray, kp, None)


hog = cv2.HOGDescriptor()

hhog.compute(gray)
plt.subplot(1,2,1), plt.imshow(sift_img), plt.title("SIFT Features")
plt.axis("off")
plt.subplot(1,2,2), plt.plot(h[:100])
plt.title("HOG Features (first 100)")