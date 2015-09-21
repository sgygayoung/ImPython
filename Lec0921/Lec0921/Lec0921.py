#encoding:cp949
#클래스 예제
class Service:
    secret = "영구 배꼽 두개"
    def sum(self,a,b):
        result = a+b
        print("%s+%s=%s입니다."%(a,b,result))
pey = Service()
print(pey.secret)
pey.sum(1,1) #bound method call
Service.sum(pey,1,1) #unbound method call
print('\n')

class Movie:
    '''영화 클래스입니다.'''
    title = "암살"
    director="최동훈"
    count=0
    def __init__(self,title,director): #생성자
        #__언더바 두 개는 시스템에서 약속된 함수
        self.director = director
        self.title = title
        Movie.count+=1
        print(self.title+"생성자 호출")
    def __del__(self): #소멸자
        print(self.title+"소멸자 호출")
    def showInfo(self):
        print(self.title+" "+self.director)
    @staticmethod #데코레이터
    def showCount1():
        print(Movie.count)
    @classmethod #데코레이터
    def showCount2(cls):
        print(cls.count)

#소멸자 예제
m1=Movie("베테랑1","류승완1")
print(m1.count)
m2=Movie("베테랑2","류승완2")
print(m2.count)
m3=Movie("베테랑3","류승완3")
m4=Movie("베테랑4","류승완4")
print(type(m4))
m4=m3 #파이썬은 얕은 복사
print(id(m3))
print(id(m4))
m4.showInfo()

#classmethod 예제
Movie.showCount2()
Movie.showCount1()

#객체 생성 예제
#movie1 = Movie("베테랑","류승완")
#print(movie1.title)
#print(movie1.__class__.title)
#print(movie1.__doc__)
#movie1.showInfo()
#movie2=Movie("프언","지정희")
#Movie.showInfo(movie2)
#movie1.main="하정우"
#print(movie1.main)
#movie2.main="송가영"
#print(movie2.main)

#Instance 없이 멤버 접근 및 함수 이용하기
class MyClass:
    data=1
    def classTest(cls):
        print("class method")
        print(cls.data)
        print()
    CTest = classmethod(classTest)

    def staticTest():
        print("static method")
        print()
    STest=staticmethod(staticTest)
MyClass.CTest()
MyClass.STest()