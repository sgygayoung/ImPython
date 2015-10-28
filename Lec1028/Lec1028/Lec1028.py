#coding:cp949
#HTML �Ľ� ����
from bs4 import BeautifulSoup
html_doc= """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html.parser")
#print(soup.prettify())

print(soup.title.string)
print(soup.title.prettify()) #�̻ڰ� ������

#���ϴ� ��ü ã��
print(soup.a['href'])
print(soup('p')[1])
print()
print(soup('a'))
print()
print(soup('a',{'id':'link2'})) #�ش� �Ӽ����� �����ؼ� ã�� ���� ����
print(soup('p',{'class':'title'}))
print()
print(soup('a')[0].parent) #�θ� �ڽ�, ���� ������ ����
print()

#find , find_all ����
print(soup.find('a'))
print()
print(soup.find_all(class_='sister'))
print()
print(soup.find_all('a'))

#���̹� ���� ��������
from urllib.request import urlopen
from urllib.parse import urljoin

url = "http://comic.naver.com/webtoon/list.nhn?titleId=662162&weekday=thu"
data = urlopen(url)
#print(data.read())
print()
soup = BeautifulSoup(data,'html.parser')
#print(soup.prettify())
cartoons = soup.find_all('td',{'class':'title'})
cartoons.reverse()
for i in range(len(cartoons)):
    title=cartoons[i].find('a').string
    ref = cartoons[i].find('a')['href']
    tempurl = urljoin(url,ref)
    print(title, " ",tempurl)

import webbrowser
webbrowser.open_new(tempurl)