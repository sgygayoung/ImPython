#encoding:cp949
import pickle
fileName = "��������¿���2.txt"
###########help ����
#help(str.split)
with open(fileName,"r") as myfile:
    #myfile.write("201211284 �۰���\n")
    #myfile.write("201311285 �̰���\n")
    #myfile.write("201111286 �谡��\n")
    #myfile.write("201011287 ������\n")

    #content=myfile.readlines()
    #print(content)

    #Ŀ�� �� ������ �����??????????????????????????

    #content=myfile.read()
    #print(content)
    #for content in myfile:
    #    (role,etc) = content.strip().split(":")
    role_list = []
    with open("Monica.txt","r") as write_file:
        for line in myfile :
            #if "Monica:" in line:
            #    (role,etc) = line.strip().split(":",1)
            #    write_file.write(etc)
            #    write_file.write("\n")
            #    print(line)
            (role,etc) = line.strip().split(":",1)
            role_list.append(role)
    print(role_list)
    #################PICKLE �̿��ϱ�
    list_file=open("monica_list.txt","wb+")
    pickle.dump(role_list,list_file)
    list_file.close()
    list_file=open("monica_list.txt","rb")
    result = pickle.load(list_file)
    print(result)
    list_file.close()
            #if role == "Monica":
            #    write_file.write(etc)
            #    write_file.write('\n')

    #while True:
    #    content=myfile.readline()
    #    if not content : break
    #    print(content)
