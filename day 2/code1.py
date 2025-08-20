import cv2
import matplotlib.pyplot as plt
ret,thesh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
img=cv2.imread("img4.jpg")
blur=cv2.blur(img,(5,5))
median = cv2.medianBlur(img,5)
plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
plt.show()
