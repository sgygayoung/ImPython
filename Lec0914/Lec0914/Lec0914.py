#coding:cp949
#입력의 개수를 모르 때 함수
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

#여러 개의 값을 하나의 튜플 형태로 만들어 반환
def sum_and_mul(a,b):
    return a+b,a*b
data = sum_and_mul(3,4)
sum,mul=sum_and_mul(3,4)
print("sum=%d  mul=%d"%(sum,mul))
print(data)
print('\n')

movie_data=["홍길동",["베테랑","암살"],
       "고길동",["뷰티인사이드","암살","인사이드아웃"],
       "김길동",["베테랑","뷰티인사이드"]]
def print_data(datas):  #list 출력
    for data in datas:
        print(data)

#list 분해
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

#list 안에 list가 또 있을 때
#def item_return(data,level=0):
#    for item in data:
#        if(isinstance(item,list)):
#            item_return(item,level+1)
#        else:
#            for i in range(level):
#                print("\t",end=" ")
#            print(item)
movie_data=["홍길동",["베테랑",["류승완","황정민","유아인"],"암살",["전지현"]],
       "고길동",["뷰티인사이드","암살","인사이드아웃"],
       "김길동",["베테랑","뷰티인사이드"]]

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
