#coding:cp949
import sys
import os
print(sys.argv)
os.system("python test.py a b c")
print(sys.path)
print()

#pickle 예제 - class 자체를 dump 및 load
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

#os 예제
#print(os.environ)
now_path=os.getcwd()
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir(now_path)

#os-walk 예제
print(list(os.walk('..')))

#해당 디렉토리 안에 모든 텍스트 파일을 다른 폴더로 복사하는 예제
import shutil
if os.path.isdir(".\\sample")==False:
    os.mkdir("sample")
for (path, dir, files) in os.walk('.'):
    for filename in files:
        if ".txt" in filename:
            copy_file_name = ".\\sample\\"+filename
            shutil.copy(filename,copy_file_name)
print()

#dirname 예제
print(os.path.dirname('c:\python34\python.exe'))
print(os.path.abspath('~'))
print(os.path.expanduser('~\\python.exe'))