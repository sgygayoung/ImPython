#coding:cp949
#�����Լ�

#dir ����
list_test = [1,2,3]
print(dir(list_test)) #��ü�� ������ �ִ� ������ �Լ��� ����Ʈ ���·� ������

#divmod����
a,b = divmod(7,3)
print(a)
print(b)

#Enumerate ����
#list_test = [1,2,3]
data = list(enumerate(list_test))
print(data)

#filter ����
def even(l):
    return l%2==0
print(list(filter(even,[-2,2,3,4,5,6])))
   
#id ���� 
a=3
print(id(3))
print(id(a))
print()

#lambda ����
l=[lambda a,b:a+b,lambda a,b:a*b]
print(l[0](3,4))
print(l[1](3,4))
print()

print(list(filter(lambda x:x%2==0, [-2,2,3,4,5,6])))
print()

#len ����
test = [2,3,4]
print(len(test))
print(len("greenjoa"))

#list ����
list('greenjoa')
a=[1,2,3]
b=list(a)
c=a
print(id(a))
print(id(b))
print(id(c))
print()

#map ����
print(list(map(lambda a:a*2,[1,2,3,4])))

#max ����
print(max([1,2,3]))
print(min("greenjoa"))

#repr����
print(eval(repr("hi".upper())))
#print(eval(str("hi".upper()))) :Error�߻�

#sorted ����
Tlist = [12,3,4,25,100,56]
print(Tlist)
print(sorted(Tlist)) # ���� ������ ��ȭX
print(Tlist)
Tlist.sort() #���� ������ ��ȭ
print(Tlist)

#zip ����
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print()

#�̸��� �� ���� ������ ����
score_data = {'ȫ�浿':[80,70,60,92], '��浿':[24,35,18,10],'��浿':[10,20,8,5]}
#print(type(score_data)) #dictionary
#name = input("�̸��� �Է��ϼ���:")

for item in score_data.keys():
    score_data.get(item).sort()

x=sorted(score_data.items(), key=lambda x: x[1])
print(x)
print(score_data['ȫ�浿'])
#print(sorted(score_data.get(name)))
