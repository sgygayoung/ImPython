#coding:cp949
#마이크로 웹 프레임워크 플라스크

#웹서버 돌리기
from flask import Flask, url_for, redirect
#the name of the application package
app = Flask(__name__) #플라스크 객체 생성

@app.route('/') #루트를 방문했을 때 호출해주는 함수
def hello_world():
    return 'Hello World!'

@app.route('/hello/') #hello를 방문했을 때 호출해주는 함수
def get_hello():
    #return "hello"
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return 'login:'

@app.route('/profile/<username>') #profile+이름를 입력했을 때 호출해주는 함수
def get_profile(username):
    return 'profile:'+username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id:%d'%message_id

#특정함수를 호출하는 URL를 반환해주는 함수 - 함수명, URL로 전달되는 값
with app.test_request_context():
    #Flask에서 제공하는 HTTP 요청을 테스트할수 있는 함수
    print(url_for('get_profile',username='greenjoa'))
    #redirect(url_for('get_profile',username='greenjoa')) #redirect하기 위한 함수

if __name__=='__main__':
    app.run() #배포시는 default 디버거 모드 false 지정

    #app.debug=True #소스 변경과 디버거 제공 - 개발할때만
    #app.run(host='203.252.166.29')