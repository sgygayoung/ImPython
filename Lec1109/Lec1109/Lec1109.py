#coding:cp949
#Database 2
#����� ���� �ڷ���
#�α��� ��� ���� Id �ߺ�üũ ���, ȸ�����Ա��, �α��� ���(mapping�Ǹ� �ҷ�����)
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
    #    #executescript�Լ� : script����(�������� ���ǹ�)�� ������ �� ���
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
    print("**** ȸ������ ****")
    print("user id : ",end="")
    userid = input()
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from user where userid = ?;",[userid])
    if(cur.fetchone()!=None):
        print("id �ߺ�")
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
    print("**** �α��� ****")
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
        print("Id�� ���� �մϴ�.")
    else:
        if(check_password_hash(temp[0],userpasswd) == True):
            print("�α��� ����")
        else:
            print("�α��� ����")
    db.close()
login()

