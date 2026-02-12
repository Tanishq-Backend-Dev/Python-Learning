import array as arr

# value = arr.array('i', [5,9,8,4,5,4,2])
# print(value)
# print(value.buffer_info())

# characters = arr.array('w',['a','e','i','o','u'])
# print(characters)

#--------------------------------------------------------------#
# val = arr.array('i',[])
# n = int(input("Enter the length of the array "))
# for i in range(n):
#     x = int(input("Enter the next value "))
#     val.append(x)
# print(val)
# val1 = int(input("Enter the value you want to search "))
# for i in val:
#     if val[i] == val1:
#         print(i)
#         break
# else:
#     print("Not Found")
#--------------------------------------------------------------#
a= arr.array('i',[1,2,3,4,5])
b = arr.array('i',[])
for i in range(0,len(a)):
    b.append(a[i]+5)
print(b)