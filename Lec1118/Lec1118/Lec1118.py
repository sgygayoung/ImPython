#coding:cp949
from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def main():
    data={
        'title':'Hello',
        'name' : 'SGY'
        }
    return render_template('main.html',**data)

@app.route('/hello/')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<name2>')
def hello(name=None,name2=None):
    data = [dict(href="http://www.naver.com",caption="네이버"),
            dict(href = "http://www.goole.com",caption="구글")]
    data2 ={
        'title':'Hello',
        }
    if name==None and name2==None:
        return render_template('hello.html',items = data,**data2)
    elif name2==None:
        return render_template('hello.html',name=name,items = data,**data2)
    else:
        return render_template('hello.html',name=name,name2=name2,items = data,**data2)
if __name__=='__main__':
    #app.debug=True
    app.run()