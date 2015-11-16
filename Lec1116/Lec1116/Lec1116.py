#coding:cp949
#����ũ�� �� �����ӿ�ũ �ö�ũ

#������ ������
from flask import Flask, url_for, redirect
#the name of the application package
app = Flask(__name__) #�ö�ũ ��ü ����

@app.route('/') #��Ʈ�� �湮���� �� ȣ�����ִ� �Լ�
def hello_world():
    return 'Hello World!'

@app.route('/hello/') #hello�� �湮���� �� ȣ�����ִ� �Լ�
def get_hello():
    #return "hello"
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return 'login:'

@app.route('/profile/<username>') #profile+�̸��� �Է����� �� ȣ�����ִ� �Լ�
def get_profile(username):
    return 'profile:'+username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id:%d'%message_id

#Ư���Լ��� ȣ���ϴ� URL�� ��ȯ���ִ� �Լ� - �Լ���, URL�� ���޵Ǵ� ��
with app.test_request_context():
    #Flask���� �����ϴ� HTTP ��û�� �׽�Ʈ�Ҽ� �ִ� �Լ�
    print(url_for('get_profile',username='greenjoa'))
    #redirect(url_for('get_profile',username='greenjoa')) #redirect�ϱ� ���� �Լ�

if __name__=='__main__':
    app.run() #�����ô� default ����� ��� false ����

    #app.debug=True #�ҽ� ����� ����� ���� - �����Ҷ���
    #app.run(host='203.252.166.29')