#coding:cp949
#Database 실습 예제
import sqlite3
#DB 생성
con = sqlite3.connect("test.db")
cur = con.cursor() #커서 획득
con.isolation_level=None

##테이블 생성
#dropsql = '''drop table if exists phonebook;'''
#cur.execute(dropsql)
#sql = '''create table if not exists
#        phonebook(name text, phoneNum text);'''
#cur.execute(sql)

##데이터 삽입
##1번째 기본 방법
#insertsql = '''insert into phonebook values('greenjoa1','010-1111-2222');'''
#cur.execute(insertsql)

##2번째 ?:인자 전달 순서에 맞추어 시퀀스 객체 전달 방법
#name = 'greenjoa2'
#phoneNumber = '010-3333-4444'
#insertsql = '''insert into phonebook values(?,?);'''
#cur.execute(insertsql,(name,phoneNumber))

##3번째 각 인자에 이름을 부여해서 수행하는 방법
##이 방법은 ?보다 가독성이 좋음 순서 기억 안해도되니까
#name = 'greenjoa3'
#phoneNumber = '010-3333-3333'
#insertsql='''insert into phonebook
#            values(:inputName, :inputNum);'''
#cur.execute(insertsql,{"inputNum":phoneNumber,"inputName":name})

##4번째 Iterator 객체를 통한 삽입
#insertsql='''insert into phonebook values(?,?);'''
#datalist=(('greenjoa4','010-4444-4444'),
#          ('greenjoa5','010-5555-5555'))
#cur.executemany(insertsql,datalist)

##5번째 제너레이터를 통한 삽입
#def dataGenerator():
#    datalist = (('greenjoa6','010-6666-6666'),('greenjoa7','010-7777-7777'))
#    for item in datalist:
#        yield item #yield:return과 같이 값을 반환하지만 종료되지 않음!!
#cur.executemany(insertsql,dataGenerator())

#con.commit() #트랜잭션 commit()

#레코드 조회
selectsql = '''select * from phonebook;'''
cur.execute(selectsql)
print(cur.fetchall())
print()

#name = 'Greenjoa8'
#phoneNumber = '010-0000-0000'
#insertsql = '''insert into phonebook values(?,?);'''
#cur.execute(insertsql,(name,phoneNumber))

#레코드 정렬
cur.execute("select * from phoneBook order by name;")
print(cur.fetchall())
print()
#cur.execute("select * from phoneBook order by name desc;")
#print(cur.fetchall())
#print()

#레코드 정렬 기준 함수 생성
def OrderFunc(str1,str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1>s2) - (s1<s2)
con.create_collation('myordering',OrderFunc)
cur.execute("select * from phoneBook order by name collate myordering;")
print(cur.fetchall())
print()

#내장 집계 함수 - count
#cur.execute("insert into phonebook(phoneNum) values('010-9999-9999');")
cur.execute("select * from phoneBook where phoneNum = '010-9999-9999';")
print(cur.fetchall())

cur.execute("select phoneNum from phoneBook;")
print(cur.fetchall())
cur.execute("select count(*) from phoneBook;")
print(cur.fetchone()[0])
print()

#내장 집계 함수 - max, min
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

#나이의 평균구하기
class Average:
    def __init__(self):
        self.sum=0
        self.cnt = 0
    def step(self, value):
        self.sum+=value
        self.cnt+=1
    def finalize(self):
        return self.sum/self.cnt
con.create_aggregate("avg",1,Average) #DB에 등록
cur.execute("select avg(age) from User;")
print(cur.fetchone()[0])