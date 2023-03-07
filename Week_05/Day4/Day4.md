# 클라우드 컴퓨팅

- 클라우드 서비스 유형
    - On-premise
    - IaaS `eg) 차를 구매하기`
    - PaaS `eg) 차를 렌트하기`
    - SaaS `eg) 택시 타기`

# 인터넷은 어떻게 작동될까요?

[Youtube : 인터넷은 어떻게 작동될까요?](https://youtu.be/o5yBl59wRbY)

- 데이터센터에 저장된 영상을 우리가 인터넷으로 보기위해서
    1. 위성을 사용하는 방식
        - 데이터센터 → 위성 → 우리 주변의 안테나 → 우리
        - 다만 장거리 이동으로 신호 수신에 지연이 생긴다.
    2. 광섬유 네트워크를 사용하는 방식
        - 데이터센터에 저장된 콘텐츠를 광섬유 케이블로 전송한다.
        - (1) 광섬유 케이블은 우리 주변의 라우터까지 연결되어, 라우터가 광섬유 케이블을 통해 도착한 빛신호를 전기신호로 변경한다.그리고 이더넷 케이블을 통해 전기신호를 기기에 전송한다.
        - (2) 만약 셀룰러를 사용중이라면, 광섬유 케이블의 빛신호는 기지국으로 도착하고, 기지국은 전자파형태로 우리 기기에 데이터를 전송한다.

# 인터넷은 어떤 원리로 운영되고 있는걸까?

[Youtube : 인터넷은 어떤 원리로 운영되고 있는걸까?](https://youtu.be/Pwf-YG--Zsg)

![image](https://user-images.githubusercontent.com/67251510/213512235-bdb6c590-001c-4d77-804e-36ccca7c6d47.png)

- 이더넷들과 연결된 라우터가 하나씩 존재.
- 라우터들끼리 연결되어있으며, 외부통신이 이루어지려면 해당 라우터를 꼭 거쳐야함 → Inter-networks(internet)
- 라우터는 패킷을 전송단위로하며, 패킷의 도착 IP주소를 확인하고 가까운 이웃에게 패킷을 전달하는 작업을 함.
- 망중립성 : 인터넷에서 패킷을 전달함에 차별이 없어야함.

# 네트워크

- 패킷
    - 정보 기술에서 패킷 방식의 컴퓨터 네트워크가 전달하는 데이터의 형식화된 블록
- IP주소
    - 인터넷에 연결된 기기를 고유하게 식별하는 번호.
    - IP, Internet Protocol : 네트워크상에서 패킷을 교환하기 위해 사용하는 규약.
- DNS(Domain Name System)
    - 우리가 IP주소를 알지못해도 도메인을 통해 사이트에 접속할 수 있게함.
        - 도메인(www.naver.com)을 IP주소(192. …)로 매핑해준다
    - hierarchy 구조를 가지고 있어, 클라이언트가 재귀적으로 각 층에 요청, 응답을 받는다.
    
    ![image](https://user-images.githubusercontent.com/67251510/213511906-5f9d011d-3032-425b-bf6c-7e5eda54ca05.png)
    
- 라우터
    - 컴퓨팅 디바이스와 네트워크를 다른 네트워크에 연결하는 네트워킹 디바이스
    - 해당 라우터를 설치해주는 망사업자, ISP(Internet Service Provider)가 존재한다.
        - KT, SKT, LGU+
    - ISP(인터넷 서비스 공급자)가 사용자의 IP 주소를 부여한다.
- 서브넷
    - 라우팅(라우터 통신)없이 데이터 passing이 가능한 집합
    
    ![image](https://user-images.githubusercontent.com/67251510/213511816-fdd66155-51e1-495b-8173-24a85c485fb6.png)
    
    - 위 그림 파란 영역 하나하나가 서브넷을 뜻함.
    - subnet mask 표기법
    - CIDR(prefix) 표기법

# Microsoft azure

### 실습 : 가상머신 만들기
![image](https://user-images.githubusercontent.com/67251510/213591063-cdc2c7b5-cfc4-40cc-8b17-d3ae8990cbce.png)
* 기본사항
    - 가상머신 이름, 관리자 계정 설정, 인스턴스 설정 등을 할 수 있다.
* 디스크
    - 가상머신의 디스크 크기 등을 설정할 수 있다.
* 네트워킹
    - 인바운드 포트, 가상 네트워크 연결 등을 할 수 있다.
* 관리
* Monitoring
* 고급
* 태그


## Load Balancer

![image](https://user-images.githubusercontent.com/67251510/213511642-fdca1539-6893-4339-bc6f-98a0ca5cef25.png)

- 부하 분산 장치
- 가상 머신 확장 집합(VMSS)
