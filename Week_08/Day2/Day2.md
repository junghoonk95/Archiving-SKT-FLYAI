| 컨테이너 | 가상머신 |
| --- | --- |
| 프로세스 가상화 | OS 가상화 |

## python 경로 확인

```bash
which python3.9
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 3
sudo update-alternatives --config python
```

## minikube 설치

```bash
curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube --help #설치확인
```

## kubectl 설치

- kubectl : 쿠버네티스 API 호출을 위한 `command-line tool`

```bash
curl -LO https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl --help
```

## 드라이버를 docker 로 설정

```bash
minikube start --driver=docker
minikube status #확인
```

- 오류 : Docker is nearly out of disk space, …
    
    ![image](https://user-images.githubusercontent.com/67251510/217166326-a5931672-0e36-4cc2-8201-09c44e270929.png)
    
    ```bash
    kubectl get pod -n kube-system
    
    minikube delete
    minikube start --driver=docker
    ```
    

## Pod

- Pod : 쿠버네티스에서 `가장 작은` 단위
- `1개 이상의 컨테이너가 캡슐화` 되어 클러스터 안에서 배포
    - 대부분 하나의 Pod는 하나의 컨테이너가 구성되어 있음 (→ 한 Pod를 컨테이너로 생각해도 됨)
- 외부에서 연결하기 위해 포트포워딩이 필요함(pod는 `외부 노출 x`)
- `언제든지 삭제될 수 있다'는 가정 하에 만들어진 개념


```bash
kubectl run nginx --image nginx --port=8080
kubectl get pod # nginx running 을 확인 가능
docker images
docker ps -a # gcr.io/k8s-minikube/... 확인
```

### 포트포워딩 (추후 다시 진행)

```bash
kubectl port-forward nginx 18080:8080
```

## YAML
- 쿠버네티스는 명령어(대부분 작업은 kubectl 명령어로 실행)로도 사용할 수 있지만, YAML 파일을 더 많이 사용함.
[Transform YAML into JSON - Online YAML Tools](https://onlineyamltools.com/convert-yaml-to-json)
- 컨테이너뿐만 아니라 `거의 모든 리소스 오브젝트들`에서 사용 가능.
    - 컨테이너의 설정값(ConfigMap), 비밀값(Secrets)

- `---` : 구분선. 여러개의 Yaml document 작성 가능.

```bash
$ vi pod.yaml
```

```yaml
apiVersion: v1 # kubernetes resource의 API Version
kind: Pod # kubernetes resource name
metadata: # 메타데이터 : name, namespace, labels, annotations 등을 포함
  name: counter
spec: # 메인 파트 : resource 의 desired state 를 명시
  containers:
  - name: count # container 의 이름
    image: busybox # container 의 image
    args: [/bin/sh, -c, 'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done'] # 해당 image 의 entrypoint 의 args 로 입력하고 싶은 부분
```

```bash
$ kubectl apply -f pod.yaml # 쿠버네티스 생성
$ kubectl get pod # kubectl get <오브젝트 이름>: 특정 오브젝트의 목록을 확인
$ kubectl describe pod counter # kubectl describe pod <pod 이름>: pod의 정보를 출력
$ kubectl get pod -o wide # pod 목록을 자세히 출력
```
- kubectl apply -f <yaml-file-path> 를 수행하면, <yaml-file-path> 에 해당하는 kubernetes resource를 생성 또는 변경함
    
### 로그 확인

```bash
kubectl logs <pod-name> {-f} # -f 옵션 : 로그를 계속 보여줌
kubectl logs <pod-name> -c <container-name> {-f}
```
### Pod 삭제
- kubectl delete pod <pod-name>
    - kubectl delete -f <YAML-파일-경로>: YAML 파일을 이용한 삭제

### 용량 늘리기
- [참고 링크1](https://www.nucleiotechnologies.com/increasing-disk-space-on-file-system-root-ubuntu-20-04)
- [참고 링크2](https://hiseon.me/linux/ubuntu/modify-partition-size)
- Hyper-V로 디스크 용량 늘려주고 
-`sudo apt-get update && sudo apt-get install gparted` 설치 후 파티션 조정

## Deployment
- Deployment(디플로이먼트)는 Pod와 Replicaset에 대한 관리를 제공하는 단위
    - Deployment 는 Pod을 감싼 개념
    -Pod을 Deployment로 배포함으로써 여러 개로 복제된 Pod, 여러 버전의 Pod을 안전하게 관리할 수 있음
``` 
apiVersion: apps/v1 # kubernetes resource 의 API Version
kind: Deployment # kubernetes resource name
metadata: # 메타데이터 : name, namespace, labels, annotations 등을 포함
  name: nginx-deployment
  labels:
    app: nginx
spec: # 메인 파트 : resource 의 desired state 를 명시
  replicas: 3 # 동일한 template 의 pod 을 3 개 복제본으로 생성
  selector:
    matchLabels:
      app: nginx
  template: # Pod 의 template
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx # container 의 이름
        image: nginx:1.14.2 # container 의 image
        ports:
        - containerPort: 80 # container 의 내부 Port
```
### Deployment Auto-healing
- kubectl delete pod <pod-name> 실행
- 위의 명령어가 실행됨에도 불구하고, 기존 pod 이 삭제되고 `동일한 pod 이 새로 하나 생성`됨(AGE으로 확인할 수 있음)

### Deployment Scaling
- kubectl scale deployment/nginx-deployment --replicas=<변경하고자 하는 replica의 갯수>

``` 
apiVersion: apps/v1 # kubernetes resource 의 API Version
kind: Deployment # kubernetes resource name
metadata: # 메타데이터 : name, namespace, labels, annotations 등을 포함
  name: nginx-deployment
  labels:
    app: nginx
spec: # 메인 파트 : resource 의 desired state 를 명시
  replicas: 3 # 동일한 template 의 pod 을 3개 복제본으로 생성
  selector:
    matchLabels:
      app: nginx
  template: # Pod 의 template
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx # container 의 이름
        image: nginx:1.14.2 # container 의 image
        ports:
        - containerPort: 80 # container 의 내부 Port
```
    
## Service
- 쿠버네티스에 배포한 애플리케이션(Pod)을 외부에서 접근하기 쉽게 추상화한 리소스
- Pod는 언제든지 삭제될 수 있기 때문에 고정된 IP로 원하는 Pod에 접근하기에는 어려움이 있음 → 클러스터의 내/외부에서 접근할 Pod의 IP가 아 Service를 통해 접근함
    - Service는 고정된 IP 를 가지며, Service는 하나 혹은 여러 개의 Pod과 매칭
    - 클라이언트가 Service의 주소로 접근하면, Service에 매칭된 Pod에 접속됨
- Type
    - ClusterIP: 클러스터 내부에서만 접근 가능
    - NodePort: 클러스터 외부 노출
    - LoadBalncer: 클러스터 외부에서 접근이 가능하지만 LoadBalancing 역할을 하는 모듈이 필요함
    
``` 
vi service.yaml
# 파일을 열어 위의 내용을 복사 붙여넣기 합니다.
kubectl apply -f service.yaml
kubectl get service
# PORT 80:<PORT> 숫자 확인
curl -X GET $(minikube ip):<PORT>
# 이렇게 서비스를 통해서 클러스터 외부에서도 정상적으로 pod 에 접속할 수 있는 것을 확인합니다. $(minikube ip) 시스템에 정의 되어 있음 
```

## PVC
- Persistent Volume(PV), Persistent Volume Claim(PVC)는 stateless한 Pod를 영구적으로(persistent) 데이터를 보존하고 싶은 경우 사용하는 리소스
    - PV: 관리자가 생성한 실제 저장 공간의 정보를 담고 있음
    - PVC: 용자가 요청한 저장 공간의 스펙에 대한 정보를 담고 있음
        - 보존하고 싶은 데이터가 있다면 `Pod에 PVC를 mount해서 사용`해야 함
