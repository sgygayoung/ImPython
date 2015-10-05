#coding:cp949

import xlsxwriter

def output_excel(fileName):
    library_list = [] # ���� �� ���� ���� ����Ʈ
    third_field_list = [] # ���� �� ����° �ʵ� ���� ����Ʈ(�ߺ�X)

    print( fileName+" : ���������� ����� �̷»���  ")
    print('*****************************************')
    count=0
    with open(fileName,"r") as origin_file:
        for line in origin_file:
            check = False #3��° �ʵ� �ߺ� üũ �÷���
            (fir,other) = line.strip().split("|",1)
            (sec,other2) = other.strip().split("|",1)
            (third,other3)=other2.strip().split("|",1)
            (fourth,etc)=other3.strip().split("|",1)
            for item in third_field_list:
                if item==third:
                    check = True
                    break
            if check==False:
                print("\t"+third,end='')
                third_field_list.append(third)
                count = count+1
                if count%4==0:
                    print('')
            library_list.append([fir,sec,third,fourth])
    if count%4!=0:
        print('')
    print("*****************************************")
    #���ϴ� ������ �Է¹ޱ�
    check = True
    while(check): # ����Ʈ�� �����ϴ��� Ȯ��
        choice = input("���ϴ� ������ �̸��� �Է��ϼ���:")
        for item in third_field_list:
            if choice==item:
                check = False
                break
        if check==True:
            print("�Է��Ͻ� �����ʹ� ����Ʈ�� �������� �ʽ��ϴ�.\n")
    choice_file = choice + ".xlsx"

    #���ο� ���� ���� ���� �� worksheet �߰�
    output = xlsxwriter.Workbook(choice_file)
    worksheet = output.add_worksheet()
    count=0

    #���ϴ� �׸� �ش��ϴ� ���� ������ �����ϱ�
    for item in library_list:
        if item[2]==choice:
            for i in range(4):
                worksheet.write(count,i,item[i])
            count=count+1
    output.close()
    print(choice_file+" ������ �Ϸ�Ǿ����ϴ�.")
    