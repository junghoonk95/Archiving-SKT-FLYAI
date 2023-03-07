import numpy as np
import cv2

# 색상 선언
blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
# 3채널 컬러 영상 생성
image = np.zeros((400, 600, 3), np.uint8)
# 3채널 흰색
image[:] = (255, 255, 255)

cropping = False
refPt = []
title1 = "Mouse Event"

def onMouse(event, x, y, flags, param):
    global refPt, cropping

    if event == cv2.EVENT_LBUTTONDOWN and not cropping:
        refPt = [(x, y)]
        cv2.circle(image, refPt[0], 2, red)
        cv2.imshow(title1, image)
        cropping = True

    elif event == cv2.EVENT_LBUTTONDOWN and cropping:
        refPt.append((x, y))
        cropping = False
        cv2.line(image, refPt[0], refPt[1], blue)
        cv2.rectangle(image, refPt[0], refPt[1], red, 3, cv2.LINE_4)
        cv2.imshow(title1, image)

while True:
    # 영상 보기
    cv2.imshow(title1, image)

    # 마우스 콜백함수
    cv2.setMouseCallback(title1, onMouse)

    if cv2.waitKey() == 27:
        print('ESC')
        break

# 열린 모든 윈도우 제거
cv2.destroyAllWindows()
