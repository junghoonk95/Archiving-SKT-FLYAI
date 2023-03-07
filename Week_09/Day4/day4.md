# TORCH.AUTOGRAD를 사용한 자동 미

[torch.autograd를 사용한 자동 미분](https://tutorials.pytorch.kr/beginner/basics/autogradqs_tutorial.html)

- 역전파에서 매개변수(모델 가중치)는 주어진 매개변수에 대한 손실 함수의 변화도(gradient)에 따라 조정
- 이러한 변화도를 계산하기 위해 pyTorch에는 torch.autograd라고 불리는 자동 미분 엔진 내장. 이는 모든 계산 그래프에 대한 변화도의 자동 계산 지원
- 입력 x, 매개변수 w와 b, 그리고 일부 손실 함수가 있는 가장 간단한 단일 계층 신경망을 가정

```python
import torch

x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w)+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)
```

- Tensor, Function과 연산그래프(Computational graph)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/713fdb87-4ca5-442e-8769-2ea0946cb1b2/Untitled.png)

- 이 신경망에서, w와 b는 최적화를 해야 하는 매개변수이다.
- 이러한 변수들에 대한 손실 함수의 변화도를 계산할 수 있어야 한다

이를 위해 해당 텐서에  `requires_grad` 속성을 설정

- 연산 그래프를 구성하기 위해 텐서에 적용하는 함수는 Function 클래스의 객체
- 이 객체는 순전파 방향으로 함수를 계산하는 방법과, 역전파 단계에서 도함수**(derivative)**를 계산하는 방법
- 역전파 함수에 대한 참조는 텐서의 grad_fn 속성에 저장

```python
Gradient function for z = <AddBackward0 object at 0x7ff3df4e6280> # 메모리주
Gradient function for loss = <BinaryCrossEntropyWithLogitsBackward0 object at 0x7ff36616c940>
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63d79a53-4564-49d8-b06f-55fc3ad569e3/Untitled.png)

## 변화도(Gradient) 계산하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee362ee2-7870-4fb5-829e-db9a0baff2a9/Untitled.png)

```python
loss.backward()
print(w.grad)
print(b.grad)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/56e5f5d3-9789-4ade-81b0-0ecc2d509ed7/Untitled.png)

- 연산 그래프의 잎(leaf) 노드들 중 `requires_grad` 속성이 `True`로 설정된 노드들의 `grad` 속성만 구할 수 있습니다. 그래프의 다른 모든 노드에서는 변화도가 유효하지 않습니다.
- 성능 상의 이유로, 주어진 그래프에서의 `backward`를 사용한 변화도 계산은 한 번만 수행할 수 있습니다. 만약 동일한 그래프에서 여러번의 `backward` 호출이 필요하면, `backward` 호출 시에 `retrain_graph=True`를 전달해야 합니다.

## 변화도 추적 멈추기

- 기본적으로, requires_grad=True인 모든 텐서들은 연산 기록을 추적하고 변화도 계산을 지원
- 그러나 순전파 연산만 필요한 경우에는, 이러한 추적이나 지원이 필요 없을 수 있다. 이런 경우에는 연산 코드를 torch.no_grad() 블록으로 둘러싸서 연산 추적 중단. 이를 통해 순전파 단계만 수행할 때 연산 속도가 향상

```python
z = torch.matmul(x, w)+b
print(z.requires_grad)

with torch.no_grad():
    z = torch.matmul(x, w)+b
print(z.requires_grad)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7e079ac2-5c36-4966-bcc8-78a1cd105c74/Untitled.png)

- 변화도 추적을 하는 것은 느리다
- 테스트 코드에서는 필요 없음
- with torch.no_grad(): 이 코드 밑에는 gradient 계산 안함
- 다른 방법은 텐서에 detach() 메소드 사용

```python
z = torch.matmul(x, w)+b
z_det = z.detach()
print(z_det.requires_grad)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c225de5-c9a5-4b91-9478-3494823efed9/Untitled.png)

- 변화도 추적을 멈춰야 하는 이유
    - 신경망의 일부 매개변수를 고정된 매개변수(frozen parameter)로 표시합니다. 이는 사전 학습된 신경망을 미세조정 할 때 매우 일반적인 시나리오입니다.
    - 변화도를 추적하지 않는 텐서의 연산이 더 효율적이기 때문에, 순전파 단계만 수행할 때 연산 속도가 향상됩니다.

## 연산 그래프에 대한 추가 정보

- 개념적으로, autograd는 데이터(텐서)의 및 실행된 모든 연산들(및 연산 결과가 새로운 텐서인 경우도 포함하여)의 기록을 Function 객체로 구성된 방향성 비순환 그래프(DAG; Directed Acyclic Graph)에 저장(keep)합니다.
- 이 방향성 비순환 그래프(DAG)의 잎(leave)은 입력 텐서이고, 뿌리(root)는 결과 텐서이다.
- 이 그래프를 뿌리에서부터 잎까지 추적하면 연쇄 법칙(chain rule)에 따라 변화도를 자동 계산 가능
- 순전파 단계에서, autograd는 다음 두 가지 작업을 동시에 수행합니다:
    - 요청된 연산을 수행하여 결과 텐서를 계산하고,
    - DAG에 연산의 변화도 기능(gradient function) 를 유지(maintain)
- 역전파 단계는 DAG 뿌리(root)에서 `.backward()` 가 호출될 때 시작됩니다. `autograd`는 이 때:
    - 각 `.grad_fn` 으로부터 변화도를 계산하고,
    - 각 텐서의 `.grad` 속성에 계산 결과를 쌓고(accumulate),
    - 연쇄 법칙을 사용하여, 모든 잎(leaf) 텐서들까지 전파(propagate)
    

> PyTorch에서 DAG들은 동적(dynamic)입니다. 주목해야 할 중요한 점은 그래프가 처음부터(from scratch) 다시 생성된다는 것입니다; 매번 `.bachward()` 가 호출되고 나면, autograd는 새로운 그래프를 채우기(populate) 시작합니다. 이러한 점 덕분에 모델에서 흐름 제어(control flow) 구문들을 사용할 수 있게 되는 것입니다; 매번 반복(iteration)할 때마다 필요하면 모양(shape)이나 크기(size), 연산(operation)을 바꿀 수 있습니다.
> 

# Optimizing Model Params

[모델 매개변수 최적화하기](https://tutorials.pytorch.kr/beginner/basics/optimization_tutorial.html)

## 하이퍼파라미터(Hyperparameter)

- 하이퍼파라미터 : 모델 최적화 과정을 제어할 수 있는 조절 가능한 매개변수
- 서로 다른 하이퍼파라미터 값은 모델 학습과 수렴율(convergence rate)에 영향을 미칠 수 있다.
- 학습 시에는 다음과 같은 하이퍼파라미터를 정의:
    - 에폭(epoch)수 : 데이터 셋을 반복하는 횟수
    - 배치 크기(batch size) : 매개변수가 갱신되기 전 신경망을 통해 전파된 데이터의 샘플 수
    - 학습률(learning rate) : 각 배치/에폭에서 모델의 매개변수를 조절하는 비율. 값이 작을수록 학습 속도가 느려지고, 값이 크면 학습 중 예측할 수 없는 동작 가능
    
    ```python
    learning_rate = 1e-3
    batch_size =64
    epochs = 5
    ```
    

## 최적화 단계(Optimization Loop)

- 하이퍼파라미터를 설정한 뒤에는 최적화 단계를 통해 모델을 학습하고 최적화
- 하나의 에폭은 다음 두 부분으로 구성
    - 학습 단계(train loop) : 학습용 데이터 셋을 반복하고 최적의 매개변수로 수렴
    - 검증/테스트 단계(validation/test loop) : 모델 성능이 개선되고 있는지를 확인하기 위해 테스트 데이터 셋을 반복

## 손실 함수(Loss Function)

- 손실 함수는 획득한 결과와 실제 값 사이의 틀린 정도(degree of dissimilarity)를 측정하며, 학습 중에 이 값을 최소화
- 주어진 데이터 샘플을 입력으로 계산한 예측과 정답(label)을 비교하여 손실(loss)을 계산
- 일반적인 손실함수에는 회귀 문제(regressio task)에 사용하는 nn.MSELoss(평균 제곱 오차:Mean Square Error)나 분류(classification)에 사용하는 nn.NLLLoss(음의 로그 우도;Negative Log Likelihood), 그리고 nn.LogSoftmax와  nn.NLLLoss를 합친 nn.CrossEntropyLoss 등이 있다.
- 여기서는 모델의 출력 로짓(logit)을 nn.CrossEntropyLoss에 전달하여 logit을 정규화하고 예측 오류를 계산

```python
# 손실 함수를 초기화
loss_fn = nn.CrossEntropyLoss()
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1294087-8616-4371-be8d-df68315fe450/Untitled.png)

## 옵티마이저(Optimizer)

- 최적화 : 각 학습 단계에서 모델의 오류를 줄이기 위해 모델 매개변수를 조정하는 과정
- 여기서는 SGD(확률적 경사하강법;Stochastic Gradient Descent) 옵티마이저 사용
- 학습하려는 모델의 매개변수와 학습률 하이퍼파라미터를 등록하여 옵디마이저를 초기화

```python
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
```

- 학습 단계에서 최적화 단계:
    - optimizer.zero_grad()를 호출하여 모델 매개변수의 변화도를 재설정. 기본적으로 변화도는 더해지기 때문에 중복 계산을 막기 위해 반복할 때마다 명시적으로 0으로 설정
    - loss.backward()를 호출하여 예측 손실(prediction loss)을 역전파.
    - 변화도를 계산한 뒤에는 optimizer.step()을 호출하여 역전파 단계에서 수집된 변화도로 매개변수를 조정
- 전체 구현 - Train Loop

```python
def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
```

```python
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

epochs = 10
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")
```

Out

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f995f88-d19e-466f-9b88-73c8c507fcdc/Untitled.png)

# Save and Load the Model

[모델 저장하고 불러오기](https://tutorials.pytorch.kr/beginner/basics/saveloadrun_tutorial.html)

```python
import torch
import torchvision.models as models
```

## 모델 가중치 저장하고 불러오기

- PyTorch 모델은 학습한 매개변수를  state_dict라고 불리는 내부 상태 사전(internal state dictionary)에 저장. 이 상태 값들은 [`t](http://torch.save)orch.save` 메소드를 저장할 수 있다.

```python
model = models.vgg16(pretrained=True)
torch.save(model.state_dict(), 'model_weights.pth')
```

- 모델 가중치를 불러오기 위해서는, 먼저 동일한 모델의 인스턴스를 생성한 다음에 메소드를 사용하여 매개변수들을 불러온다.

```python
model = models.vgg16(pretrained=True)
torch.save(model.state_dict(), 'model_weights.pth')
```

## 모델의 형태를 포함하여 저장하고 불러오기

- 모델의 가중치를 불러올 때, 신경망의 구조를 정의하기 위해 모델 클래스를 먼저 생성해야 했다. 이 클래스의 구조를 모델과 함께 저장하고 싶으면 model.state_dict()가 아닌 model을 저장 함수에 전달

```python
torch.save(model, 'model.pth')
```

- 다음과 같이 모델을 불러온다

```python
model = torch.load('model.pth')
```

# Training a Classifier

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7995944-530f-4efb-a23a-41afff2a9eb4/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b7100ef-9b35-4e2b-9f64-99bcb34318ed/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/956b2995-cfc2-4e76-b62b-d96ddbe28ad1/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6531695a-caa4-481d-897c-9ff2f3a774c3/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7424093e-9977-4101-a89f-d90737d9f9b2/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a672efa0-4bf3-4c90-a752-e96ac532e153/Untitled.png)

- 손실함수로 CrossEntropyloss 사용

```python
loss_fn = torch.nn.CrossEntropyLoss()
```

- Optimizer

```python
# Optimizers specified in the torch.optim package
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
```

- The Training Loop

```python
def train_one_epoch(epoch_index, tb_writer):
  running_loss = 0.
  last_loss = 0.

  for i, data in enumerate(training_loader):
    inputs, labels = data

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = loss_fn(outputs, labels)
    loss.backward()

    optimizer.step()

    running_loss += loss.item()
    if i % 1000 == 999:
      last_loss = running_loss / 1000
      print(' batch {} loss: {}'.format(i + 1, last_loss))
      tb_x = epoch_index * len(training_loader) + i + 1
      tb_writer.add_scalar('Loss/train', last_loss, tb_x)
      running_loss = 0.
    
  return last_loss
```

- Per-Epoch Activity(Training)

```python
from datetime import datetime
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
writer = SummaryWriter('runs/fashion_trainer_{}'.format(timestamp))
epoch_number = 0

EPOCHS = 5

best_vloss = 1_000_000.

for epoch in range(EPOCHS):
  print('EPOCH {}:'.format(epoch_number + 1))

  model.train(True)
  avg_loss = train_one_epoch(epoch_number, writer)

  model.train(False)

  running_vloss = 0.0
  for i, vdata in enumerate(validation_loader):
    vinputs, vlabels = vdata
    voutputs = model(vinputs)
    vloss = loss_fn(voutputs, vlabels)
    running_vloss += vloss

  avg_vloss = running_vloss / (i + 1)
  print('LOSS train {} valid {}'.format(avg_loss, avg_vloss))

  writer.add_scalars('Training vs. Validation Loss',
                     {'Training': avg_loss, 'Validation': avg_vloss},
                     epoch_number + 1)
  writer.flush()

  if avg_vloss < best_vloss:
    best_vloss = avg_vloss
    model_path = 'model_{}_{}'.format(timestamp, epoch_number)
    torch.save(model.state_dict(), model_path)

  epoch_number += 1
```

- Tensorboard

```python
%load_ext tensorboard
%tensorboard --logdir=runs
```

- (N+2P-F)/S + 1

# 실습(GarmentClassifier 바꿔보기)

[Google Colaboratory](https://colab.research.google.com/drive/1OUgm4zM732VKWRd0Z34x6k-PbI8Dun59?usp=sharing)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7556e750-6745-4a1d-aeb6-8524144591a3/Untitled.png)

# Transfer_learning

[Transfer_learning.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b85b87e1-860e-4730-8a8a-6fcc97fc26ba/Transfer_learning.pdf)

## 데이터 구축은 고비용(시간 + 돈)!

- 이미 구축된 데이터를 활용하여 특징을 학습한 후 활용
- 예 : 이미지넷(120만 개의 이미지에 대하여 학습)을 활용하여 특징 학습 후에 적은 규모의 데이터 셋(e.g. FashionMNIST)에 적용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d891746-a857-43a1-9127-4c45b6adadbc/Untitled.png)

- 주로 세 가지 전략 사용
    - ConvNet as fixed feature extractor : 마지막 FC 레이어만 학습
    - Fine-tuning the ConvNet : 전체 네트워크를 재학습(소규모 데이터로)
    - Pretrained models : 다른 연구자가 공개한 사전학습 모델 활용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7a126d1-d1b6-4d27-8db2-1d452b53ad9a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a215d3f7-4271-4ec7-9cd5-41e49238ffcb/Untitled.png)

## 개미 / 벌 분류 실습

[컴퓨터 비전(Vision)을 위한 전이학습(Transfer Learning)](https://tutorials.pytorch.kr/beginner/transfer_learning_tutorial)

[Google Colaboratory](https://colab.research.google.com/drive/19HbKkEVTnLDya4c3xC8TQybzgnRdNczg?usp=sharing)

1. Training 및 Test 데이터 셋을 불러오고 정규화 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cb1168e-a2b8-43fd-a63d-088e7f62d4c2/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6dc0b73-4219-462a-bc61-36fd07165a6a/Untitled.png)

- Normalize는 RGB 값의 평균과 분산값 사용
- 위에 숫자는 ImageNet의 평균과 분산값

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8660bc91-f952-40f6-9528-4138e148c9a2/Untitled.png)

- 보통 validation set 에서는 shuffle을 False로 True도 가능

- 일부 이미지 시각화

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de43b848-a2aa-4621-a4f8-affc28d3c2dc/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5824d518-4b0b-4b9a-9790-b53f5259b73e/Untitled.png)

1. 모델 정의하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16a33c83-646b-43d1-8ad1-e195b731304a/Untitled.png)

- requires_grad : 자동미분
    - False라면 FC 레이어에만 학습 적용
- in_features는 들어오는 차원수를 나타내줌
- fc는 모델 마다 이름, 값이 다르기 때문에 각각의 모델에서 확인 필요

3. 손실함수와  Optimizer 정의

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f998a561-0ca7-4084-956f-5f237ea379f0/Untitled.png)

1. Training set을 사용하여 신경망 학습

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59f0c01b-7b72-4f54-b467-f29eab7f2960/Untitled.png)

- 모델을 저장하는 방법
    - 100번마다 저장하는 방법
        - 되돌아가기 쉽지만 저장용량 많이 차지
    - 성능이 이전 모델보다 좋아졌을 때 저장하는 방법
- 학습 시에만 연산기록을 추적할 때
    - requires = True인 것만 추적

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65188414-16af-44df-a813-6add7d781a5e/Untitled.png)

1. Test set을 사용하여 신경망이 잘 훈련했는지 검사

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f65a886d-cd04-4a5b-85e6-435cef85c2c9/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d975d767-2deb-4c23-acd7-2f278bb47a80/Untitled.png)

# CNN

[CNN Practice.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15632812-6a4f-459d-8a62-cd55be034aad/CNN_Practice.pdf)

# Batch Normalization

[배치 정규화(Batch Normalization)](https://gaussian37.github.io/dl-concept-batchnorm/)

- Normalization 하는 이유 :
    - 데이터가 크다면 전량을 조사할 수 없다
    - 사용하는 데이터가 nomal distribution을 뽑을 수 없을 만큼 작다면 사용하는 것이 batch nomalizatino이다
- 아웃라이어가 학습을 방해하기 때문에 batch nomalization
- batch 단위로 하기 때문에 Batch Normalization
- Internal Covariant Shift
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1c8fb00-a6ae-48e0-a610-37aae6065ff2/Untitled.png)
    
    - `Batch` 단위로 학습을 하게 되면 발생하는 문제점이 있는데 이것이 **Internal Covariant Shift** 이다.
    - 먼저 Internal Covariant Shift 의미를 알아보면 위 그림과 같이 **학습 과정에서 계층 별로 입력의 데이터 분포가 달라지는 현상**을 말한다.
    - 각 계층에서 입력으로 feature를 받게 되고 그 feature는 convolution이나 위와 같이 fully connected 연산을 거친 뒤 activation function을 적용
    - 그러면 **연산 전/후에 데이터 간 분포가 달라질 수**가 있습니다.
    - 이와 유사하게 Batch 단위로 학습을 하게 되면 **Batch 단위간에 데이터 분포의 차이**가 발생할 수 있음
    - 즉, **Batch 간의 데이터가 상이**하다고 말할 수 있는데 위에서 말한 `Internal Covariant Shift` 문제
    - 이 문제를 개선하기 위한 개념이 **Batch Normalization** 개념이 적용

## Batch Normalization

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f502ea20-40c0-472a-988d-0036158fde24/Untitled.png)

- batch normalization은 학습 과정에서 각 배치 단위 별로 데이터가 다양한 분포를 가지더라도 **각 배치별로 평균과 분산을 이용해 정규화**하는 것.
- 위 그림을 보면 batch 단위나 layer에 따라서 입력 값의 분포가 모두 다르지만 정규화를 통하여 분포를 zero mean gaussian 형태로 만든다.
- 그러면 평균은 0, 표준 편차는 1로 데이터의 분포를 조정할 수 있음.
- 여기서 중요한 것은 Batch Normalization은 학습 단계와 추론 단계에서 조금 다르게 적용되어야 한다.

# Object Detection and Image Segmentation

[lecture_9_jiajun.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b23b2162-78e9-4bbd-82ae-69c7e46b9e31/lecture_9_jiajun.pdf)

- 이미지 맵이 줄어드는 이유
    - 연산량을 줄이기 위해
- 줄여가는 것 > Donwsample, Subsampling
- 키워가는 것 > Upsampling

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3504440c-9629-4c2b-8141-eb3138769ce7/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f1aca0dd-b6a7-439f-b490-725c4cc5a1d5/Untitled.png)

- maxpooling 시의 위치를 기억
- 그 위치에 unpooling

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31dc3118-6590-40eb-b546-c2a9a932ff2c/Untitled.png)

- Obeject 할 객체의 개수를 모르는 문제 발생
    - 이것을 알기 위한 방법
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/959d3e7e-6edf-470b-9cd4-b07bb0944526/Untitled.png)
    
    - 색이 바뀌는 지점에 바운딩 박스
    - 바운딩 박스 후보를 줄일 수 있음

# R-CNN

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bdaa7e0-1738-4176-a7df-191227a466cb/Untitled.png)

1. Hypothesize Bounding Boxes (Proposals)
    - Image로부터 Object가 존재할 적절한 위치에 Bounding Box Proposal (Selective Search)
    - 2000개의 Proposal이 생성됨.
2. Resampling pixels / features for each boxes
    - 모든 Proposal을 Crop 후 동일한 크기로 만듦 (224*224*3)
3. Classifier / Bounding Box Regressor
    - 위의 영상을 Classifier와 Bounding Box Regressor로 처리
- 하지만 모든 Proposal에 대해 CNN을 거쳐야 하므로 연산량이 매우 많은 단점이 존재

# Fast R-CNN

- R-CNN 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/930a4c8d-acdc-4c3d-8a96-b0944ccb723a/Untitled.png)

- Fast R-CNN 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8d19ad50-8eba-489f-8fd9-1dadc06e9402/Untitled.png)

- Fast R-CNN은 모든 Proposal이 네트워크를 거쳐야 하는 R-CNN의 병목(bottleneck)구조의 단점을 개선하고자 제안 된 방식
- 가장 큰 차이점은, 각 Proposal들이 CNN을 거치는것이 아니라 전체 이미지에 대해 CNN을 한번 거친 후 출력 된 특징 맵(Feature map)단에서 객체 탐지를 수행
- R-CNN
    - Extract image regions
    - 1 CNN per region(2000 CNNs)
    - Classify region-based features
    - Complexity: ~224 x 224 x 2000
- Fast R-CNN
    - 1 CNN on the entire image
    - Extract features from feature map regions
    - Classify region-based features
    - Complexity: ~600 x 1000 x 1
    - ~160x faster than R-CNN
- 하지만 Fast R-CNN에서 Region Proposal을 CNN Network가 아닌 Selective search 외부 알고리즘으로 수행하여 병목현상 발생

# Faster R-CNN

- R-CNN 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04c136f8-4bb8-4b75-aedb-cf35497e6792/Untitled.png)

• Region Proposal을 RPN이라는 네트워크를 이용하여 수행(병목현상 해소)

- Faster R-CNN 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f2d0ed9-c63e-44a3-bfc8-7fa2da876cfe/Untitled.png)

- Region Proposal 단계에서의 bottleneck 현상 제거
    - 해당 단계를 기존의 Selective search 가 아닌 CNN(RPN)으로 해결
- CNN을 통과한 Feature map에서 슬라이딩 윈도우를 이용해 각 지점(anchor)마다 가능한 바운딩 박스의 좌표와 그 점수를 계산
- 2:1, 1:1, 1:2의 종횡비(Aspect ratio)로 객체를 탐색

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/551bb0ca-c6aa-4060-81f7-0279b0beb9a6/Untitled.png)

# YOLO

## You Only Look Once

[You Only Look Once. YOLO](https://blog.nerdfactory.ai/2021/05/06/You-Only-Look-Once.-YOLO.html)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f6017e4a-ccef-429c-b48d-87cc23a82fca/Untitled.png)

- 큰 박스와 작은 박스의 차이를 줄이기 위해
    - 루트 사용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d0bf0b80-1b91-4d49-a988-d61d6c193b8e/Untitled.png)

- YOLO는 localization 많이 틀림
- 그리드 형식을 사용하고
- 1-Stage이기 때문

# 실습(객체 검출 미세조정(Finetuning))

[TorchVision 객체 검출 미세조정(Finetuning) 튜토리얼](https://tutorials.pytorch.kr/intermediate/torchvision_tutorial.html)

[Google Colaboratory](https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/torchvision_finetuning_instance_segmentation.ipynb)

# 실습

[Google Colaboratory](https://colab.research.google.com/drive/1xO5_8cDHpJ0KamE-42xV7_qccZaUaK_J?usp=sharing)

[Object Dectction Practice.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/572401d5-35ef-4739-9d75-49c4ae432dea/Object_Dectction_Practice.pdf)
