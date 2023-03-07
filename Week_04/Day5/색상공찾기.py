# load image
import cv2
import numpy as np
ball = cv2.imread("C:/Users/028/Desktop/Huh.png", cv2.IMREAD_COLOR)
ball_hsv = cv2.cvtColor(ball, cv2.COLOR_BGR2HSV)
# ball_hsv=ball_hsv.astype(np.uint16)
ball_hsv = cv2.GaussianBlur(ball_hsv, (0, 0), 1)

def bgr_mask(frame, hsv_frame):

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    lower_red = np.array([0, 0, 200])
    upper_red = np.array([50, 50, 255])
    lower_green = np.array([0, 200, 0])
    upper_green = np.array([50, 255, 50])

    blue_mask = cv2.inRange(frame, lower_blue, upper_blue)
    green_mask = cv2.inRange(frame, lower_green, upper_green)
    red_mask = cv2.inRange(frame, lower_red, upper_red)

    blue_ball = cv2.bitwise_and(frame, frame, mask=blue_mask)
    green_ball = cv2.bitwise_and(frame, frame, mask=green_mask)
    red_ball = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow("blue_ball", blue_ball)
    cv2.imshow("green_ball", green_ball)
    cv2.imshow("red_ball", red_ball)

    cv2.waitKey(0)
    return blue_ball, green_ball, red_ball

def ball_count(img, blue, green, red):
    edges = cv2.Canny(cv2.GaussianBlur(img, (0, 0), 1), 30, 150)

    blue_edges = cv2.Canny(cv2.GaussianBlur(blue, (0, 0), 1), 30, 150)
    green_edges = cv2.Canny(cv2.GaussianBlur(green, (0, 0), 1), 30, 150)
    red_edges = cv2.Canny(cv2.GaussianBlur(red, (0, 0), 1), 30, 150)

    (cnts, _) = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (blue_cnts, _) = cv2.findContours(blue_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (green_cnts, _) = cv2.findContours(green_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (red_cnts, _) = cv2.findContours(red_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # draw edges - drawing on img will over write the original
    result = img.copy()
    cv2.drawContours(result, cnts, -1, (0, 255, 0), 2)

    # 공갯수 출력
    cv2.putText(result, "Blue " + str(len(blue_cnts)) + " balls", (0, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0))
    cv2.putText(result, "Green " + str(len(green_cnts)) + " balls", (0, 140), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))
    cv2.putText(result, "Red " + str(len(red_cnts)) + " balls", (0, 210), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
    print(green_cnts)

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    
    

blue, green, red = bgr_mask(ball, ball_hsv)
ball_count(ball, blue, green, red)
