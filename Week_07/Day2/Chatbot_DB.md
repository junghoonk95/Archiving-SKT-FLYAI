# Chatbot 프로그램에 DB 연동
>연동하여 chatbot의 실시간 수집데이터를 DB 서버에 보낼 예정


> 필요한 도커 컨테이너 2개: webserver , Mysql(chatbot-db)

## DB 컨테이너 : Mysql-container (chatbot-db)

### 기존 DB가 없는경우  (과거 실습때 사용한 flyai DB)


> 외부에서 도커 이미지 받아오기 https://hub.docker.com/r/apptools/chatbot-webserver

혹은

```
도커 이미지 받아오기
docker pull apptools/chatbot-db:1.0

도커 이미지 조회
docker images

도커 이미지 실행 - 생성하기
docker run -d -i -it --name chatbot-db -p 3306:3306 apptools/chatbot-db:1.0

도커 컨테이너 조회
docker ps

도커 컨테이너 안으로 들어가기
docker exec -e LC_ALL=C.UTF-8 -it chatbot-db /bin/bash

MySQL 접속하기
mysql -u root -p
password : apptools

```
> 접속이 안될시 password 확인, 도커에 들어가서 해당 콘테이너,이미지 지워보고 다시 실행
* DB를 다운 받아오는 경우 하기 실습때 파일명, 폴더명, 컨테이너명 유의

### 데이터 생성

```
데이터베이스 생성
create database flyai;

데이터베이스 선택
use flyai;

테이블 생성
create table chatbot(
num int not null auto_increment,
type varchar(4),
msg varchar(200),
indate varchar(50),
primary key(num)
);

테이블 구조보기
desc chatbot();

테이블 데이터 조회하기
select * from chatbot;
```

### 챗 봇 메시지 저장
```
챗봇 메시지 샘플 저장해보기
insert into chatbot set
type = 'bot',
msg = '안녕하세요! 저는 귀염둥이 챗봇 입니다.',
indate = now();
select * from chatbot;
```

## Chatbot 컨테이너

> 앞서 "도커세팅"에서 만든 webserver 사용

```
도커 컨테이너 안으로 들어가기
docker exec -e LC_ALL=C.UTF-8 -it webserver /bin/bash

```

기존에 업로드한 chatbot 폴더 접속후
nano chatbot.py 수정

```
# chatbot.py 파일 위쪽에 추가
# DB 접속 IP를  본인 IP로 수정 (local ipconfig에서 확인)

import json
import pymysql
db = pymysql.connect(host='172.23.247.247',user='root',password='apptools',db='flyai',charset='utf8')

cursor = db.cursor()
sql = """insert into mem set userid='ggg',userpw='1234',name='이경용',sex='M',post_num='12345',address='nohouse',tel='010-2222-3333',age='22';"""
#print(sql)
cursor.execute(sql)
db.commit()
db.close()
```
![image](https://user-images.githubusercontent.com/80855939/215920114-bc5a5ebc-d947-469d-9d50-62ac1fa9f0ba.png)

### 챗봇 실행

```
챗봇 소스 경로로 이동
cd /root/mental-health-chatbot-master

챗봇 실행
streamlit run server chatbot.py --server.port 80

브라우저에서 본인 PC IP로 접속
http://"본인 IP":80
```

