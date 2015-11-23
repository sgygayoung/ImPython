#coding:cp949
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing #file ����

#configuration
DATABASE = 'flask.db'
DEBUG = True
SECRET_KEY = 'development key' #�� Ű ���� ���� ���, ������ ������ ����
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
#app.config�� �ö�ũ ������ ���õ� dictionary ��ü
#from_object() �Լ��� �빮�ڷ� ������ ������ config�� �߰���Ŵ

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
def init_db():
    with closing(connect_db()) as db: #closing�̶�� ��� ���
        #���ϻӸ� �ƴ϶� db�� �ڵ����� ��������ִ� �Լ��� ���� ���̺귯��
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    #db = connect_db()
    #with open('schema.sql') as f:
    #    db.cursor().executescript(f.read())
    #db.commit()

#web server
@app.before_request # request ���� ���� ȣ��
def before_request():
    g.db = connect_db() #db ����
    #g : flask�� ���� Ŭ���� �ν��Ͻ�(global)

@app.teardown_request #request �������� ȣ��
def teardown_request(exception):
    g.db.close() #db ���� ����

@app.route('/')
def show_entries():
    #cursor ��ü�� ������ �� ���Ǹ� �����ϴ� ��ǥ�� ���
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    print(entries)
    return render_template('show_entries.html',entries = entries)

@app.route('/login/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST': #default�� get ����̴ϱ� login.html�� �б�!
        if request.form['username'] !=app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] !=app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in']=True
            flash('You were logged in') 
            # flash(): ���� request�� �޽����� �����ϴ� �Լ�
            # �޴� �ʿ����� get_flashed_messages() �Լ� �̿�
            return redirect(url_for('show_entries'))
    return render_template('login.html',error=error)

@app.route('/add/', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401) #abort() : HTTPException �߻�
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