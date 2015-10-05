#coding:cp949

import xlsxwriter

def output_excel(fileName):
    library_list = [] # 파일 내 정보 저장 리스트
    third_field_list = [] # 파일 내 세번째 필드 저장 리스트(중복X)

    print( fileName+" : 도서관에서 대출된 이력사항  ")
    print('*****************************************')
    count=0
    with open(fileName,"r") as origin_file:
        for line in origin_file:
            check = False #3번째 필드 중복 체크 플래그
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
    #원하는 데이터 입력받기
    check = True
    while(check): # 리스트에 존재하는지 확인
        choice = input("원하는 데이터 이름을 입력하세요:")
        for item in third_field_list:
            if choice==item:
                check = False
                break
        if check==True:
            print("입력하신 데이터는 리스트에 존재하지 않습니다.\n")
    choice_file = choice + ".xlsx"

    #새로운 엑셀 파일 생성 및 worksheet 추가
    output = xlsxwriter.Workbook(choice_file)
    worksheet = output.add_worksheet()
    count=0

    #원하는 항목에 해당하는 정보 엑셀에 저장하기
    for item in library_list:
        if item[2]==choice:
            for i in range(4):
                worksheet.write(count,i,item[i])
            count=count+1
    output.close()
    print(choice_file+" 생성이 완료되었습니다.")
    