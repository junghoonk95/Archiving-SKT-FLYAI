## Hyper-V로 우분투 가상 머신 만들기

- `Hyper-V 관리자`에서 `Ubuntu 20.04 LTS` 가상 컴퓨터 설치하기
- 로그인하고 가상 컴퓨터에 접속하면 다음과 같은 화면이 나옴

![image](https://user-images.githubusercontent.com/79077316/216868235-697a4d67-763e-41cc-ba21-3d2eaeaf3b5c.png)

## [비교 실습] ****[Azure Portal에서 Virtual Machine Scale Set 만들기](https://learn.microsoft.com/ko-kr/azure/virtual-machine-scale-sets/quick-create-portal)****

- Azure Portal에서 Load Balancer 만들기
- Virtual Machine Scale Set 만들기

![image](https://user-images.githubusercontent.com/79077316/216868353-ef122afb-aae0-48fd-82e2-d10f7346a35b.png)

![image](https://user-images.githubusercontent.com/79077316/216868374-e2d4d5ad-651c-4383-82a2-f850fb74c378.png)

## `Hyper-V` 우분투 가상 컴퓨터 실습

- 우분투 터미널에서 다음 코드 실행

```powershell
sudo passwd # 새로운 비밀번호 설정 !Seoul2023
sudo apt-get update # 패키지 업데이트
sudo apt-get install vim
```

![image](https://user-images.githubusercontent.com/79077316/216868393-f01aa8f1-bc9c-43e9-a071-4979a41297c3.png)
- vim
    - [설명서](https://www.joinc.co.kr/w/Site/Vim/Documents/UsedVim)
    - command line 기반 vi 텍스트 편집 에디터
    - i랑 :wq만 기억해도 웬만한 것은 다 된다.

- [우분투 고급 세션 모드 설정하기](https://lucidmaj7.tistory.com/343)
```powershell
sudo apt-get update

sudo apt-get install --yes git

git clone https://github.com/Hinara/linux-vm-tools.git

cd linux-vm-tools/ubuntu/20.04

chmod +x ./install.sh
sudo ./install.sh

sudo reboot

sudo ./install.sh

Set-VM -VMName '[VM이름]' -EnhancedSessionTransportType HvSocket
```
    - 윈도우 Hyper-V로 우분투에 접속하면 마우스랑 키보드 입력이 느려지는 문제를 해결하기 위해 `고급 세션 모드(enhanced session mode)`가 추가됨
    - 고급 세션 모드는 내부적으로 RDP를 이용해서 VM에 접속하는 방식
    - `ctrl+v`가 된다

## Docker

### 1) 컨테이너

- 컨테이너(Container)는 개별 Software의 실행에 필요한 **실행환경을 독립적으로 운용할 수 있도록** 기반환경 또는 다른 실행환경과의 간섭을 막고 **실행의 독립성을 확보해주는 운영체제 수준의 격리 기술**
- 컨테이너는 애플리케이션을 실제 구동 환경으로부터 추상화할 수 있는 논리 패키징 메커니즘을 제공

### 2) 컨테이너 `vs` 가상머신

- 컨테이너와 가상머신 모두 독립적인 실행 환경을 구성할 수 있도록 하는데 둘의 차이는 다음과 같다

![image](https://user-images.githubusercontent.com/79077316/216879183-ab045632-8dae-4c18-9f77-daf0dc2183ea.png)

- 컨테이너
    - 하나의 Host OS 위에서 마치 각각의 독립적인 프로그램처럼 관리되고 실행됨 (하나의 프로세스)
    - 불필요한 OS 만드는 작업 및 Infra를 독립적으로 나눌 필요가 없어서 확장성이 좋고 속도가 빠름
- 가상머신
    - HyperVisor가 있음. 컴퓨터가 가지고 있는 리소스들을 VM 별로 분배하는 역할
    - 각 VM에서는 독립적인 Guest OS를 가지고 있음
    - 독립적인 플랫폼을 하나씩 늘릴 때마다 불필요한 OS를 만드는 작업을 반복함 → 확장성이 떨어지고, 리소스 효율성 측면에서도 비효율적임
    
### 3) 도커

- 도커는 **컨테이너 기반**의 오픈소스 가상화 플랫폼
- 도커는 리눅스 컨테이너를 실행하고 관리하는 엔진
- Docker를 이용해서 인프라에서 애플리케이션을 분리하여 **컨테이너로 추상화시킴**
- 하나의 호스트 OS안에서 여러 컨테이너를 동시에 실행할 수 있음
- 도커는 컨테이너의 라이프 사이클을 관리하고 어플리케이션을 **오케스트레이션**(Work flow의 자동화된 서비스)으로 배포할 수 있음
- wsl2는 내부에 있는 리눅스 커널 
```powershell
docker run -d -p 80:80 docker/getting-started
```
- 외부 포트와 내부 포트를 지정해서 들어갈 수 있다
```powershell
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo usermod -a -G docker $USER
$ sudo service docker restart

docker run --name demo3 -d busybox sh -c "while true; do $(echo date); sleep 1; done"
```
기타 명령어
from 

- base image로 어떤 것을 사용할지 명시

run

- 실행할 명령어

cmd

- 바로 실행시키고 싶은 것

WORKDIR

- 기본 디렉

ENV

- 환경변수

EXPOSE

- 포트 지정

dockerfile을 이용해 환경 설정, 라이브러리 지정, 명령 실행 등 자동화 역시 가능
