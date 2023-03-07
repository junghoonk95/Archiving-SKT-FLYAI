# MySQL 연동 - 로그인 Session

**app.py**

```python
from flask import Flask, render_template, request, redirect, session
```

session 모듈 추가



```python
app = Flask(__name__, static_folder='./img') app.config['SECRET_KEY'] = 'apptools'

app.config['SECRET_KEY'] = 'apptools'
```

세션 저장 시 암호화 할 키 값 지정하기



```python
@app.route('/') 
def index():    
    if 'ss_name' in session:        
        ss_name = session['ss_name']    
    else:        
        ss_name = ""    
        return render_template('index.html', ss_name=ss_name)

@app.route('/login', methods=['GET','POST']) 
def login():    
    if request.method == 'GET':        
        join = request.args.get('join')        
        return render_template('login.html', join=join)    
    elif request.method == 'POST':        
        userid = request.form['userid']        
        userpw = request.form['userpw']         
        sql = f"""select name from mem where         
        userid = '{userid}' and         
        userpw = SHA2('{userpw}', 256);"""        
        user = app.database.execute(text(sql)).fetchone()        
        
        if user:            
            session['ss_id'] = userid            
            session['ss_name'] = user['name']            
            return redirect('/')                    
        else:            
            return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')
```









로그아웃

```python
@app.route('/logout') 
def logout():    
    session['ss_id'] = False    
    session['ss_name'] = False    
    return redirect('/')

```



```html
/templates/index.html

{% extends "base.html" %}
{% block content %}
```




<p>로그인 하기</p>

```html
{% if ss_name %}

<h2>{{ss_name}}님 반갑습니다.</h2>

<a href="/logout" target="_blank">LOOUT</a>
{% else %}
<a href="/login" target="_blank">LOGIN</a>
{% endif %}

<br />
<br />
<img src="/img/dog.jpg" width="600" />
{% endblock %}

{% if ss_name %}

<h2>{{ss_name}}님 반갑습니다.</h2>

<a href="/logout" target="_blank">LOOUT</a>

{% else %}

<a href="/login" target="_blank">

LOGIN</a>

{% endif %}
```



세션의 값에 따라서 보여주는 내용을 변경한다. 



## Flask 전체 소스

### 1. app.py

```python
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, text

app = Flask(__name__, static_folder='./img')
app.config['SECRET_KEY'] = 'apptools'

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = "utf-8")
app.database = database

@app.route('/')
def index():
    if 'ss_name' in session:
        ss_name = session['ss_name']
    else:
        ss_name = ""
    return render_template('index.html', ss_name=ss_name)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        join = request.args.get('join')
        return render_template('login.html', join=join)
    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        sql = f"""select name from mem where 
        userid = '{userid}' and 
        userpw = SHA2('{userpw}', 256);"""
        user = app.database.execute(text(sql)).fetchone()
        if user:
            session['ss_id'] = userid
            session['ss_name'] = user['name']
            return redirect('/')            
        else:
            return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')

@app.route('/logout')
def logout():
    session['ss_id'] = False
    session['ss_name'] = False
    return redirect('/')

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
        app.database.execute(text("""
        insert into mem set
        userid = 'abc',
        userpw = SHA2('1234', 256),
        name = '홍길동',
        sex = 'M',
        post_num = '12345',
        address = '서울시 아무때나',
        tel = '010-1111-2222',
        age = 50;""")).lastrowid
        return redirect('/login?join=y')

@app.route("/insert")
def insertdb():
    app.database.execute(text("""
    insert into mem set
    userid = 'abc',
    userpw = SHA2('1234', 256),
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

### 2. /tempates/index.html

```html
{% extends "base.html" %}
{% block content %}
<p>로그인 하기</p>

{% if ss_name %}
<h2>{{ss_name}}님 반갑습니다.</h2>
<a href="/logout" target="_blank">LOOUT</a>
{% else %}
<a href="/login" target="_blank">LOGIN</a>
{% endif %}

<br />
<br />
<img src="/img/dog.jpg" width="600" />
{% endblock %}
```



# 회원가입 프로필 이미지 추가하기 및 로그인시 프로필 이미지 가져오기



DB에 프로필 이미지 필드 추가

img 필드 varchar(200)



```code

alter table mem add img varchar(200);
```



**app.py**

```python
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, text

app = Flask(__name__, static_folder='./img')
app.config['SECRET_KEY'] = 'apptools'

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = "utf-8")
app.database = database

@app.route('/')
def index():
    if 'ss_name' in session:
        ss_name = session['ss_name']
        ss_img = session['ss_img']
    else:
        ss_name = ""
        ss_img = ""
    return render_template('index.html', ss_name=ss_name, ss_img=ss_img)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        join = request.args.get('join')
        return render_template('login.html', join=join)
    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        sql = f"""select name,img from mem where 
        userid = '{userid}' and 
        userpw = SHA2('{userpw}', 256);"""
        user = app.database.execute(text(sql)).fetchone()
        if user:
            session['ss_id'] = userid
            session['ss_name'] = user['name']
            session['ss_img'] = user['img']
            return redirect('/')            
        else:
            return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')

@app.route('/logout')
def logout():
    session['ss_id'] = False
    session['ss_name'] = False
    return redirect('/')

@app.route('/join', methods=['GET','POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else: # POST
        userid = request.form['userid']
        userpw = request.form['userpw']
        name = request.form['name']
        sex = request.form['sex']
        post_num = request.form['post_num']
        address = request.form['address']
        tel = request.form['tel']
        age = request.form['age']

        f = request.files['img1']
        f.save("./img/" + secure_filename(f.filename))
        img = f.filename

        # DB 인젝션 공격이 있는 검토
        # 이미 가입 되어 있는지 확인
        # DB에 회원정보 저장하기
        app.database.execute(text("""
        insert into mem (
            userid, userpw, name, sex, post_num, address, tel, age, img
        ) values (
            :userid, SHA2(:userpw, 256), :name, :sex, :post_num, :address, :tel, :age, :img);"""), {
                'userid' : userid,
                'userpw' : userpw,
                'name' : name,
                'sex' : sex,
                'post_num' : post_num,
                'address' : address,
                'tel' : tel,
                'age' : age,
                'img' : img,
            }).lastrowid
        return redirect('/login?join=y')

@app.route("/insert")
def insertdb():
    app.database.execute(text("""
    insert into mem set
    userid = 'abc',
    userpw = SHA2('1234', 256),
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





**/templates/join.html**

```html
{% extends "base.html" %}
{% block content %}
<div class="container">
    <form method="post" action="/join" enctype="multipart/form-data">
        <div class="mb-3 row">
            <label class="form-label" for="formid">아이디</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="formid" name="userid" value="" />
            </div>
        </div>
        <div class="mb-3 row">
            <label class="form-label">비밀번호</label>
            <div class="col-sm-10">
                <input type="password" class="form-control" name="userpw" value="" />
            </div>
        </div>
        <div class="mb-3 row">
            <label class="form-label">이름</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" name="name" value="" />
            </div>            
        </div>
        <div class="mb-3 row">
            <label class="form-label">성별</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" name="sex" value="" />
            </div>            
        </div>
        <div class="mb-3 row">
            <label class="form-label">우편번호</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" name="post_num" value="" />
            </div>            
        </div>
        <div class="mb-3 row">
            <label class="form-label">주소</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" name="address" value="" />
            </div>            
        </div>
        <div class="mb-3 row">
            <label class="form-label">전화번호</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" name="tel" value="" />
            </div>            
        </div>
        <div class="mb-3 row">
            <label class="form-label">나이</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" name="age" value="" />
            </div>            
        </div>
        <div class="mb-3 row">
            <label class="form-label">프로필이미지</label>
            <div class="col-sm-10">
                <input type="file" class="form-control" name="img1" value="" />
            </div>
        </div>
        <div class="mb-3 row">
            <div class="col-sm-10">
                <button type="submit" class="btn btn-primary">회원가입</button>
            </div>
        </div>
        {% if msg %}
        <div class="mb-3 row">
            <div class="col-sm-10">
                <div class="alert alert-danger" role="alert">
                    {{msg}}
                </div>
            </div>
        </div>
        {% endif %}
    </form>
</div>
{% endblock %}
```





![img](https://cafeptthumb-phinf.pstatic.net/MjAyMzAxMThfMjk5/MDAxNjc0MDEzMzYzODg5.asqDNJ5emqoPC3IGplEIBJ4y5QaZJdxeU_UEVsPUpi8g.4GccQgUjuCuujSi3ldzo22unwWAPewnj1e5xQQw_h00g.PNG/image.png?type=w1600)

![img](https://cafeptthumb-phinf.pstatic.net/MjAyMzAxMThfNzUg/MDAxNjc0MDEzMzcyNDEz.6gp0G1Tl2yEzbBln7Ggwgb0OGOo5Udnb1MC1XyY6F-Eg.5jW0BJECJt4gj--RMj3KRu5aqoX0jDD8lpNr9D303y4g.PNG/image.png?type=w1600)



```code
select userid, name, img from mem;
```



![img](https://cafeptthumb-phinf.pstatic.net/MjAyMzAxMThfMTI2/MDAxNjc0MDEzNDE0MzU1.b7Ox4xPVFFwnejGfekmqSAzunue_3-bL_czvh5p-ytwg.5sLn3WcRU_MrOK2aZtzmIRac1v0ScXduY_6EoBXK5jMg.PNG/image.png?type=w1600)



**/templates/index.html**



```html
{% extends "base.html" %}
{% block content %}
<p>로그인 하기</p>
{% if ss_name %}
<h2>{{ss_name}}님 반갑습니다.</h2>
{% if ss_name %}
<p><img src="/img/{{ss_img}}" width="400" /></p>
{% endif %}
<a href="/logout" target="_blank">LOOUT</a>
{% else %}
<a href="/login" target="_blank">LOGIN</a>
{% endif %}
{% endblock %}


```



# 회원 전체 리스트 보기

**/templates/list.html**

```html
{% extends 'base.html' %} 
{% block content %}
    <div class="container">
        <table class="table">
            <thead>
            <tr>
                <th scope="col">번호</th>
                <th scope="col">사진</th>
                <th scope="col">이름</th>
                <th scope="col">아이디</th>
                <th scope="col">성별</th>
                <th scope="col">주소</th>
                <th scope="col">나이</th>
            </tr>
            </thead>
            <tbody>
            {% for user in user_list %}
                <tr>
                    <th scope="row">{{ user['num'] }}</th>
                    <td>
                        {% if user['img'] %}
                            <img
                                    src="/img/{{user['img']}}"
                                    class="rounded-circle"
                                    style="height: 70px; width: 70px"
                            />
                        {% endif %}
                    </td>
                    <td>{{ user['name'] }}</td>
                    <td>{{ user['id'] }}</td>
                    <td>{{ user['sex'] }}</td>
                    <td>{{ user['address'] }}</td>
                    <td>{{ user['age'] }}</td>
                    <td>
                        {% if userid == user['userid'] %}
                        <a href="#" type="button" class="btn btn-primary">수정</a>
                        {% endif %}
                    </td>
                    <td>
                        {% if userid == user['userid'] %}
                        <a href="/delete?num={{user['num']}}" type="button" class="btn btn-danger">제거</a>
                        {% endif %}
                    </td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```



```python
@app.route('/list')
def list_members():
    sql = """select num, userid, name, sex, address, age, img from mem;"""
    user_list = app.database.execute(text(sql)).all()
    return render_template('list.html', user_list=user_list)

@app.route('/delete', methods=['GET'])
def delete():
    num = request.args.get('num')
    sql = "delete from mem where num = '%s' and userid='%s'" % (num, 
    session['ss_id'])
    app.database.execute(text(sql)).lastrowid    
    # 사진파일 삭제 (세션)
    return redirect('/list')
```



# Flask 웹프로그래밍 전체 소스

```python
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, text

app = Flask(__name__, static_folder='./img')
app.config['SECRET_KEY'] = 'apptools'

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = "utf-8")
app.database = database

@app.route('/')
def index():
    if 'ss_name' in session:
        ss_name = session['ss_name']
        ss_img = session['ss_img']
    else:
        ss_name = ""
        ss_img = ""
    return render_template('index.html', ss_name=ss_name, ss_img=ss_img)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        join = request.args.get('join')
        return render_template('login.html', join=join)
    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        sql = f"""select name,img from mem where 
        userid = '{userid}' and 
        userpw = SHA2('{userpw}', 256);"""
        user = app.database.execute(text(sql)).fetchone()
        if user:
            session['ss_id'] = userid
            session['ss_name'] = user['name']
            session['ss_img'] = user['img']
            return redirect('/')            
        else:
            return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')

@app.route('/logout')
def logout():
    session['ss_id'] = False
    session['ss_name'] = False
    return redirect('/')

@app.route('/join', methods=['GET','POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else: # POST
        userid = request.form['userid']
        userpw = request.form['userpw']
        name = request.form['name']
        sex = request.form['sex']
        post_num = request.form['post_num']
        address = request.form['address']
        tel = request.form['tel']
        age = request.form['age']

        f = request.files['img1']
        if f:
            f.save("./img/" + secure_filename(f.filename))
            img = f.filename
        else:
            img = ""

        # DB 인젝션 공격이 있는 검토
        # 이미 가입 되어 있는지 확인
        # DB에 회원정보 저장하기
        app.database.execute(text("""
        insert into mem (
            userid, userpw, name, sex, post_num, address, tel, age, img
        ) values (
            :userid, SHA2(:userpw, 256), :name, :sex, :post_num, :address, :tel, :age, :img);"""), {
                'userid' : userid,
                'userpw' : userpw,
                'name' : name,
                'sex' : sex,
                'post_num' : post_num,
                'address' : address,
                'tel' : tel,
                'age' : age,
                'img' : img,
            }).lastrowid
        return redirect('/login?join=y')

@app.route('/list')
def list_members():
    sql = """select num, userid, name, sex, address, age, img from mem;"""
    user_list = app.database.execute(text(sql)).all()
    return render_template('list.html', user_list=user_list, userid=session['ss_id'])

@app.route('/delete', methods=['GET'])
def delete():
    num = request.args.get('num')
    if session['ss_id'] == 'admin':
        sql = "delete from mem where num = '%s'" % (num)
    else:
        sql = "delete from mem where num = '%s' and userid='%s'" % (num, session['ss_id'])
    app.database.execute(text(sql)).lastrowid    
    # 사진파일 삭제 (세션)
    return redirect('/list')

@app.route('/edit', methods=['GET','POST'])
def edit():
    if request.method == 'GET':
        num = request.args.get('num')
        sql = f"""select * from mem where num = '{num}'"""
        user = app.database.execute(text(sql)).fetchone()
        return render_template('edit.html', user=user)
    else: # POST
        num = request.form['num']
        userid = request.form['userid']
        name = request.form['name']
        sex = request.form['sex']
        post_num = request.form['post_num']
        address = request.form['address']
        tel = request.form['tel']
        age = request.form['age']

        f = request.files['img1']
        if f:
            f.save("./img/" + secure_filename(f.filename))
            sql_img = ", img = '%s'" % (f.filename)
        else:
            sql_img = ""

        sql = f"""
        update mem set
        userid='{userid}', 
        name='{name}', 
        sex='{sex}', 
        post_num='{post_num}', 
        address='{address}', 
        tel='{tel}', 
        age='{age}'
        {sql_img}
        where num = {num}
        """
        app.database.execute(text(sql)).lastrowid
        return redirect('/list')

if __name__ == '__main__':
    app.run(debug=True)
```

