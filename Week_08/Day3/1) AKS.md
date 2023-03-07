# Azure Kubernetes Service (AKS)

## 노드가 1개인 기본 AKS 만들기 

<img src = "https://user-images.githubusercontent.com/80855939/217396856-c7204544-e380-423d-b8e6-288d555b33ff.png" width="70%" height="70%">
<img src = "https://user-images.githubusercontent.com/80855939/217398190-ed162939-c646-430c-b815-243dedd161cb.png" width="70%" height="70%">
<img src = "https://user-images.githubusercontent.com/80855939/217397643-46a10d66-6725-462e-94db-ab3394c1e488.png" width="70%" height="70%">

> 기존 리소스 에는 "aksTest32", 신규 리소스에는 내부 AKS 요소 확인

<img src = "https://user-images.githubusercontent.com/80855939/217398430-5cceaa81-85df-4742-981e-8b433a3eb281.png" width="70%" height="80%">
<img src = "https://user-images.githubusercontent.com/80855939/217404275-73378a16-27ea-4aa4-98ad-24c1a903ab83.png" width="50%" height="50%">

## 생성한 노드에 pod 추가하기
<img src = "https://user-images.githubusercontent.com/80855939/217406077-be6facfa-39a0-4a5d-b0f2-8df1f545525c.png" width="100%" height="100%">


> 노드 확인
```code
kubectl get node
```
![image](https://user-images.githubusercontent.com/80855939/217401864-3021d577-23c0-433d-a4e0-b810c45a2800.png)

> 노드에 pod 생성

```code

vi svc.yaml
# svc.yaml 파일 작성

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80 #내부 80
---
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  type: LoadBalancer
  ports:
  - port: 80 # 외부에서 80 
    protocol: TCP
  selector:
    app: nginx

# 작성 완료후 적용
kubectl apply -f svc.yaml

# 생성 확인
kubectl get pod
```
![image](https://user-images.githubusercontent.com/80855939/217402140-c81044c2-d173-47c6-93af-428b13dfbb62.png)

> 서비스 상태 확인    

```code
kubectl get svc
```
![image](https://user-images.githubusercontent.com/80855939/217402528-ca351197-de04-4250-a6b4-5663e390e7f5.png)

> 외부 ip 입력후 사이트 접속확인
![image](https://user-images.githubusercontent.com/80855939/217401315-5e8dfae2-e244-480d-9f96-fd27bf9cc20a.png)



