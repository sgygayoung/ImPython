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
                    print("��й�ȣ �Է� �Ϸ�")
                except:
                    print("Ư������ �����ؾ���")
            except:
                print("���� �����ؾ���")
        except:
            print("������ �����ؾ���")
    except:
        print("��й�ȣ�� 8�� �̻� 13�ڸ� ���Ͽ�����")
pw = input("��й�ȣ �Է��Ͻÿ�:")
CheckPassword(pw)
