# Day4. Convolution Neural Network

## 1. 전이학습(Transfer Learning)

- 기존에 사전학습된(pre-trained) 모델을 가져와, 사용하고자 하는 학습 데이터를 학습 시켜 이용하는 방법

- 기존에 비슷한 도메인의 데이터를 학습한 모델이라면 현재 갖고 있는 데이터가 다소 적더라도 좋은 성능 보여줌

- 어떤 목적을 이루기 위해 학습된 모델을 다른 작업에 이용하는 것(모델의 지식을 다른 문제에 이용)

### 전이학습을 사용하는 이유
1. 학습이 빠르게 수행됨
2. 작은 데이터 셋에 대해 학습할 때, 오버피팅 예방 효과가 있음
3. Fine Tuning : 모델을 불러와 동결해 두었떤 전이학습 모델의 가중치를(일부 또는 전부) 학습 가능상태로 만들고 학습

### 전이학습의 사전 학습과 미세 조정
- 사전 학습 : 학습된 모델 만드는 과정
- 미세 조정(fine-tuning) : 사전 학습된 모델 불러와 새로운 문제에 적용하기 위해 새로운 학습 통해 일부 가중치 조절하는 학습 과정

### 전이학습 이외에 모델 성능 개선 방법
- 적합한 Optimizer 적용
- Batch Normalization 추가
- Dropout 적용
- Data 전처리 및 증강
- Fully Connected Layer 은닉층 추가 및 노드 추가
- Learning Decay 적용


---

## 2. 바운딩 박스(Bounding Box)

![img](https://i.loli.net/2017/09/12/59b6d0529299e.png)

- Computer Vision의 Tasks들 중 대표적인 Task들로 **Image Classificiation**, **Object Detection**, **Segmentation** 를 들 수 있음

- 그 중, **Object Detection**에서 사용되는 Bounding Box에 대해 알아보고자 함

### 바운딩 박스(Bounding box)
#### 물체의 위치를 추정(회귀 작업)
- 물체 중심의 수평,수직 좌표와 높이, 너비를 예측
- 모델을 크게 바꿀 필요는 없음
- 바운딩 박스에 널리 사용되는 지표는 IoU(Intersection over Union)
  - 예측한 바운딩 박스와 타겟 바운딩 박스 사이에 중첩된 영역을 전체 영역으로 나눈 것

- 라벨링 지정 도구
 - Label Img
 - Labelme
 - DarkLabel
 + [RobowFlow](https://roboflow.com/) (개인적으로 추천)

---

## 3. 객체 탐지(Object Detection)
### YOLOv5
  - 대표적인 Object Detection 모델
  - 논문으로 publish 안돼있음
  - 이론적인 내용을 알고 싶다면 [YOLOv4 리뷰](https://www.youtube.com/watch?v=6f7jglewoWg&t=312s) 

