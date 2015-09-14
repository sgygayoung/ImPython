#coding:cp949

def item_return(data,level=0):
    for item in data:
        if(isinstance(item,list)):
            item_return(item,level+1)
        else:
            for i in range(level):
                print("\t",end=" ")
            print(item)