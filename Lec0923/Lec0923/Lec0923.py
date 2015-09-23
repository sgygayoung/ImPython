#coding:cp949
#Ŭ���� ���
from abc import ABCMeta, abstractmethod
class Terran(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
        print("Terran Class"+self.name)
    @abstractmethod
    def attack(self):
        pass

class Tank(Terran):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
        print("Tank Class"+self.name+"%d"%self.damage)
    def attack(self):
        print("��ũ�� ���ϴ�.")

class Marine(Terran):
    def __init__(self,name,hp):
        super().__init__(name)
        self.hp = hp
        print("Marine Class"+self.name+"%d"%self.hp)
    def attack(self):
        print("���� ���ϴ�.")

def Attack(terran):
    terran.attack()

t1 = Tank("tank",0)
t2 = Marine("marine",100)

tlist=[Tank("tank1",0),Tank("tank2",0),Marine("marine1",200)]
for item in tlist:
    Attack(item)
#Attack(t1)
#Attack(t2)
print('')

#class Test(Tank,Marine):
#    def __init__(self,name,damage,hp,age):
#        super().__init__(name,damage)
#        self.age = age
#t = Test("abc",100,200,300)

class MyList(list):
    name=''
    def __init__(self,name):
        super().__init__([])
        self.name=name
    #������ ������
    def __str__(self):
        return self.name+":"+super().__str__()

list1=MyList("greenjoa")
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)
list1.append(60)
list1.append(100)
print(list1)
#print(list1.name)
#print(dir(list1))
print(list1.__str__())