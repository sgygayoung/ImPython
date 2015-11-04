#coding:cp949
#Database �ǽ� ����
import sqlite3
#DB ����
con = sqlite3.connect("test.db")
cur = con.cursor() #Ŀ�� ȹ��
con.isolation_level=None

##���̺� ����
#dropsql = '''drop table if exists phonebook;'''
#cur.execute(dropsql)
#sql = '''create table if not exists
#        phonebook(name text, phoneNum text);'''
#cur.execute(sql)

##������ ����
##1��° �⺻ ���
#insertsql = '''insert into phonebook values('greenjoa1','010-1111-2222');'''
#cur.execute(insertsql)

##2��° ?:���� ���� ������ ���߾� ������ ��ü ���� ���
#name = 'greenjoa2'
#phoneNumber = '010-3333-4444'
#insertsql = '''insert into phonebook values(?,?);'''
#cur.execute(insertsql,(name,phoneNumber))

##3��° �� ���ڿ� �̸��� �ο��ؼ� �����ϴ� ���
##�� ����� ?���� �������� ���� ���� ��� ���ص��Ǵϱ�
#name = 'greenjoa3'
#phoneNumber = '010-3333-3333'
#insertsql='''insert into phonebook
#            values(:inputName, :inputNum);'''
#cur.execute(insertsql,{"inputNum":phoneNumber,"inputName":name})

##4��° Iterator ��ü�� ���� ����
#insertsql='''insert into phonebook values(?,?);'''
#datalist=(('greenjoa4','010-4444-4444'),
#          ('greenjoa5','010-5555-5555'))
#cur.executemany(insertsql,datalist)

##5��° ���ʷ����͸� ���� ����
#def dataGenerator():
#    datalist = (('greenjoa6','010-6666-6666'),('greenjoa7','010-7777-7777'))
#    for item in datalist:
#        yield item #yield:return�� ���� ���� ��ȯ������ ������� ����!!
#cur.executemany(insertsql,dataGenerator())

#con.commit() #Ʈ����� commit()

#���ڵ� ��ȸ
selectsql = '''select * from phonebook;'''
cur.execute(selectsql)
print(cur.fetchall())
print()

#name = 'Greenjoa8'
#phoneNumber = '010-0000-0000'
#insertsql = '''insert into phonebook values(?,?);'''
#cur.execute(insertsql,(name,phoneNumber))

#���ڵ� ����
cur.execute("select * from phoneBook order by name;")
print(cur.fetchall())
print()
#cur.execute("select * from phoneBook order by name desc;")
#print(cur.fetchall())
#print()

#���ڵ� ���� ���� �Լ� ����
def OrderFunc(str1,str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1>s2) - (s1<s2)
con.create_collation('myordering',OrderFunc)
cur.execute("select * from phoneBook order by name collate myordering;")
print(cur.fetchall())
print()

#���� ���� �Լ� - count
#cur.execute("insert into phonebook(phoneNum) values('010-9999-9999');")
cur.execute("select * from phoneBook where phoneNum = '010-9999-9999';")
print(cur.fetchall())

cur.execute("select phoneNum from phoneBook;")
print(cur.fetchall())
cur.execute("select count(*) from phoneBook;")
print(cur.fetchone()[0])
print()

#���� ���� �Լ� - max, min
dropsql = '''drop table if exists User;'''
cur.execute(dropsql)
sql = '''create table if not exists
        User(name text, age int);'''
cur.execute(sql)
insertsql='''insert into User values(?,?);'''
datalist=(('gayoung',23),
          ('minzoo',26),
          ('gwangwoon',25),
          ('youngsuk',24))
cur.executemany(insertsql,datalist)
cur.execute("select name,max(age) from User;")
print(cur.fetchone()[0])
cur.execute("select name,min(age) from User;")
print(cur.fetchone()[0])

#������ ��ձ��ϱ�
class Average:
    def __init__(self):
        self.sum=0
        self.cnt = 0
    def step(self, value):
        self.sum+=value
        self.cnt+=1
    def finalize(self):
        return self.sum/self.cnt
con.create_aggregate("avg",1,Average) #DB�� ���
cur.execute("select avg(age) from User;")
print(cur.fetchone()[0])