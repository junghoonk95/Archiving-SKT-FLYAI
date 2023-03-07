# 통상적으로 Flask 서버를 돌리는 파일은 app.py로 네이밍함

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='./img')

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

        # DB 인젝션 공격 가능어부 검토
        # 이미 가입 되어 있는지 확인
        # DB에 회원정보 저장하기
        return redirect('/login?join=y')

if __name__ == '__main__':
    app.run(debug=True)




# https://dojang.io/mod/page/view.php?id=2448
# https://hazel-developer.tistory.com/48