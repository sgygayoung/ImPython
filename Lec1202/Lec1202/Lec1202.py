#coding:cp949
#Numpy
import numpy as np
mileposts = np.array([0,198,303,736,871,1175,1475,1544,1913,2448])
distance_array = np.abs(mileposts-mileposts[:,np.newaxis]) 
#broadcast하기 위해 세로축으로 변환
print(mileposts)
print(mileposts[:,np.newaxis])
print(distance_array)

x,y = np.arange(5),np.arange(5)[:,np.newaxis]
#Node사이의 거리를 구하는 행렬을 만든 것
distance = np.sqrt(x**2+y**2)
print(distance)

x,y = np.arange(5),np.arange(5)[:,np.newaxis]
print(x)
print(y)
print(x+y)

x,y = np.ogrid[0:5,0:5] #grid에 대한 계산을 다루기 유용
#x : (5,1) y : (1,5) shape를 가짐
print(x)
print(y)
print("***********")
print(x+y)

x,y = np.mgrid[0:5,0:5]
#x,y : (5,5) shape를 가짐
print(x)
print(y)
print("***********")
print(x+y)
print()

from matplotlib import pyplot as plt
#plt.pcolor(distance)
#plt.colorbar()
#plt.show()

#Array Shape Manipulation
#Flattening
a = np.array([[1,2,3],[4,5,6]])
print(a.ravel()) #[1,2,3,4,5,6]
print(a.T)
print(a.T.ravel())
#Reshaping
print(a.shape)
b=a.ravel()
print(b)
b=b.reshape((2,3))
print(b)
print()
print(b.reshape((2,-1))) #unspecified (-1) value is inferred
print(b.reshape((3,2)))
print()

#Adding a dimension
z = np.array([1,2,3])
print(z[:,np.newaxis])
print(z[np.newaxis,:])

#Resizing
a=np.arange(4)
print(a)
a.resize((8,))
print(a)
#다른 변수에 의해 참조되지 않아야 변경 가능
#기본 연산이 참조니까
print()

#Sorting data
a = np.array([[4,3,5],[1,2,1]])
print(a)
b=np.sort(a,axis=0)
print(b)
b = np.sort(a,axis=1) #sorts each row separately!
print(b)
a.sort(axis=1)
print(a)

a=np.array([4,3,1,2])
print(a)
j = np.argsort(a) #sorting with index
print(j)
j_max = np.argmax(a) #finding maxima
j_min = np.argmin(a) #finding minima
print(j_max,j_min)
print()

#Advanced operations
#Polynomials
p = np.poly1d([3,2,-1]) #각 계수를 의미
print(p(0))
print(p.roots)
print(p.order)
p = np.polynomial.Polynomial([-1,2,3])
print(p)

x = np.linspace(0,1,20)
print(x)
y = np.cos(x) + 0.3*np.random.rand(20)
print(y)
p = np.poly1d(np.polyfit(x,y,3))
print(p)
t = np.linspace(0,1,200)
#plt.plot(x,y,'o',t,p(t),'-')
#plt.show()

x=np.linspace(-1,1,2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x,y,90)
t = np.linspace(-1,1,200)
plt.plot(x,y,'r.')
plt.plot(t,p(t),'k-',lw=3)
#plt.show()

#Loading data files
#data = np.loadtxt('populations.txt')
#np.savetxt('pop2.txt', data) 
#data2 = np.loadtxt('pop2.txt')

img = plt.imread('image.png')
print(img.shape, img.dtype)
plt.imshow(img[0:200,120:280])
plt.show()