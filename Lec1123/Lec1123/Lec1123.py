#coding:cp949
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing #file 관련

#configuration
DATABASE = 'flask.db'
DEBUG = True
SECRET_KEY = 'development key' #이 키 사용시 세션 사용, 세션의 안전성 보장
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
#app.config는 플라스크 설정과 관련된 dictionary 객체
#from_object() 함수는 대문자로 설정된 값들을 config에 추가시킴

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
def init_db():
    with closing(connect_db()) as db: #closing이라는 모듈 사용
        #파일뿐만 아니라 db도 자동으로 종료시켜주는 함수를 가진 라이브러리
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    #db = connect_db()
    #with open('schema.sql') as f:
    #    db.cursor().executescript(f.read())
    #db.commit()

#web server
@app.before_request # request 실행 전에 호출
def before_request():
    g.db = connect_db() #db 연결
    #g : flask의 전역 클래스 인스턴스(global)

@app.teardown_request #request 마지막에 호출
def teardown_request(exception):
    g.db.close() #db 연결 해제

@app.route('/')
def show_entries():
    #cursor 객체를 생성한 후 질의를 수행하는 비표준 방법
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    print(entries)
    return render_template('show_entries.html',entries = entries)

@app.route('/login/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST': #default는 get 방식이니까 login.html로 분기!
        if request.form['username'] !=app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] !=app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in']=True
            flash('You were logged in') 
            # flash(): 다음 request에 메시지를 전달하는 함수
            # 받는 쪽에서는 get_flashed_messages() 함수 이용
            return redirect(url_for('show_entries'))
    return render_template('login.html',error=error)

@app.route('/add/', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401) #abort() : HTTPException 발생
    g.db.execute('insert into entries (title, text) values (?, ?)',
                    [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/logout/')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__=='__main__':
    init_db()
    app.run()