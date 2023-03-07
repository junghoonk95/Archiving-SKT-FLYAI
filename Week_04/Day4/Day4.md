# 4.4 영상파일 처리
## 4.4.1 영상파일 읽기
```
(실습) read_image1.py, read_image2.py
```
- `cv2.IMREAD_UNCHANGED` : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다.
- `cv2.imread(title2, (color2unchanged2 * 255).astype(’uint8’))` : (`color2unchanged2` : float32) 정수형 변환 후 표시

* 동영상 : 연속성을 가지므로, 프레임간의 차이가 없을 때 첫번째 프레임의 퀄리티를 높게 저장하고 나머지 프레임은 차분을 내어 표현해 적은 비용으로 높은 퀄리티를 보일 수 있음
    - decoding : 복원. 화면을 보여줌.
- stepSize : ex) 범위1 : 0\~10/10\~20/20\~30/30\~40/40\~50, 범위2 : 0\~20/20\~40/40\~60. 범위1보다 범위2가 stepSize가 크다.
- Region of Interest (ROI), 관심영역
- `grab` : 메모리상으로 불러옴


- `split`, `merge` : 채널 분리, 채널 합치기


# 4.6 Matplotlib 패키지 활용

- interpolation 들.
    - Linear, Cubic, Bilinear, Bicubic …
    
# 5.2 채널 처리 함수
- RGB 채널을 나누어서, 흰색으로 보이는 곳 -> intensity 값이 높음을 알 수 있음.
```
- 빨간 사과를 추적하고 싶을 때, red 채널에 intensity 가 가장 높은 것을 탐지해내어, 마킹해 계속 추적하여 탐지할 수 있기도 함.
```

- mask : 특정한 지역에 1이라고 적용된것만 연산.
- 더하기, `add`
    - saturation 연산 : opencv (max값을 넘어가지않음)
    - modulo 연산 : Numpy (max를 넘어서, 다시 min값부터.)
- `addWeighted(src1, alpha, src2, beta, gamma)`
    - alpha 는 src1 에, beta 는 src2 에, gamma 는 최종값에 가중치를 더함.

