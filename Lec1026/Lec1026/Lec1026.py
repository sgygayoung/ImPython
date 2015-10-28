#coding:cp949
#����ǥ����2 
#findall����
str = '''Window
Unix
Linux
Solaris'''
import re
p=re.compile('^.+')
print(p.findall(str))
print()

p=re.compile('^.+',re.M)
#.�� �ٹٲ��� ������ ��� ���ڿ��� �ϳ��̻�
#M �÷��״� �� ������ ��ó���� ^�� ��ġ��
print(p.findall(str))
print()

p=re.compile('^.+',re.S)
#.�� �ٹٲٱ� ����\n�� ��ġ�ϰ� ��
result = p.search(str)
print(result.group())
print()

p=re.compile('^.+',re.M)
result = p.search(str)
print(result.group())
print()

#�׷� �̸� ����
m=re.match(r"(?P<first_group>\w+) (?P<second_group>\w+)","Malcolm Reynolds")
print(m.group('first_group','second_group'))
print()
print(m.group('first_group'))
print()
print(m.groups())
print()
print(m.groupdict())

m=re.match(r"(\d+)\.?(\d+)?","24") #\.�� �����ǹ���..???????????
print(m.groups())
print(m.groups(0))
print(m.groups(50))
print(m.group(0))
print()

#Lookahead assertion
p=re.compile(".+:")
m=p.search("http://google.com")
print(m.group())
#�ݷ��� �����ϰ� ������!! �׷� (?=����)�� ������!
p=re.compile(".+(?=:)")
m=p.search("http://google.com")
print(m.group())

import os
os.chdir("C:\\")
print(os.getcwd())
import glob
p=re.compile('.*[.](?!bat$|exe$).*$')
#Ȯ���ڰ� ��, ���� batch�����̳� �������Ͽ� �ش��ϴ� ���� !�����ϰ� ��ġ
for i in glob.glob('*'):
    result=p.search(i)
    try:
        print(result.group())
    except AttributeError:
        print("",end="")
print()

#Lookbehind assertion
p=re.compile("(?<=abc)def")
m=p.search("abcdef")
print(m.group())
m=re.search('(?<=-)\w+','spam-egg')
print(m.group())
print()

#start end ����
email="tony@tiremove_thisger.net"
m=re.search("remove_this",email)
print(m.group())
result = email[:m.start()]+email[m.end():]
print(result)

#display ����
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>'%(match.group(),match.groups())
valid = re.compile(r"^[a2-9tjqk]{5}$")
print(displaymatch(valid.match("akt")))
print(displaymatch(valid.match("akt5q")))

#Url ���̺귯�� ����
import urllib.request
with urllib.request.urlopen('http://www.naver.org/') as f:
    content = f.read()
    #print(content)
    p=re.compile(r"<title>(.*)</title>")
    m=re.search(p,content,re.S)
    print(p.group())
    #result=content[:m.start()]+email[m.end():]
    #print(result)
#title�� �ش��ϴ� �͸� �̾ƺ���