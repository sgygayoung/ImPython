#coding:cp949
#�Է��� ������ �� �� �Լ�
def sum_mul(choice, *args):
    if choice =="sum":
        result=0
        for i in args:
            result +=i
    elif choice =="mul":
        result = 1
        for i in args:
            result *=i
    return result
result = sum_mul('sum',1,2,3,4,5)
print("sum=%d"%result)

#���� ���� ���� �ϳ��� Ʃ�� ���·� ����� ��ȯ
def sum_and_mul(a,b):
    return a+b,a*b
data = sum_and_mul(3,4)
sum,mul=sum_and_mul(3,4)
print("sum=%d  mul=%d"%(sum,mul))
print(data)
print('\n')

movie_data=["ȫ�浿",["���׶�","�ϻ�"],
       "��浿",["��Ƽ�λ��̵�","�ϻ�","�λ��̵�ƿ�"],
       "��浿",["���׶�","��Ƽ�λ��̵�"]]
def print_data(datas):  #list ���
    for data in datas:
        print(data)

#list ����
def print_all_data(datas): 
    for data in datas:
        if(type(data)==list): #isinstance(item,list)
            for item in data:
                print(item)
        else:
            print(data)

print_data(movie_data)
print("\n")
print_all_data(movie_data)
print("\n")

#list �ȿ� list�� �� ���� ��
#def item_return(data,level=0):
#    for item in data:
#        if(isinstance(item,list)):
#            item_return(item,level+1)
#        else:
#            for i in range(level):
#                print("\t",end=" ")
#            print(item)
movie_data=["ȫ�浿",["���׶�",["���¿�","Ȳ����","������"],"�ϻ�",["������"]],
       "��浿",["��Ƽ�λ��̵�","�ϻ�","�λ��̵�ƿ�"],
       "��浿",["���׶�","��Ƽ�λ��̵�"]]

#import printData
#printData.item_return(movie_data)
from printData import item_return
item_return(movie_data)
print('\n')

import os
#help(os.mkdir)
print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
print(os.getcwd())
#os.system("python setup.py sdist")
os.system("python setup.py install")
