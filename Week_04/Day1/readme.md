### 인공 신경망

- 퍼셉트론

### 활성화 함수

- 회귀 → linear
- 이진 분류 → 시그모이드
- 다중 분류 → 소프트맥스

### 손실함수

- 회귀 → 평균제곱오차(MSE)
- 이진분류 → binary cross entropy
- 다중 분류 → categorical cross entropy

출력과 실제 값의 차이를 최소화하는 weight와 bias를 찾는다

### 옵티마이저

- gradient descent를 통해 미분이 0이 되는 global maxima 찾기
    - local minima에 빠지지 않도록 유의
- loss를 최소화하는 방향으로 갱
- ex: SGD, RMSProp, Adagrad, Adam
- epoch 증가시 overfitting 문제 고려 필요

### 다층 신경(Multi Layer Perceptron)

- consisted of **input, hidden, and output layer**
- unit(input → activaiton func → output)
