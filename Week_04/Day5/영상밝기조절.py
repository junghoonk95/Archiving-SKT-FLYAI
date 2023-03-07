import cv2

cap = cv2.VideoCapture('C:/Users/028/Desktop/plz.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    frame_yuv[:,:,0] = cv2.equalizeHist(frame_yuv[:,:,0])
    frame_output = cv2.cvtColor(frame_yuv, cv2.COLOR_YUV2BGR)
  # equalizeHist를 사용해서 자동으로 변환
    cv2.imshow("original", frame)
    cv2.imshow("equalized", frame_output)

    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
