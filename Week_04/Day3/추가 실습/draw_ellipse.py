
import numpy as np
import cv2

# 색상 지정
orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)
# 3채널 행렬 생성 및 초기화
image = np.full((300, 700, 3), white, np.uint8)

pt1 = (100, 100)
pt2 = (300, 100)
size = (60, 30)
cv2.circle(image, pt1, 1, 0, 2)
cv2.circle(image, pt2, 1, 0, 2)

cv2.ellipse(image, pt1, size, 0, 0, 360, blue, 1)
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1)

cv2.ellipse(image, pt1, size, 0, 30, 270, orange, 2)
cv2.ellipse(image, pt2, size, 90, -45, 90, orange, 2)

while True:
    cv2.imshow('Character Array', image)

    if cv2.waitKey() == 27:
        print('ESC')
        break

cv2.destroyAllWindows()