#coding:cp949

#Class 다중 상속
class A():
    def __init__(self, a):
        self.a = a
    def show(self):
        print("show a:",self.a)
class B(A):
    def __init__(self, b, **arg):
        super().__init__(**arg)
        self.b=b
    def show(self):
        print("show b:",self.b)
        super().show()
class C(A):
    def __init__(self, c,**arg):
        super().__init__(**arg)
        self.c = c
    def show(self):
        print("show c:",self.c)
        super().show()
class D(B,C):
    def __init__(self,d,**arg):
        super().__init__(**arg)
        self.d=d
    def show(self):
        print("show d:",self.d)
        super().show()

data = D(a=1,b=2,c=3,d=4)
data.show()
print()

#Private Variables
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    #private copy of original update() method
    __update = update
class MappingSubclass(Mapping):
    def update(self,keys,values):
        #provides new signature for update()
        #but does not break __init__()
        for item in zip(keys,values):
            self.items_list.append(item)
            print(item)

list = ['a','b','c']
Test_Class = MappingSubclass(list)
print(Test_Class.items_list)
# Test_Class.__update(['1']) : 사용불가 Private이기 때문!!!!!!!!
Test_Class.update(['name','phone','address'],['가영','01028881898','서울시 강동구'])
print(Test_Class.items_list)
print()

#예외처리
import sys
number1 = float(input('enter a number:'))
number2 = float(input('enter a number:'))
try:
    result = number1/number2
    print(result)
except ZeroDivisionError as e:
    print(e)
    print('The answer is infinity')
except:
    error = sys.exc_info()[0] # 현재 발생한 예외정보를 튜플로 반환
    classtype, value, traceback = sys.exc_info()
    print(classtype)
    print(value)
    print(error)
    sys.exit()
    print('i am sorry something went wrong')
finally:
    print('Done')
print()

