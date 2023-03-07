참고 페이지 https://learn.microsoft.com/ko-kr/azure/aks/learn/quick-kubernetes-deploy-portal?tabs=azure-cli
# AKS를 활용하여 앱 배포하기

## [AKS.md](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/blob/main/Week_08/Day3/AKS.md) 참고하여 노드가 5개인 AKS를 만듭니다

<img src = "https://user-images.githubusercontent.com/80855939/217405760-6445b948-fcb4-4383-9db9-c0158af5f9ed.png" width="70%" height="70%">

> 본인 리소스에 생긴 myAKSCluster에 접속 후 연결 및 노드 확인

![image](https://user-images.githubusercontent.com/80855939/217407205-c4d00e68-ffa6-4d60-9814-c2666cdfc13c.png)

> 애플리케이션 배포를 위한 yaml 파일 생성

```code
# azure-vote.yaml 파일 생성
vi azure-vote.yaml
```

```code
# yaml 파일 

apiVersion: apps/v1
kind: Deployment
metadata:
  name: azure-vote-back
spec:
  replicas: 1
  selector:
    matchLabels:
      app: azure-vote-back
  template:
    metadata:
      labels:
        app: azure-vote-back
    spec:
      nodeSelector:
        "kubernetes.io/os": linux
      containers:
      - name: azure-vote-back
        image: mcr.microsoft.com/oss/bitnami/redis:6.0.8
        env:
        - name: ALLOW_EMPTY_PASSWORD
          value: "yes"
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 250m
            memory: 256Mi
        ports:
        - containerPort: 6379
          name: redis
---
apiVersion: v1
kind: Service
metadata:
  name: azure-vote-back
spec:
  ports:
  - port: 6379
  selector:
    app: azure-vote-back
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: azure-vote-front
spec:
  replicas: 1
  selector:
    matchLabels:
      app: azure-vote-front
  template:
    metadata:
      labels:
        app: azure-vote-front
    spec:
      nodeSelector:
        "kubernetes.io/os": linux
      containers:
      - name: azure-vote-front
        image: mcr.microsoft.com/azuredocs/azure-vote-front:v1
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 250m
            memory: 256Mi
        ports:
        - containerPort: 80
        env:
        - name: REDIS
          value: "azure-vote-back"
---
apiVersion: v1
kind: Service
metadata:
  name: azure-vote-front
spec:
  type: LoadBalancer
  ports:
  - port: 80
  selector:
    app: azure-vote-front
```

```code
# 작성한 yaml 파일 적용
kubectl apply -f azure-vote.yaml
```
> 성공적인 출력 메시지 

```
deployment "azure-vote-back" created
service "azure-vote-back" created
deployment "azure-vote-front" created
service "azure-vote-front" created
```
![image](https://user-images.githubusercontent.com/80855939/217408079-b6b25e70-3eb9-433f-8d36-437cf51bfa15.png)


> 애플리케이션 테스트
```
kubectl get service azure-vote-front --watch
```
### Pending이 사라지고  EXTERNAL-IP 가 생성됨을 확인
![image](https://user-images.githubusercontent.com/80855939/217408331-cef25482-6b43-49ed-8f45-76d75a238773.png)

>  EXTERNAL-IP 접속하여 정상적으로 앱 배포  확인
![image](https://user-images.githubusercontent.com/80855939/217406815-b60a0334-e53a-4693-b8c8-d53ff7c58991.png)
