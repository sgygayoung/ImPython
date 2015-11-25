#coding:cp949
#행렬 만들기
import numpy as np
data = np.array([[1,2,3],[4,5,6],[7,8,9]])

#행렬의 크기
print(data.ndim)
print(data.shape)
print(len(data)) 
print()

#행렬의 데이터 형 - 행렬은 같은 데이터 타입
print(data.dtype)
data2 = np.array([[1,2,3],[4,5,6],[7,8,9.]]) 
#np.array는 모두 같은 데이터형을 가짐.
print(data2.dtype)
print()

#데이터형 변경하기
data.astype(np.float)
print(data.dtype)
data3=np.array(['1','2','3'])
print(data3.dtype)
data3.astype(np.int)
print(data3.dtype)
print()

#데이터형 지정하기
data = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype = float)
print(data.dtype)
data = np.array([1,2,3],dtype=complex)
print(data.dtype)
print()

#1로 채워진 행렬
print(np.ones((3,2)))
#0으로 채워진 행렬
print(np.zeros((3,2)))
#단위 행렬
print(np.eye((3)))
#대각행렬
print(np.diag(np.array([1,2,3,4])))
#전치행렬
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print(data.T)
#1행으로 만든 행렬에 대해 전치행렬은 바뀌지 않는다!
data = np.array([1,2,3])
print(data)
print(data.T)
print()

#범위 지정하여 등간격 배열 만들기
print(np.arange(10)) #0,,,n-1
print(np.arange(10,1,-1)) #start,end(exclusive),step
print(np.arange(10,1,-1)[:,np.newaxis]) #행 증가
print(np.arange(2,8,dtype = np.float))
print(np.arange(35).reshape(5,7))
print()

#지정된 수의 배열
print(np.linspace(1.,4.,6)) #start, end, num-points
print(np.linspace(1.,4.,6,endpoint=False)) #마지막 값을 포함X
print(np.linspace(1.,4.,6,endpoint=True)) #마지막 값을 포함
print()

#난수 생성
#Uniform in [0,1]
data = np.random.rand(4)
print(data)
#Gaussian
data = np.random.randn(4,4)
print(data)
print()

#행렬의 연산
from matplotlib import pyplot as plt
data = np.loadtxt('data.txt')
print(data)
#년도, 토기 개체수, 동물의 개체수, 당근 수확량
year, hares, lynxes, carrots = data.T
#plt.plot(year,hares,year,lynxes,year,carrots)
#plt.show()
print()

#인덱스 & 슬라이싱
#배열의 인덱스는 0을 기반으로 함, -1은 끝에서부터의 인덱스
data = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(data[0])
print(data[-1])
print(data[0:2])
print(data[:2])
print(data[2][0]) #각 원소 출력시
print(data[2,0]) #각 원소 출력시
print(data[1:4:2]) #start : end : step
print(data[1:4:2,::3])
print(data[::1]) #전체 출력 - slice는 0이 될 수 없다
print(data[::-1]) #거꾸로 출력
print()

#인덱스 배열
x = np.arange(10,1,-1)
print(x)
print(x[np.array([3,3,1,8])])
print(x[np.array([[1,1],[2,3]])])

y=np.arange(35).reshape(5,7)
print(y)
print(y[np.array([0,2,4])]) #0행,2행,4행 출력
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