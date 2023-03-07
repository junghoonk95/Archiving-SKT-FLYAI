# DNN (심층 신경망)
- 이미지 출처: cs231n 강의 노트, 직접 제작

## 0. Intro
- **데이터 이해도 및 데이터 전처리가** AI 모델링에서 매우 중요함
  - 데이터를 정확하게 이해하지 못하면 모델을 만들어도 사용하기 어려움
  - raw data도 확인해보기
- 하드웨어의 성능도 고려해서 아키텍처 설계를 해야 함
- 네트워크 구조에 따라, 입력 데이터에 따라 아웃풋이 달라짐
- ML에서는 40% 정도를 Data Makeup에 투자


## 1. DNN

### DNN (심층 신경망)

![img1](https://user-images.githubusercontent.com/79077316/211125871-23fc8e09-31fb-4156-99ec-0f825cad242c.png)

- NN은 크게 3개의 층으로 이루어짐
    - `Input layer`
    - `Hidden layer`
    - `Output layer`
- 입력층과 출력층 사이에 여러 개의 은닉층(hidden layer)로 이루어짐
- 이때 DNN은 모든 layer들이 하나도 빠짐없이 다 연결되어 있고, 이를 **Fully connected layer(==Dense layer)**라고 함


### Back-propagation (오차 역전파)

- `Foward-propagation`과는 반대로 출력층 → 입력층 방향으로 계산하면서 가중치를 업데이트

### Loss function (손실 함수)

- 평균 제곱오차(mean squared error:MSE)

![img2](https://user-images.githubusercontent.com/79077316/211125902-0ed4b587-ecda-4a16-84ae-e8bf6cee9dd9.png)

  - y<sub>k</sub>: 예측 값 (신경망 출력)
  - t<sub>k</sub>: 레이블 값
  - 실제 값과 추정 값과의 차이를 나타내며 **회귀** 문제에 사용됨
- 교차 엔트로피 함수(cross entropy error:CEE)

![img3](https://user-images.githubusercontent.com/79077316/211125915-445b696e-7d56-4d17-affc-239e85ac6856.png)


  - 두 분포 간의 차이를 나타내는 척도로서 **분류** 문제에 많이 사용

### Optimizer (최적화 알고리즘)
- Loss function의 값을 최소화하는 가중치를 찾기 위한 알고리즘을 옵티마이저(Optimizer) 또는 최적화 알고리즘이라고 함
- [keras optimizer](https://keras.io/ko/optimizers/)로 SGD, RMSprop, Adam, Adagrad, .. 가 있음
- `SGD` (확률적 경사 하강법)
  - 경사 하강법은 가장 기본적인 최적화 알고리즘
  - 함수의 기울기(미분값)를 구해 기울기가 낮은 쪽으로 계속 이동시켜서 극값에 이를 때까지 반복시키는 방법
- `SGD` + `Momentum`
  - 기본적으로 SGD와 유사하지만, **속도(v)** 개념이 추가됨
  - 즉, 물체가 아무런 힘을 받지 않을 때에도 서서히 하강시키는 역할을 수행함
- `AdaGrad`
  - 신경망 학습에서 중요한 학습률(learning rate)을 서서히 낮추는 방법
  - 개별 매개변수에 적응적으로(Adaptive) 학습률을 조정하면서 학습을 진행함
  - 그러나 `AdaGrad`는 과거의 기울기를 제곱해서 계속 더하기 때문에, 학습을 진행할수록 갱신 강도가 약해져서 무한히 계속 학습할 경우에는 어느 순간 갱신량이 "0"이 되어서 갱신이 이루어지지 않는 단점이 있음
  - 이러한 단점을 개선한 방법이 `RMSProp`
- `RMSProp`
  - 과거의 모든 기울기를 균일하게 더해가는 것이 아니라, 먼 과거의 기울기는 서서히 잊고 새로운 기울기 정보를 크게 반영(지수이동평균)함
- `Adam`
  - `Momentum`과 `AdaGrad` 방법을 결합한 방법임
  - `Adam`은 하이퍼파라미터의 "편향 보정"이 진행됨
  - 하이퍼파라미터를 3개 설정함
    - 학습률(learning rate) = alpha
    - 일차 모멘텀용 계수 beta1 (default 값은 0.9)
    - 이차 모멘텀용 계수 beta2 (default 값은 0.999)


### Activation function (활성화 함수)

![img4](https://user-images.githubusercontent.com/79077316/211125920-105cdd95-2f17-49fc-baa9-8c633f2c01c5.png)

- 뉴럴 네트워크에서는 노드에 들어오는 값들에 대해 곧바로 다음 레이어로 전달하지 않고 활성화 함수(Activation Function)를 통과시킨 후에 전달
- 언더피팅의 문제를 개선
- 활성화 함수는 특정 feature에 대해 이 정보를 얼마나 활성화할 것인지를 결정하는 역할
- 활성화 함수로 비선형 함수를 사용 -> non-linearity 제공

![img5](https://user-images.githubusercontent.com/79077316/211125928-36ceb397-350f-402a-8d42-3cdb416246c3.png)
![img6](https://user-images.githubusercontent.com/79077316/211125933-4ab1a774-0503-40c0-897d-eb3e362460bc.png)

### Vanishing gradient (경사도 소실)

- 여러 은닉 계층으로 구성되어 있는 신경망에서는 활성화 함수에 따라 경사도 소실 문제가 발생할 수 있음
  - 특히 시그모이드의 경우 x가 증가함에 따라 기울기가 0에 가까워지므로 신경망이 깊어질수록 경사도 소실이 커짐
  - 따라서 시그모이드는 사용한다면 보통 출력층에서 사용
- DNN에서는 경사도 소실 문제를 극복하는 함수로 ReLU 활성화 함수를 사용

### DNN 구현

- Dense module
    - neural network를 구성하는 layer를 생성할 때 사용
    - `model.add(Dense(1, input_dim=5, activation='relu')`
    - 출력 노드의 수, 입력 노드의 수, 활성화 함수     
- Dropout
    - 일부의 노드를 의도적으로 생략하여 학습을 진행
    - 오버피팅 방지

### DNN 구현 단계
1. 데이터 준비
    - 데이터 불러오기
    - 데이터 시각화
2. 데이터 전처리
    - 결측치 확인 및 처리
    - 이상치 확인 및 처리
3. 피쳐 추출하기
4. 데이터 정규화
5. train/val/test 데이터셋 분리
    - feature와 label 분리
6. 모델 구현
    - 모델 만들기
    - 모델 컴파일
7. 모델 학습 및 결과 시각화
8. 모델 예측 및 결과 시각화

## 이진분류

- 규칙에 따라 입력된 값을 **두 그룹으로 분류하는 작업**

**활성화 함수(Activation Function)**

- output에 non linear한 성질을 추가하기 위함
- Sigmoid function
    $Sigmoid(x) = \frac{1}{1+e^{-x}}$

**Loss**

- Binary cross entroy loss
    - MSE의 loss 변화가 심한 단점 보완
    - 로그를 사용하기에 불일치율 높을수록 높은 loss 반환

$BCE = - \frac{1}{n} \sum_{i=1}^{n} ( Y_{i} \cdot log (\hat{Y_{i}}) + (1 - Y_{i}) \cdot log (1 - \hat{Y_{i}}))$

정규화

- Normalization
    - 값의 범위(scale)를 0~1 사이의 값으로 변환
    - 학습 전에 scaling
        - 머신러닝에서 scale이 큰 feature의 영향이 커지는 것을 방지
        - 딥러닝에서 Local Minima에 빠질 위험 감소(학습 속도 향상)
    - ${x-x_{min} \over x_{max}-x_{min}}$
- Standardization(표준화)
    - 값의 범위(scale)를 평균 0, 분산 1이 되도록 변환
    - 학습 전에 scaling
        - 머신러닝에서 scale이 큰 feature의 영향이 커지는 것을 방지
        - 딥러닝에서 Local Minima에 빠질 위험 감소(학습 속도 향상)
    - 정규분포를 표준정규분포로 변환하는 것과 동일
        - 1 ~ 1 사이에 68%가 있고, -2 ~ 2 사이에 95%가 있고, -3 ~ 3 사이에 99%가 있음
        - 3 ~ 3의 범위를 벗어나면 outlier 가능성 높음
    - $\frac {x-\mu} {\sigma} \space \space \space (\mu:평균, \sigma: 표준편차)$
- Regularization
    - weight를 조정하는데 규제
    - Overfitting을 막기위해
    - L1 regularization, L2 regularizaion 등의 종류가 있음
        - L1: LASSO(라쏘)
        - L2: Lidge(릿지)
    - $Loss = \frac {1} {n} \sum_{i=1}^{n} \{ (y -\hat{y})^2 + \frac {\lambda} {2} |w|^2 \}$

## 다중분류
- 클래스의 정보가 3개 이상인 경우, 여러개의 답 중 하나를 고르는 분류 문제

OHE

- 문자열 포함시 숫자로 바꾸는 작업 필요
- 특정 숫자 부여시 숫자의 크기에 의미 부여 가능성 존재
- 이를 해결하기 위해 사용

**Softmax Function**

- 합계가 1이도록 만들어준다
- 큰 값은 더 두드러지게 작은 값은 더 작게
- $p_j = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_j}}$

Loss

- categorical cross entropy loss
    - 원핫 벡터일 때
- sparse categorical cross entropy loss
    - 정수일 때
- $CE = -\sum_{c=1}^{C}L_{c}logP_{c}$
