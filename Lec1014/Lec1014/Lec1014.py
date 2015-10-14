#coding:cp949
#정규표현식
import re
pattern = re.compile("d")
result = pattern.search("dog")
print(result)
print(result.group())
result = pattern.search("dog",1)
#print(result.group())
str = '''Sample1.
Sample2.
Sample3.'''
#pattern = re.compile('^.*') #Sample1만 추출
#pattern = re.compile('^.*',re.DOTALL) #Sample 1, Sample2, Sample3 추출
pattern = re.compile('.*$') #Sample3만 추출
result = pattern.search(str)
print(result.group())
print()

#정규식 표현을 통한 잘라내기_group별로
str = '  abc  1234   xyz'
pattern = re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*")
result = pattern.match(str)
print(result.group(1))
print(result.group(2))
print()

#fullmatch 예제
pattern = re.compile("o[gh]")
result = pattern.fullmatch("og")
try:
    print(result.group())
except AttributeError:
    print('none type')
result = pattern.fullmatch("dog")
try:
    print(result.group())
except AttributeError:
    print('none type')
result = pattern.fullmatch("ogre")
try:
    print(result.group())
except AttributeError:
    print('none type')
result = pattern.fullmatch("doggie",1,3) 
#1,3은 index가 0부터 시작하니까 1,2에 (3은 없음!)있다는 의미
try:
    print(result.group())
except AttributeError:
    print('none type')
print()

#Split 예제
pattern = re.compile("\W+") #\W는 숫자나 문자가 아닌 문자 매치
result = pattern.split('words, words, words.')
print(result)
result = pattern.split('words,words,words.',1)
print(result)
pattern = re.compile("x*")
result = pattern.split('axbc')
print(result)

#sub 예제
result = re.sub(r'\W','','a:b:c, d.')
print(result)

#탐욕적인 매칭 예제
str='<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*?)">',str)
print(result.group(1))
print()

#예제
str = '123456-1234567'
pattern = re.compile("(\d{6})-(\d{7})")
result = pattern.fullmatch(str)
try:
    print(result.group(1))
    print(result.group(2))
    #2번째 방법
    pattern2 = re.compile('-')
    result2 = pattern2.split(str)
    print(result2)
except AttributeError:
    print('none type')
    
str = '1123456-1234567'
pattern = re.compile("(\d{6})-(\d{7})")
result = pattern.fullmatch(str)
try:
    print(result.group(1))
    print(result.group(2))
except AttributeError:
    print('none type')
