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

