#coding:cp949
#��� �����
import numpy as np
data = np.array([[1,2,3],[4,5,6],[7,8,9]])

#����� ũ��
print(data.ndim)
print(data.shape)
print(len(data)) 
print()

#����� ������ �� - ����� ���� ������ Ÿ��
print(data.dtype)
data2 = np.array([[1,2,3],[4,5,6],[7,8,9.]]) 
#np.array�� ��� ���� ���������� ����.
print(data2.dtype)
print()

#�������� �����ϱ�
data.astype(np.float)
print(data.dtype)
data3=np.array(['1','2','3'])
print(data3.dtype)
data3.astype(np.int)
print(data3.dtype)
print()

#�������� �����ϱ�
data = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype = float)
print(data.dtype)
data = np.array([1,2,3],dtype=complex)
print(data.dtype)
print()

#1�� ä���� ���
print(np.ones((3,2)))
#0���� ä���� ���
print(np.zeros((3,2)))
#���� ���
print(np.eye((3)))
#�밢���
print(np.diag(np.array([1,2,3,4])))
#��ġ���
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print(data.T)
#1������ ���� ��Ŀ� ���� ��ġ����� �ٲ��� �ʴ´�!
data = np.array([1,2,3])
print(data)
print(data.T)
print()

#���� �����Ͽ� ��� �迭 �����
print(np.arange(10)) #0,,,n-1
print(np.arange(10,1,-1)) #start,end(exclusive),step
print(np.arange(10,1,-1)[:,np.newaxis]) #�� ����
print(np.arange(2,8,dtype = np.float))
print(np.arange(35).reshape(5,7))
print()

#������ ���� �迭
print(np.linspace(1.,4.,6)) #start, end, num-points
print(np.linspace(1.,4.,6,endpoint=False)) #������ ���� ����X
print(np.linspace(1.,4.,6,endpoint=True)) #������ ���� ����
print()

#���� ����
#Uniform in [0,1]
data = np.random.rand(4)
print(data)
#Gaussian
data = np.random.randn(4,4)
print(data)
print()

#����� ����
from matplotlib import pyplot as plt
data = np.loadtxt('data.txt')
print(data)
#�⵵, ��� ��ü��, ������ ��ü��, ��� ��Ȯ��
year, hares, lynxes, carrots = data.T
#plt.plot(year,hares,year,lynxes,year,carrots)
#plt.show()
print()

#�ε��� & �����̽�
#�迭�� �ε����� 0�� ������� ��, -1�� ������������ �ε���
data = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(data[0])
print(data[-1])
print(data[0:2])
print(data[:2])
print(data[2][0]) #�� ���� ��½�
print(data[2,0]) #�� ���� ��½�
print(data[1:4:2]) #start : end : step
print(data[1:4:2,::3])
print(data[::1]) #��ü ��� - slice�� 0�� �� �� ����
print(data[::-1]) #�Ųٷ� ���
print()

#�ε��� �迭
x = np.arange(10,1,-1)
print(x)
print(x[np.array([3,3,1,8])])
print(x[np.array([[1,1],[2,3]])])

y=np.arange(35).reshape(5,7)
print(y)
print(y[np.array([0,2,4])]) #0��,2��,4�� ���
b=y>20
print(b)
print(y[b])
print()

#boolean masks
mask = np.array(np.array([1,0,1,0,0,1],dtype=bool))
print(mask)
data=np.arange(60).reshape(6,10)
data2 = data[:6,:6]
print(data2)
print(data2[mask,2])
mask1 = np.array([0,1,2,3,4])
mask2 = np.array([1,2,3,4,5])
print(data2[mask1,mask2])
mask3=np.array(np.array([0,0,0,1,1,1],dtype=bool))
print((data2[3:6,mask]))