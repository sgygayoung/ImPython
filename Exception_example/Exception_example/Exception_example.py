#coding:cp949

#xlsxwriter 설치
#import os
#print(os.getcwd())
#os.chdir("C://Python34//XlsxWriter-master")
#print(os.getcwd())
#os.system("python setup.py install")

#파일 추출 모듈 이용
from Output_Excep_Module import output_excel
fileName = "201401.txt"
print('[프로그래밍 언어론] 파일 입출력 과제 - 201211284 송가영\n')
try:
    output_excel(fileName)
except ImportError as e:
    print(e)
finally:
    print("done")