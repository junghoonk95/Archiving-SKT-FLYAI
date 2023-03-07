import cv2

capture = cv2.VideoCapture(0)                       # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 29.97                                         # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
size  = (640, 360)                                  # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'DX50')            # 압축 코덱 설정

capture.set(cv2.CAP_PROP_ZOOM, 1)                   # 카메라 속성 지정
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH , size[0])     	# 해상도 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])


writer = cv2.VideoWriter("C:/Users/101/opencv/chap04/images/video_file.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

while True:
    ret, frame = capture.read() # 비디오의 한 프레임씩 읽습니다. 제대로 프레임을 읽으면 ret값이 True, 실패하면 False가 나타납니다. frame에 읽은 프레임이 나옵니다
    if not ret or cv2.waitKey(delay) >= 0:
        break
   
    frame = cv2.flip(frame, 1) # y축 기준으로 좌우 뒤집기
    writer.write(frame)
    cv2.imshow('230112_practice_2', frame)

capture.release()