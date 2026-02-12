list = [5,8,4,6,9,2]
num = 4

def search(list,num):
    for i in range(0,len(list)):
        if list[i] == num:
            print("Value Found at",i)
            break
    else:
        print("Value Not Found")

search(list,num)