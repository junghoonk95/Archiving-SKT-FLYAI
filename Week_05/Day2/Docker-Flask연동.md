## 1. config.py 생성

> 전날에 만든 Flask 홈페이지와 Docker와 연동

* Flask 홈페이지 [Day4](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/tree/main/Week_05/Day1) 자료 참고


```console
pip install sqlalchemy
pip install mysql-connector-python
```

```SQL

db = {
    'user'     : 'root',
    'password' : 'apptools',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'flyai'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

```

## 2. 기존 app.py 코드 추가 및 수정

> 추가 내용

```SQL

... 생략 ...
from sqlalchemy import create_engine, text

app = Flask(__name__, static_folder='./img')

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = "utf-8")
app.database = database

... 생략 ...

@app.route("/insert")
def insertdb():
    app.database.execute(text("""
    insert into mem set
    id = 'abc',
    name = '홍길동',
    sex = 'M',
    post_num = '12345',
    address = '서울시 아무때나',
    tel = '010-1111-2222',
    age = 50;""")).lastrowid
    return "Insert DB OK"

if __name__ == '__main__':
    app.run(debug=True)

```

> 최종 app.py 코드
```SQL
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, text

app = Flask(__name__, static_folder='./img')

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = "utf-8")
app.database = database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        join = request.args.get('join')
        return render_template('login.html', join=join)
    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        if userid == 'admin' and userpw == '1234':
            return redirect('/')
        else:
            return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')

@app.route('/join', methods=['GET','POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        userid = request.form['userid']
        userpw = request.form['userpw']
        name = request.form['name']
        f = request.files['img1']
        f.save("./upload/" + secure_filename(f.filename))

        # DB 인젝션 공격이 있는 검토
        # 이미 가입 되어 있는지 확인
        # DB에 회원정보 저장하기
        return redirect('/login?join=y')

@app.route("/insert")
def insertdb():
    app.database.execute(text("""
    insert into mem set
    id = 'abc',
    name = '홍길동',
    sex = 'M',
    post_num = '12345',
    address = '서울시 아무때나',
    tel = '010-1111-2222',
    age = 50;""")).lastrowid
    return "Insert DB OK"

if __name__ == '__main__':
    app.run(debug=True)
    
```

## 3. Flask 홈페이지 접속
> 홈페이지 정상 접속시
 
![image](https://user-images.githubusercontent.com/80855939/212878448-3fd7eece-f560-4961-a4ca-d5ee5b261642.png)

> /insert 접속시

![image](https://user-images.githubusercontent.com/80855939/212878862-ec57f620-cbf6-4fa2-a61a-ec0a66413700.png)


> DB에 insert된 자료 확인

![image](https://user-images.githubusercontent.com/80855939/212879168-e66c5861-032a-446d-802a-832115ce1236.png)


## 4. Flask 접속 및 /insert 시 오류시 확인 상황

### 1. app.py 혹은 flask 파일 한글경로 유무 확인

  - 경로에 한글이 있을시 오류 발생

### 2. config.py user, password 확인

- 때때로 잘못된 정보 입력되어 있는경우 오류 발생
ex) 다른 user명 혹은 password,  port 오타, host 주

### 3. /insert 코드 확인

- Mysql flyai mem 데이터베이스 양식과 다르게 적혀있을 경우 오류
- ex) app.py 에는 "userpw"로 되어있지만 데이터베이스 양식은 "passwd"로 되어있을 수 
