import cv2

capture = cv2.VideoCapture(0)		# 0번 카메라에 연결
if not capture.isOpened():
    raise Exception("카메라 연결 안됨")		# 예외 처리

fps = 30 # 초당 프레임 수
delay = round(1000/ fps) # 프레임 간 지연 시간
size = (640, 480) # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 압축 코덱 설정

# capture.set(cv2.CAP_PROP_ZOOM, 1)                   # 카메라 속성 지정
# capture.set(cv2.CAP_PROP_FOCUS, 0)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH , size[0])     	# 해상도 설정
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])



while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0: break
    x, y, w, h = (200, 100, 100, 200)
    cv2.rectangle(frame, (x,y,w,h), (0, 0, 255), 3) # (0, 0, 225):Green, 두께 3
	
    blue, green, red = cv2.split(frame)             				# 컬러 영상 채널 분리
    tmp = green[y:y+h, x:x+w]
    cv2.add(tmp, 50, tmp) # green 채널 밝기 증가
    frame = cv2.merge( [blue, green, red] )                 # 단일채널 영상 합성
    cv2.imshow("연습1", frame)

capture.release()