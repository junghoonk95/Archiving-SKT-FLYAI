# 도커 설치후 MySQL 세팅

## 1. MySQL Docker 이미지 다운로드
```SQL
docker pull mysql
```

## 2. MySQL Docker 컨테이너 생성 및 실행
```SQL
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -d -p 3306:3306 mysql:latest
```

## 3. MySQL Docker 컨테이너 접속
```SQL
docker exec -e LC_ALL=C.UTF-8 -it "본인 Key값" ad bash
mysql -u root -p
# Enter password:창이 뜨면 비밀번호 입력 
```

*정상 작동시 

![image](https://user-images.githubusercontent.com/80855939/212869766-eb158acc-c3b0-41ab-a333-97b806158440.png)


 > 유용한 MySQL Docker 명령

```SQL 
#Docker 설치 확인하기
docker -v

#Docker 이미지를 확인
docker images

#Docker 컨테이너 리스트 출력
docker ps -a

# MySQL Docker 컨테이너 중지
docker stop mysql-container

# MySQL Docker 컨테이너 시작
docker start mysql-container

# MySQL Docker 컨테이너 재시작
docker restart mysql-container
```
