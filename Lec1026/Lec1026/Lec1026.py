#coding:cp949
#정규표현식2 
#findall예제
str = '''Window
Unix
Linux
Solaris'''
import re
p=re.compile('^.+')
print(p.findall(str))
print()

p=re.compile('^.+',re.M)
#.은 줄바꿈을 제외한 모든 문자열이 하나이상
#M 플래그는 각 라인의 맨처음과 ^가 매치됨
print(p.findall(str))
print()

p=re.compile('^.+',re.S)
#.을 줄바꾸기 문자\n도 매치하게 함
result = p.search(str)
print(result.group())
print()

p=re.compile('^.+',re.M)
result = p.search(str)
print(result.group())
print()

#그룹 이름 지정
m=re.match(r"(?P<first_group>\w+) (?P<second_group>\w+)","Malcolm Reynolds")
print(m.group('first_group','second_group'))
print()
print(m.group('first_group'))
print()
print(m.groups())
print()
print(m.groupdict())

m=re.match(r"(\d+)\.?(\d+)?","24") #\.이 무슨의미지..???????????
print(m.groups())
print(m.groups(0))
print(m.groups(50))
print(m.group(0))
print()

#Lookahead assertion
p=re.compile(".+:")
m=p.search("http://google.com")
print(m.group())
#콜론은 제외하고 싶은데!! 그럼 (?=문자)로 해주자!
p=re.compile(".+(?=:)")
m=p.search("http://google.com")
print(m.group())

import os
os.chdir("C:\\")
print(os.getcwd())
import glob
p=re.compile('.*[.](?!bat$|exe$).*$')
#확장자가 즉, 끝이 batch파일이나 실행파일에 해당하는 것은 !제외하고 매치
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

#start end 예제
email="tony@tiremove_thisger.net"
m=re.search("remove_this",email)
print(m.group())
result = email[:m.start()]+email[m.end():]
print(result)

#display 예제
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>'%(match.group(),match.groups())
valid = re.compile(r"^[a2-9tjqk]{5}$")
print(displaymatch(valid.match("akt")))
print(displaymatch(valid.match("akt5q")))

#Url 라이브러리 예제
import urllib.request
with urllib.request.urlopen('http://www.naver.org/') as f:
    content = f.read()
    #print(content)
    p=re.compile(r"<title>(.*)</title>")
    m=re.search(p,content,re.S)
    print(p.group())
    #result=content[:m.start()]+email[m.end():]
    #print(result)
#title에 해당하는 것만 뽑아보기