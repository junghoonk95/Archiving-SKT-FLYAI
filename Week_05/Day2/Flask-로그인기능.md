## Flask로 만든 홈페이지에 로그인 DB 추가

* Flask 홈페이지 [Day4](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/tree/main/Week_05/Day1) 자료 참고

> 기존 id 필드를 -> userid로 변경


> userpw 라는 신규 필드 추가, 위치는 user id 밑으로, Default 값은 '1234'

```SQL
alter table mem change id userid varchar(10);
alter table mem add userpw varchar(200) after userid;
update mem set userpw = '1234';
```


## 보안을 위해 DB 비밀번호 데이터 암호화
```SQL
update mem set userpw=SHA2('1234', 256);
```
<암호화된 비밀번호>
![image](https://user-images.githubusercontent.com/80855939/212882195-c35f8f73-dcbe-4b7f-adf8-61a41db72c7e.png)

> app.py 로그인가능하게 수정
```SQL
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        join = request.args.get('join')
        return render_template('login.html', join=join)
    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        user = app.database.execute(text("""
            select name from mem where 
            userid = :userid and userpw = SHA2(:userpw, 256);"""), {
                'userid' : userid,
                'userpw' : userpw
            }).fetchone()
        return user['name']
        
        #if userid == 'admin' and userpw == '1234':
        #    return redirect('/')
        #else:
        #    return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')

```

## 홈페이지 접속후 id, password 입력
![image](https://user-images.githubusercontent.com/80855939/212882688-d4bff506-ea9d-405d-9206-34b574a1e25a.png)

> 로그인시 해당 계정 이름 확인

![image](https://user-images.githubusercontent.com/80855939/212882646-0d506242-7f21-4a39-966f-eaba80b86b4d.png)
