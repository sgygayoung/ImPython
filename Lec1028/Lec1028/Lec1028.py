#coding:cp949
#HTML 파싱 예제
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
print(soup.title.prettify()) #이쁘게 보여줌

#원하는 객체 찾기
print(soup.a['href'])
print(soup('p')[1])
print()
print(soup('a'))
print()
print(soup('a',{'id':'link2'})) #해당 속성값을 지정해서 찾을 수도 있음
print(soup('p',{'class':'title'}))
print()
print(soup('a')[0].parent) #부모 자식, 계층 구조도 가능
print()

#find , find_all 예제
print(soup.find('a'))
print()
print(soup.find_all(class_='sister'))
print()
print(soup.find_all('a'))

#네이버 웹툰 가져오기
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