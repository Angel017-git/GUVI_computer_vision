import cv2
img=cv2.imread("zoom img.jpg")
cv2.imwrite("compressed_image_30.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),30])
cv2.imwrite("compressed_image_50.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),90])