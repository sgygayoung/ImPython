#coding:cp949

#xlsxwriter ��ġ
#import os
#print(os.getcwd())
#os.chdir("C://Python34//XlsxWriter-master")
#print(os.getcwd())
#os.system("python setup.py install")

#���� ���� ��� �̿�
from Output_Excep_Module import output_excel
fileName = "201401.txt"
print('[���α׷��� ����] ���� ����� ���� - 201211284 �۰���\n')
try:
    output_excel(fileName)
except ImportError as e:
    print(e)
finally:
    print("done")