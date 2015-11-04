#coding:cp949
import re
def CheckPassword(str):
    p0=re.compile(".{8,13}")
    result = p0.fullmatch(str)
    try:
        result.group()
        p = re.compile("[a-zA-Z]+")
        result = p.search(str)
        try:
            result.group()
            p2 = re.compile("[0-9]+")
            result = p2.search(str)
            try:
                result.group()
                p3 = re.compile("[!@#$%^&*]+")
                result = p3.search(str)
                try:
                    result.group()
                    print("비밀번호 입력 완료")
                except:
                    print("특수문자 포함해야함")
            except:
                print("숫자 포함해야함")
        except:
            print("영문자 포함해야함")
    except:
        print("비밀번호는 8자 이상 13자리 이하여야함")
pw = input("비밀번호 입력하시오:")
CheckPassword(pw)
