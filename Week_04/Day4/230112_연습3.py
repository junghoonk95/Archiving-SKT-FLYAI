# bitwise 연산으로 특정 영역 따로 표시

import numpy as np
import cv2

image = cv2.imread('C:/Users/101/opencv/chap05/images/color.jpg', cv2.IMREAD_COLOR)

if image is None:
    raise Exception('영상 파일 읽기 오류')

mask = np.zeros(image.shape[:2], np.uint8)
center = (190, 170)

cv2.ellipse(mask, center, (50, 80), 0, 0, 360, 255, -1) # 내부 채움: -1
dst = cv2.bitwise_and(image, image, mask = mask) # Point: 논리곱

cv2.imshow('original', image)
cv2.imshow('bitwise_and', dst)
cv2.waitKey()

print(image)

