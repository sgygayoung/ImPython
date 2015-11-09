#coding:cp949
#Database 2
#사용자 정의 자료형
#로그인 기능 예제 Id 중복체크 기능, 회원가입기능, 로그인 기능(mapping되면 불러오기)
import sqlite3 as sqlite

def init_db():
    db = sqlite.connect("test.db")
    sql = '''drop table if exists user;'''
    db.cursor().execute(sql)
    sql = '''create table user(
        user_no integer primary key autoincrement,
        userid string not null,
        username string not null,
        userpw string not null
        );'''
    db.cursor().execute(sql)
    #with open('schema.sql') as f:
    #    print(f.read())
    #    db.cursor().executescript(f.read()) 
    #    #executescript함수 : script파일(여러개의 질의문)로 실행할 때 사용
    #    db.commit()

#init_db()

#class Memeber:
#    def __init__(self,userid,username,userpw):
#        self.userid = userid
#        self.username = username
#        self.userpw = userpw
#def MemberAdapter(member):
#    return username,":",userid,":",userpw
#def MemberConverter(s):
#    name,id,pw = list(map(str,s.decode().split(":")))
#    return Member(name,id,pw)

def get_db():
    db = sqlite.connect("test.db")
    return db

def register():
    print("**** 회원가입 ****")
    print("user id : ",end="")
    userid = input()
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from user where userid = ?;",[userid])
    if(cur.fetchone()!=None):
        print("id 중복")
        return
    print("user name : ",end="")
    username = input()
    print("user passwd : ",end="")
    userpasswd = input()
    sql = "insert into user(userid,username,userpw) values(?,?,?)"
    from werkzeug import check_password_hash, generate_password_hash
    cur.execute(sql,[userid,username,generate_password_hash(userpasswd)])
    cur.execute("select * from user;")
    print(cur.fetchall())
    db.commit()
    db.close()
#init_db()
register()

def login():
    print("**** 로그인 ****")
    print("user id : ",end="")
    userid = input()
    print("user password : ",end="")
    userpasswd=input()
    sql = "select userpw from user where userid=?"
    from werkzeug import check_password_hash, generate_password_hash
    db = get_db()
    cur = db.cursor()
    cur.execute(sql,[userid])
    temp = cur.fetchone()
    if temp==None:
        print("Id가 존재 합니다.")
    else:
        if(check_password_hash(temp[0],userpasswd) == True):
            print("로그인 성공")
        else:
            print("로그인 실패")
    db.close()
login()

