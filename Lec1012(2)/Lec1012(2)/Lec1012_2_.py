#coding:cp949
#glob ����
import glob
import os.path
print(glob.glob('*.txt'))
print(glob.glob(os.path.abspath('.'+'\\*.txt')))
for i in glob.iglob('*'):
    print (i)
print()

#����
ndir = nfile = 0
def traverse(dir, depth):
    global ndir, nfile
    for obj in glob.glob(dir+'/*'):
        if depth ==0:
            prefix = '|--'
        else:
            prefix = '|'+'  '*depth+'|--'
        if os.path.isdir(obj):
            ndir+=1
            print(prefix+os.path.basename(obj))
            traverse(obj,depth+1)
        elif os.path.isfile(obj):
            nfile+=1
            print(prefix+os.path.basename(obj))
        else:
            print(prefix+'unknown object:',obj)
if __name__=='__main__': #����� ��ü������ �����ų ���� ����ǰԲ�
    traverse('..',0)
    print('\n',ndir,'directories',nfile,'files')

#Tempfile ����
import tempfile
file_name = ''
with tempfile.TemporaryFile('w+',delete='False') as fp:
    fp.write('Hello World!')
    fp.seek(0)
    data = fp.read()
    print(data)
    file_name = fp.name
    print(fp.name)
print(file_name)
print(os.path.exists(file_name))
print()

#time ����
import time
time1 = time.ctime(time.time())
print(time1)
t = time.strptime(time1)
print(t)
print(time.strftime('%B %dth %A %I:%M',t))
print(time.strftime('%b %d %a %H %M',t))
print()

#�޷� ����
import calendar
print(calendar.calendar(2015))
print("���� �� ���� : ",calendar.weekday(2015,12,27))
print(calendar.monthrange(2015,2))
print(calendar.monthrange(2016,2))
print()

#Random ����
import random
print(random.random())
list_sample = random.sample(range(100),5)
print(list_sample)

#0���� 100���� ���� 10�� �̰� ���� �ϳ� �̱�
list_test = random.sample(range(100),10)
print(list_test)
random.shuffle(list_test)
print(list_test)
print(random.choice(list_test)) 

#����ġ �ִ� ���� �߻�
data = [('Red',3),('Blue',1),('Yellow',2),('Green',4)]
datalist = []
#datalist = [val for val,cnt in data for i in range(cnt)]
for val,cnt in data:
    for i in range(cnt):
        datalist.append(val)
print(datalist)
random.shuffle(datalist)
print(datalist)
print(random.choice(datalist))

#webbrowser ����
import webbrowser
url = 'http://www.naver.com'
webbrowser.open_new(url)
webbrowser.open_new_tab(url)