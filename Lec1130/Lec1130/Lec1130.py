#coding:cp949
import numpy as np
#����� ���� - ������ �� ��Һ� ������ ����
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data+2)
print(data-2)
print(data**2)
print(data*data) #not matrix multiplication
print(data.dot(data)) #matrix multiplication
print()

#�� ����
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print(a==b)
print(a>b)
print()

#array �� ����
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
c = np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))
print()

#������
a = np.array([1,1,0,0],dtype = bool)
b=np.array([1,0,1,0],dtype = bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.all([True,True,False])) #��� true���� true
print(np.any([True,True,False])) #�ϳ��� true��
print()

#�ʿ��Լ� transcendental functions
a = np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))
print()

#�������
a=np.triu(np.ones((3,3)),1) 
#1�� index��ȣ,��𼭺��� ä���� �ﰢ����� ������ΰ�
print(a)
print(a.T)
print()

#Sum
x = np.array([1,2,3,4])
print(np.sum(x))
print(x.sum())

x=np.array([[1,1],[2,2]])
print(x.sum(axis=0)) #columns - first dimension
print(x.sum(axis=1)) #rows - second dimension
print(x[0,:].sum(),x[1,:].sum())
print()

#�ִ�,�ּ�
x = np.array([1,3,2])
print(x.min())
print(x.max())
print(x.argmin()) #index of minimum
print(x.argmax()) #index of maximum
print()

#�� ����
print(np.all([True,True,False]))
print(np.any([True,True,False]))
#�迭 �񱳽� �ַ� ��� - �迭�� ���Ҹ��� ���ϴϱ�
a = np.zeros((100,100))
print(np.any(a!=0))
print(np.all(a==a))
print()

#���
x = np.array([1,2,3,1])
y = np.array([[1,2,3],[5,6,1]])
print(x.mean())
print(np.median(x))
print(np.median(y))
print(np.median(y,axis =-1)) #last axis
print(x.std()) #full population standard dev.
print()

#����� ����
from matplotlib import pyplot as plt
data=np.loadtxt('data.txt')
#print(data)
#print(data.T)
year, hares, lynxes, carrots = data.T
#plt.plot(year,hares,year,lynxes,year,carrots)
#year-���䳢 �� year-�ö�Ҵ� �� year-��� �� �� ��Ʈ�� 3�� �׷��� �׷���
#print(year)

#������ ���
print(data[1:].mean(axis=1))
print(hares.mean())
print(lynxes.mean())
print(carrots.mean())
print()

#������ ǥ������
print(hares.std())
print(lynxes.std())
print(carrots.std())
print()

#�ų� ���� ���� �α��� ���� ����?
print(data[1:].argmax(axis=1))

#�ִ� ��ü���� ���� �⵵��?
print(year[hares.argmax()])
print(year[lynxes.argmax()])
print(year[carrots.argmax()])

bdata = np.arange(60).reshape(6,10)
data = bdata[:6,:6]
print(data)

data2 = np.array([[0,10,20,30,40,50]]).T
print(data2)
data3 = np.array([0,1,2,3,4,5])
print(data3)
print(data2+data3)