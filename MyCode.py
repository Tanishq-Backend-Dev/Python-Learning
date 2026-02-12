# ||Taking user input in Python - Video #18||
# Note:- By default input method returns string.

# x = int(input("Enter first number "))
# y = int(input("Enter second number "))
# z = x + y
# print(z)

# ||eval()-> It evaluates the expression.||

# result = eval(input("Enter an expression "))
# print(result)

## Write a code to find the cube of the number.

# c = int(input("Enter a number "))
# print("The cube of your number is ", c**3)

# ---------------------------------------------- #

# Prime number

n = 10
for i in range(2,n):
    if n%i==0:
        print("Not a Prime number")
        break
else:
    print("Prime Number")
