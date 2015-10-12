#coding:cp949
import sys
import os
print(sys.argv)
os.system("python test.py a b c")
print(sys.path)
print()

#pickle ���� - class ��ü�� dump �� load
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age = age
    def show(self):
        print(self.name," : ",self.age)

s1 = Student("gayoung",23)
s1.show()
import pickle
f = open("test.txt",'wb')
pickle.dump(s1,f)
f.close()

f=open("test.txt",'rb')
data = pickle.load(f)
print(data)
print(data.name,data.age)
data.show()

s1.age=25
s1.show()
data.show()
print()

#os ����
#print(os.environ)
now_path=os.getcwd()
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir(now_path)

#os-walk ����
print(list(os.walk('..')))

#�ش� ���丮 �ȿ� ��� �ؽ�Ʈ ������ �ٸ� ������ �����ϴ� ����
import shutil
if os.path.isdir(".\\sample")==False:
    os.mkdir("sample")
for (path, dir, files) in os.walk('.'):
    for filename in files:
        if ".txt" in filename:
            copy_file_name = ".\\sample\\"+filename
            shutil.copy(filename,copy_file_name)
print()

#dirname ����
print(os.path.dirname('c:\python34\python.exe'))
print(os.path.abspath('~'))
print(os.path.expanduser('~\\python.exe'))