#encoding:cp949
#Ŭ���� ����
class Service:
    secret = "���� ��� �ΰ�"
    def sum(self,a,b):
        result = a+b
        print("%s+%s=%s�Դϴ�."%(a,b,result))
pey = Service()
print(pey.secret)
pey.sum(1,1) #bound method call
Service.sum(pey,1,1) #unbound method call
print('\n')

class Movie:
    '''��ȭ Ŭ�����Դϴ�.'''
    title = "�ϻ�"
    director="�ֵ���"
    count=0
    def __init__(self,title,director): #������
        #__����� �� ���� �ý��ۿ��� ��ӵ� �Լ�
        self.director = director
        self.title = title
        Movie.count+=1
        print(self.title+"������ ȣ��")
    def __del__(self): #�Ҹ���
        print(self.title+"�Ҹ��� ȣ��")
    def showInfo(self):
        print(self.title+" "+self.director)
    @staticmethod #���ڷ�����
    def showCount1():
        print(Movie.count)
    @classmethod #���ڷ�����
    def showCount2(cls):
        print(cls.count)

#�Ҹ��� ����
m1=Movie("���׶�1","���¿�1")
print(m1.count)
m2=Movie("���׶�2","���¿�2")
print(m2.count)
m3=Movie("���׶�3","���¿�3")
m4=Movie("���׶�4","���¿�4")
print(type(m4))
m4=m3 #���̽��� ���� ����
print(id(m3))
print(id(m4))
m4.showInfo()

#classmethod ����
Movie.showCount2()
Movie.showCount1()

#��ü ���� ����
#movie1 = Movie("���׶�","���¿�")
#print(movie1.title)
#print(movie1.__class__.title)
#print(movie1.__doc__)
#movie1.showInfo()
#movie2=Movie("����","������")
#Movie.showInfo(movie2)
#movie1.main="������"
#print(movie1.main)
#movie2.main="�۰���"
#print(movie2.main)

#Instance ���� ��� ���� �� �Լ� �̿��ϱ�
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