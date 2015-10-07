#coding:cp949
#내장함수

#dir 예제
list_test = [1,2,3]
print(dir(list_test)) #객체가 가지고 있는 변수나 함수를 리스트 형태로 보여줌

#divmod예제
a,b = divmod(7,3)
print(a)
print(b)

#Enumerate 예제
#list_test = [1,2,3]
data = list(enumerate(list_test))
print(data)

#filter 예제
def even(l):
    return l%2==0
print(list(filter(even,[-2,2,3,4,5,6])))
   
#id 예제 
a=3
print(id(3))
print(id(a))
print()

#lambda 예제
l=[lambda a,b:a+b,lambda a,b:a*b]
print(l[0](3,4))
print(l[1](3,4))
print()

print(list(filter(lambda x:x%2==0, [-2,2,3,4,5,6])))
print()

#len 예제
test = [2,3,4]
print(len(test))
print(len("greenjoa"))

#list 예제
list('greenjoa')
a=[1,2,3]
b=list(a)
c=a
print(id(a))
print(id(b))
print(id(c))
print()

#map 예제
print(list(map(lambda a:a*2,[1,2,3,4])))

#max 예제
print(max([1,2,3]))
print(min("greenjoa"))

#repr예제
print(eval(repr("hi".upper())))
#print(eval(str("hi".upper()))) :Error발생

#sorted 예제
Tlist = [12,3,4,25,100,56]
print(Tlist)
print(sorted(Tlist)) # 원래 데이터 변화X
print(Tlist)
Tlist.sort() #원래 데이터 변화
print(Tlist)

#zip 예제
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print()

#이름순 및 점수 순으로 정렬
score_data = {'홍길동':[80,70,60,92], '김길동':[24,35,18,10],'고길동':[10,20,8,5]}
#print(type(score_data)) #dictionary
#name = input("이름을 입력하세요:")

for item in score_data.keys():
    score_data.get(item).sort()

x=sorted(score_data.items(), key=lambda x: x[1])
print(x)
print(score_data['홍길동'])
#print(sorted(score_data.get(name)))
