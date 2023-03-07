import numpy as np
import cv2

image = cv2.imread("./sample_image/bit_test.jpg", cv2.IMREAD_COLOR)
logo  = cv2.imread("./sample_image/logo.jpg", cv2.IMREAD_COLOR)

if image is None or logo is None:
    raise Exception("영상 파일 읽기 오류 ")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

cv2.imshow('fg_pass_mask', fg_pass_mask)
cv2.imshow('bg_pass_mask', bg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2] # 로고 영상 크기
x, y = (W-w)//2, (H - h)//2
roi = image[y:y+h, x:x+w]                        # 관심 영역(roi) 지정

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask) # 로고의 전경 복사
background = cv2.bitwise_and(roi , roi , mask=bg_pass_mask) # roi에 원본배경만 복사

dst = cv2.add(background, foreground)            # 로고 전경과 원본 배경 간 합성
image[y:y+h, x:x+w] = dst             # 합성 영상을 원본에 복사

cv2.imshow("background", background)
cv2.imshow("forground", foreground)
cv2.imshow("dst", dst)
cv2.imshow("image", image)
cv2.waitKey()
