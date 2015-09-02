#출력 예제
print("Hey"+"The first is{0:d} The Second is {1:4d}".format(2,3))
print("\n")

#입력받기 및 형변환 예제
salary="20"#input("Enter salary:")
bonus="10"#input("Enter bonus:")
payCheck=salary+bonus
print("Before"+payCheck)
print(type(payCheck))
salary = int(salary)
bonus = int(bonus)
payCheck = salary+bonus
print("After:%d"%payCheck)
print(type(payCheck))
print("\n")

#문자열 인덱싱 예제
name = "greenjoa"
print(name[0])
print(name[-1])
print(name[-2])
print("\n")

#문자열 파싱 예제
info = "201012345greenjoa"
sid = info[:9]
sname = info[9:]
print(sid+" "+sname)
print("\n")

#왼쪽 정렬 및 오른쪽 정렬 예제
a = "I eat %10s apples"%"five"
print(a)
a = "I eat %-10s apples"%"five"
print(a)
a = "Error is %d%%"%98
print(a)
print("\n")

#이름으로 치환하기
print("I ate {number}apples and I was sick {day}days\n".format(number=10, day=4))

#문자열 쪼개기
a="Life is too short"
b = a.split()
print(b[0]+"\n")

#test
ans = input("종료할까요?")
if(ans.lower()=="yes"):
    print(ans.lower())
if(ans.lower()=="no"):
    print(ans.lower())
print(ans.lower())
print(ans.upper())
print(ans.swapcase())