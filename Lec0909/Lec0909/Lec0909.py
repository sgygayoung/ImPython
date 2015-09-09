#Dictionary 리스트 만들기
a={'name':'pey','phone':'01020331898','birth':'1118'}
print(a['name'])

b=a.keys()
print(b)

b=list(a.keys())
print(b)

b=a.values()
print(b)

b=list(a.values()) #list 반환
print(b)
print('\n')

b=a.items()
print(b)

b=a.get('name') #key를 주면 value 반환, 없는 키값일 경우 none 반환, name자체가 없으면 오류!
print(b)
a.get('foo','bar') #foo라는 key가 없으면 디폴트 값인 경우 bar를 반환
b='name' in a #해당 key가 있는지 조사
print(b)
a.clear() #지우기
print('\n')

#예제
movie ={"홍길동":{"베테랑":5.0,"암살":4.0},"고길동":{"베테랑":1.0}}
print(movie.get("홍길동"))
print(movie.get("고길동"))
hong = movie.get("홍길동") #get으로 dictionary 반환
print(hong.get("암살"))
print(movie["홍길동"]["암살"])
print('\n')

#제어문 연습
answer='yes' #input("Would you like express shipping?")
if answer.lower() == 'yes': #대문자, 소문자 상관없이 만들기
    print("That will be an extra $10")
elif answer.lower() == 'no':
    print("no")
else:
    print("what")

pocket=['paper','cellphone','money']
if 'money' in pocket:
    pass #????????pass아래 있으면 수행되네..?
    print("go taxi")
print("\n")

#구구단 출력
#for i in range(2,10):
#    for j in range(1,10):
#        print("%d*%d=%d"%(i,j,i*j),end=" ") #줄바꿈 안함
#    print('')
#print('\n')
for j in range(1,10):
    for i in range(2,10):
        print("%d*%d=%2d"%(i,j,i*j),end="  ") #줄바꿈 안함
    print('')
print('\n')

#그리기 예제
import turtle
nSides=5
color = ['red','blue','green','black','yellow']
for steps in range(nSides):
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides):
        turtle.color(color[steps])
        turtle.forward(50)
        turtle.right(360/nSides)

#메뉴 만들기
prompt = '''
1.Add
2.Del
3.List
4.Quit

Enter number:'''
number=0
while number!=4:
    print(prompt,end="")
    number=int(input())