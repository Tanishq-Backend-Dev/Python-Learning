# def greet(): || Function_Definition
#     print("Hello Ji")
#     print("Good Morning")

# greet() || Function_Calling

#----------------------------------------------------------------------------------------#

# Function to add two numbers

# def add(x,y):
#     s = x + y
#     print(s)
# add(3,5)

# def add():
#     a = int(input("Enter first number "))
#     b = int(input("Enter second number "))
#     c = a + b
#     print(c)
# add()

#----------------------------------------------------------------------------------------#

# Function_Arguments

# def update(x):
#     x = 8
#     print(x)
# update(10)

#----------------------------------------------------------------------------------------#

# Types of arguments - Position, Keyword, Default, Variable Length

# Position Arguments 

# def person(name, age):
#     print(name)
#     print(age)
    
# person('Tanishq',25)

# Keyword Arguments

# def person(name, age):
#     print(name)
#     print(age-5)
# person(age=25,name='Tanishq')

# Default

# def person(name,age=25):
#     print(name)
#     print(age)
# person('Tanishq')

# Variable Length

# def sum(a, *b):
#     c = a
#     for i in b:
#         c = c + i
#         print(c)
# sum(5,6,34,33)

#----------------------------------------------------------------------------------------#

# Keyworded variable length arguments

# def person(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)

# person('Tanishq', age = 25, city = 'Bangalore', Mobile = 9522191988)

#----------------------------------------------------------------------------------------#