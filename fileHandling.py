f = open('myData.txt','r')

# print(f.read())

# print(f.readline())
# print(f.readline())

# print(f.readlines())

f1 = open('abc','a')

# f1.write("Prince Thakur")
# f1.write("Talented boy")

for data in f:
    f1.write(data)