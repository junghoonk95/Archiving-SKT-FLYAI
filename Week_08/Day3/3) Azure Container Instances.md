※ 참고링크
- https://learn.microsoft.com/ko-kr/azure/container-instances/container-instances-tutorial-prepare-app
- https://learn.microsoft.com/ko-kr/cli/azure/install-azure-cli

# 1. 컨테이너 이미지 만들기 
### Windows에 Azure CLI 설치후 AZ 로그인

[윈도우 Azure CLI 다운로드](https://aka.ms/installazurecliwindows)
>설치확인
```
az
```
![image](https://user-images.githubusercontent.com/80855939/217418461-663a7540-f7ee-4336-8d61-6ebeaabfa6ae.png)


>AZ 로그인
```
az login
```
![image](https://user-images.githubusercontent.com/80855939/217413691-e86e29ba-84e8-4e10-be00-68d08b641ba4.png)


### 실습에 사용할 간단한 웹앱 다운
git clone https://github.com/Azure-Samples/aci-helloworld.git
* 다운 받은 폴더에서 진행, 도커가 실행 되어있는 상태여야함
* 
> 컨테이너 이미지를 만들고 aci-tutorial-app으로 태깅
```
docker build ./aci-helloworld -t aci-tutorial-app
```
![image](https://user-images.githubusercontent.com/80855939/217412905-ccd63fc3-2a2d-4c39-b1c8-22d33628dfed.png)

> docker images

![image](https://user-images.githubusercontent.com/80855939/217417945-ac7baeb0-8744-4466-9646-3d1d30911b2e.png)
![image](https://user-images.githubusercontent.com/80855939/217417995-b385d3d6-9e1b-482c-8368-cfbad571a4a8.png)



### 컨테이너 로컬에서 실행 확인
```
docker run -d -p 8080:80 aci-tutorial-app
```

![image](https://user-images.githubusercontent.com/80855939/217424738-26c4139c-bb88-47c4-94c4-63de3d345b58.png)

# 2. Azure 컨테이너 레지스트리

### Azure 컨테이너 레지스트리 생성

```
az group create --name myResourceGroup --location eastus
```
![image](https://user-images.githubusercontent.com/80855939/217433577-c09dbca2-bd20-4b7f-a6cc-f96a1cec296d.png)


```
# name에 고유이름 컨테이너 레지스트리 생성
az acr create --resource-group myResourceGroup --name mycontainer32 --sku Basic
```
![image](https://user-images.githubusercontent.com/80855939/217433606-52c136e5-e983-430f-b250-8baeda87f12a.png)

> 컨테이너 레지스트리에 로그인

```
az acr login --name mycontainer32
```

![image](https://user-images.githubusercontent.com/80855939/217451497-840b579f-fd80-44b1-9bea-12af5294874a.png)


> 컨테이너 이미지 태그 지정

```
az acr show --name mycontainer32 --query loginServer --output table
```

![image](https://user-images.githubusercontent.com/80855939/217451635-cdc436cd-7770-4930-a248-9df0d8f112a5.png)


> Azure Container Registry에 이미지 푸시하기

```
docker push <acrLoginServer>/aci-tutorial-app:v1
```

![image](https://user-images.githubusercontent.com/80855939/217451948-baf4b947-721a-4148-9903-8f8034982052.png)

> Azure Container Registry에서 이미지 나열

``` 
az acr repository list --name mycontainerregistry082 --output table
```
![image](https://user-images.githubusercontent.com/80855939/217452444-3660f83a-7014-4a1b-9fea-1542dcc547e4.png)

# 3. 애플리케이션 배포

###  Azure Container Instances에 컨테이너 애플리케이션 배포

> Azure 컨테이너 레지스트리에서 Id, PW 확인

![image](https://user-images.githubusercontent.com/80855939/217452974-fc912173-f9a6-4ed4-8066-d4b9a67ff94c.png)


```
az container create --resource-group myResourceGroup --name aci-tutorial-app --image <acrLoginServer>/aci-tutorial-app:v1 --cpu 1 --memory 1 --registry-login-server <acrLoginServer> --registry-username <service-principal-ID> --registry-password <service-principal-password> --ip-address Public --dns-name-label <aciDnsLabel> --ports 80
```
> 개인 ID/PW 적용
```
az container create --resource-group myResourceGroup --name aci-tutorial-app --image mycontainer32.azurecr.io/aci-tutorial-app:v1 --cpu 1 --memory 1 --registry-login-server mycontainer32.azurecr.io --registry-username mycontainer32 --registry-password uvad9wIYJkdVKhz9pK7Xi2lGLSPZlsuKb8Rb+HMqVE+ACRDeDwIl --ip-address Public --dns-name-label aci32 --ports 80
```
![image](https://user-images.githubusercontent.com/80855939/217453194-a00de4e7-ff2d-4a66-ab65-44c1cd845745.png)

> 애플리케이션 및 컨테이너 로그 보기
```
az container show --resource-group myResourceGroup --name aci-tutorial-app --query ipAddress.fqdn
```
![image](https://user-images.githubusercontent.com/80855939/217453361-02b7e230-31cd-4ca8-a58b-46ddbe16588c.png)

> 생성된 주소로 접속 확인
aci-demo.eastus.azurecontainer.io

![image](https://user-images.githubusercontent.com/80855939/217453650-b7d3c57f-9958-4ff2-9799-1a96f0744375.png)


