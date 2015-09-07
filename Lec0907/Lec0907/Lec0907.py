#List 예제
data = ['a','b','c',['abcd','efg']]
print(data[0])
print(data[-1])
print(data[-1][1])
print("\n")

a=[]
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']]
print(e[2][0])
f=b+c
print(b+c)
print(f)
print(b*3)
print("\n")

data[0]=['greenjoa']
print(data[0])
print(data[1])
print(data[2])
data[1]=['greenjoa1','greenjoa2']
print(data[1])
print(data[2])
data[1:2]=['greenjoa1','greenjoa2']
print(data[1])
print(data[2])
print('\n')

data.insert(2,'e')
print(data[2])
data.append('greenjoa2') #마지막에 추가됨
print(data[-1])
data.remove('c')
data[1:2]=[]
del data[0]
print('\n')

#id가 3개 있는 리스트에 비밀번호 추가후 
#이름과 번호 리스트 추가_insert 이용
data=['greenjoa1','greenjoa2','greenjoa3']
data.insert(1,'123')
data.insert(3,'345')
data.insert(5,'456')
data.insert(2,['name','010'])
data.insert(5,['name2','0102'])
data.insert(8,['name3','0103'])
print(data)
print('\n')

#for문 이용
nEntries = len(data)
print(nEntries)
for d in range(3):
    print(data[d])
print('\n')
for steps in data:
    print(steps)
print('\n')

#sort 이용
scores=[85,65,62,63,45,90,75]
print(scores)
scores.sort()
print(scores)
#top3 top5출력
scores.reverse()
top3=scores[0:3]
print(top3)
top5=scores[0:5]
print(top5)
print(scores)
