
## 도커 세팅 

> 도커 컨테이너를 이미지로 생성하기
```cmd
docker commit ubuntu_server ubuntu_copy
```
![image](https://user-images.githubusercontent.com/80855939/215626498-928663c8-1e28-41fd-af16-019c24abaf89.png)

> 백업 받은 도커 이미지로 컨테이너 다시 생성하기
```cmd
docker run -d -it -p 80:80 --name webserver ubuntu_copy
```

> 컨테이너 접속 하기
```
docker exec -e LC_ALL=C.UTF-8 -it webserver bash
```

> 한글 설정
```
https://earth-95.tistory.com/160
apt-get install -y locales # locales 설치
locale -a # 현재 사용할 수 있는 locale 확인
apt-get install -y language-pack-ko # 한글 패키지 다운로드
locale-gen ko_KR.utf8 # 템플릿을 사용하여 locale 구성하기
dpkg-reconfigure locales # 한글로 locale 변경하기
vi ~/.bashrc
export LANGUAGE=ko_KR.UTF-8
export LANG=ko_KR.UTF-8
:wq!
```

> 필요한 모듈 다운로드 (도커에서 실행)


```
apt-get install python3
apt-get install python3-pip
pip install streamlit
pip install streamlit-chat
pip install pandas
pip install scikit-learn
pip install sentence-transformers

# sentence-transformers install 시 pytorch도 다운 받아지기 때문에 소요시간 발생
```


## 도커에 파일 업로드

> 데이터 다운로드 from [github](https://github.com/kairess/mental-health-chatbot)
![image](https://user-images.githubusercontent.com/80855939/215672780-ed21ca30-8339-4e35-837a-21dbbfaeabdd.png)

> 로컬 에서 도커로 파일 업로드
```
# 로컬에서
cd C:\Users\028\Downloads
docker cp .\wellness_dataset.csv da8e2fce1ba5:/root
# docker cp c:\경로\로컬파일 도커컨테이너 고유 ID : 리눅스경로

# 도커에서 압축 해
apt-get install unzip
unzip 파일.zip
```

## 도커에서 파일 실행하기

> 도커 접속
```
docker exec -e LC_ALL=C.UTF-8 -it webserver bash

cd <chatbot.py 위치>
streamlit run chatbot.py --server.port 80
```

> 로컬에서 로컬 주소 확인

cmd -> ip config -> IPv4 주소 확인 

![image](https://user-images.githubusercontent.com/80855939/215680557-d183bed1-1cd5-4b9a-9675-1347f2e227b4.png)


인터넷 접속 -> ip 주소 입력 혹은 ip주소 :80 입력






