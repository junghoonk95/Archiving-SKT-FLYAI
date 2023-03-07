# Flask 실습

- 개발환경
    - VScode

```python
from flask import Flask

app = Flask(__name__)

#라우팅
@app.route('/')
def hello():
    return 'Hello, My First Flask!'
```

 

```python
#플레이 버튼으로 실행 가
if __name__ == '__main__':
    app.run()
```

- debug 모드 추가로 오류 메시지 체크 가능

## Docker 환경

- 컨테이너 기반으로 외부로부터 독립시켜 실행 가능

## HTML 렌더링

```python
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
#return 'Hello World!'
return render_template('index.html')
if __name__ == '__main__':
app.run()
```

- render_template 라이브러리로 HTML 렌더링
- python anywhere 혹은 goormide를 활용하여 서버 환경에서도 사용 가능
- templates folder에 렌더할 HTML화일 저장

## Template 상속

- 재활용성 증대

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title> 나의 첫 홈페이지 </title>
</head>
<body>
<h1> My First HomePage </h1>
<hr/>
{% block content %}
{% endblock %}
</body>
</html>
```

```html
{% extends "base.html" %}
{% block content %}
<p>네이버 이동하기</p>
<a href="http://www.naver.com" target="_blank">NAVER</a>
{% endblock %}
```

- 위와 같이 동일 부분을 상속하여 단축 가능

## static

- image, css, js 파일을 static folder에 추가하여 꾸밀 수 있음

```html
{% extends "base.html" %}
{% block content %}
<p>네이버 이동하기</p>
<a href="http://www.naver.com" target="_blank">NAVER</a>
<br />
<img src="/static/img/dog.jpg" />
{% endblock %}
```

# Request

## GET / POST

GET

- 주소에 파라미터 노출
- 용량 제한
- 보안 취약

POST

- 노출 x
- 용량 제한 x

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>wordcloud</title>
... Bootstrap CDN ...
<style>
body { padding:50px; }
h1 { text-align:center; }
</style>
</head>
<body>
<h1>Word Cloud</h1>
<form action="/wordcloud" method="post" name="frm">
<div class="form-group">
<label for="comment">News Input :</label>
<textarea class="form-control" rows="5" name="content"></textarea>
</div>
<div class="form-group">
<input type="submit" class="btn btn-primary btn-block btn-lg">
</div>
</form>
<h3>{{content}}</h3>
</body>
</html>
```

- 변수 값 전달 가능

## File Upload

```html
<input type="file" class="form-control" name="file">
```

```python
from werkzeug.utils import secure_filename
```

```python
@app.route('/upload', methods=['GET','POST'])
def upload():
if request.method == 'GET':
return render_template('upload.html')
elif request.method == 'POST':
f = request.files['file']
f.save("/home/UserID/mysite/static/upload/" + secure_filename(f.filename))
return render_template('upload.html', file=secure_filename(f.filename))
```

- 위의 함수로 파일 업로드, 저장 가능
- 파일 이름 안전하게 저장

# MySQL

- DB를 별도로 두어 데이터 관리 용이
- 보안성
- 용어 정리 → 테이블, 필드, 레코

```sql
create table 테이블 (필드명1 타입, 필드명2 타입 ...);
```

```sql
alter table 테이블명 add 새로운 필드 필드타입;
```

```sql
alter table 테이블명 drop 삭제 필드 필드타입;
```

```sql
alter table 테이블명 change 이전 필드명 새 필드;
```

```sql
alter table 테이블명 modify 필드명 새 타;
```

```sql
alter table 이전 테이블명 rename 새 테이블;
```

- mysql 접속
service mysql start
mysql -u root -p
비번 없이 엔터

# mysql 접속
1. service mysql start
2. mysql -u root -p
3. 비밀번호 입력

# 데이터베이스 조회
show databases;
# 데이터베이스 선택
use mysql;
# 선택된 데이터베이스에 테이블 조회
show tables;
# 데이터베이스 생성
create database flyai;
# 생성한 데이터베이스 선택
use flyai;
# 선택한 데이터베이스에 테이블 조회
show tables;

# 테이블 생성
create table friend(
num int not null,
name varchar(10),
address varchar(80),
tel varchar(20),
email varchar(20),
primary key(num)
);

# 테이블 구조 보기
desc friend;

# 테이블 삭제
- drop table friend;

# 테이블 생성 (auto_Increment)
- create table friend(
num int not null auto_Increment,
name varchar(10),
address varchar(80),
tel varchar(20),
email varchar(20),
primary key(num)
);
  - `auto_Increment` 값은 테이블에서 PK(Primary Key)로 많이 사용됨
  - 데이터가 입력될 때 자동으로 값이 1개씩 증가되는 칼럼 속성이기 때문에 데이터 중복이 발생하지 않기 때문

# 필드 추가하기
- alter table friend add age int;

# 필드 삭제하기
- alter table friend drop email;
- alter table friend drop age;

# 필드 변경하기
- alter table friend change tel phone int;

# 필드 타입 변경
- alter table friend modify name int;

# 테이블 이름 변경
- alter table friend rename student;
- show tables;

# 테이블 삭제
- drop table student;
- show tables;

# 테이블 생성
- create table mem (
num int not null auto_Increment,
id char(15) not null,
name char(10) not null,
sex char(1),
post_num char(8),
address char(80),
tel char(20),
age int,
primary key(num)
);
