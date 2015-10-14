#coding:cp949
#����ǥ����
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
#pattern = re.compile('^.*') #Sample1�� ����
#pattern = re.compile('^.*',re.DOTALL) #Sample 1, Sample2, Sample3 ����
pattern = re.compile('.*$') #Sample3�� ����
result = pattern.search(str)
print(result.group())
print()

#���Խ� ǥ���� ���� �߶󳻱�_group����
str = '  abc  1234   xyz'
pattern = re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*")
result = pattern.match(str)
print(result.group(1))
print(result.group(2))
print()

#fullmatch ����
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
#1,3�� index�� 0���� �����ϴϱ� 1,2�� (3�� ����!)�ִٴ� �ǹ�
try:
    print(result.group())
except AttributeError:
    print('none type')
print()

#Split ����
pattern = re.compile("\W+") #\W�� ���ڳ� ���ڰ� �ƴ� ���� ��ġ
result = pattern.split('words, words, words.')
print(result)
result = pattern.split('words,words,words.',1)
print(result)
pattern = re.compile("x*")
result = pattern.split('axbc')
print(result)

#sub ����
result = re.sub(r'\W','','a:b:c, d.')
print(result)

#Ž������ ��Ī ����
str='<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*?)">',str)
print(result.group(1))
print()

#����
str = '123456-1234567'
pattern = re.compile("(\d{6})-(\d{7})")
result = pattern.fullmatch(str)
try:
    print(result.group(1))
    print(result.group(2))
    #2��° ���
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
