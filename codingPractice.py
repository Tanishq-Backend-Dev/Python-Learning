#37 Done

# 🟢 BEGINNER LEVEL (1–30)

# Q.1.Hello World program

# print("Hello World !")

# Q.2.Take user input and print it

# age = int(input("Please enter your age:- "))
# print(age)

# Q.3.Check if a number is even or odd

# num = int(input("Enter a number:- "))
# if num%2==0:
#     print(num,"is a even number")
# else:
#     print(num,"is a odd number")

# Q.4.Find the largest of two numbers

# num1 = int(input("Enter a number :- "))
# num2 = int(input("Enter a number :- "))
# if num1>num2:
#     print(num1,"is greater than",num2)
# else:
#     print(num2,"is greater than",num1)

# Q.5.Find the largest of three numbers

# num1 = int(input("Enter a number :- "))
# num2 = int(input("Enter a number :- "))
# num3 = int(input("Enter a number :- "))
# if num1>num2 and num1>num3:
#     print(num1,"is greater than",num2,"and",num3)
# elif num2>num1 and num2>num3:
#     print(num2,"is greater than",num1,"and",num3)
# else:
#     print(num3,"is greater than",num1,"and",num2)

# Q.6.Swap two variables

# a = int(input("Enter a number:- "))
# b = int(input("Enter a number:- "))
# print("After swapping")
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# Q.7.Calculate factorial of a number

# num = int(input("Enter a number:- "))
# fac = 1
# for i in range(1,num+1):
#     fac = fac * i
# print("The factorial of your number is",fac)

# Q.8.Generate Fibonacci series

# n = int(input("Enter a number:- "))
# a = 0
# b = 1
# if n <= 0:
#     print("Please enter a number greater than 0")
# elif n == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)

# Q.9.Check if a number is prime

# num = int(input("Enter a number:- "))
# if num<=1:
#     print("Please enter a number greater than 1")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")

# Q.10.Print all prime numbers in a range



# Q.11.Reverse a number

# num = int(input("Enter a number:- "))
# str_num = str(num)
# reversed_str_num = str_num[::-1]
# reversed_num = int(reversed_str_num)
# print("Your number in reverse order is:-",reversed_num)

# Q.12.Check palindrome (number & string)



# Q.13.Count digits in a number

# num = int(input("Enter a number:- "))
# str_num = str(num)
# count = 0
# for i in str_num:
#     count = count + 1
# print("The number of digits in your number is",count)

# Q.14.Sum of digits of a number

# num = int(input("Enter a number:- "))
# sum = 0
# while num>0:
#     digit = num%10
#     sum = sum + digit
#     num = num // 10
# print("The sum of a digits of your number is",sum)

# Q.15.Find ASCII value of a character



# Q.16.Simple calculator using if-else

# print("---------- Calculator ----------")
# operation = input("Which operation you want to perform? - Addition, Subtraction, Multiplication and Division:- ").lower()
# num1 = int(input("Enter a number:- "))
# num2 = int(input("Enter a number:- "))
# if operation == "addition":
#     print("result is",num1+num2)
# elif operation == "subtraction":
#     print("result is",num1 - num2)
# elif operation == "multiplication":
#     print("result is",num1*num2)
# elif operation == "division":
#     print("result is", num1/num2)

# Q.17.Area of circle / rectangle / triangle



# Q.18.Convert Celsius to Fahrenheit



# Q.19.Check leap year



# Q.20.Print multiplication table

# num = int(input("Enter a number:- "))
# for i in range(1,11):
#     print(num*i)

# Q.21.Count vowels and consonants in a string

# name = input("Enter your name:- ")
# vowels = 0
# consonants = 0
# for i in name:
#     if i in "aeiou":
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1
# print("The number of vowels in your sentence is",vowels)
# print("The number of consonants in your sentence is",consonants)

# Q.22.Reverse a string

# fullName = input("Enter your name:- ")
# reversed_fullName = fullName[::-1]
# print("Your name in reverse order is :",reversed_fullName)

# Q.23.Find string length without using len() [including spaces]

# name = input("Enter your name:- ")
# count = 0
# for i in name:
#     count = count + 1
# print("Length of your string is:-",count)

# Q.24.Check anagram



# Q.25.Find duplicate characters in a string



# Q.26.Count words in a sentence

# fullName = input("Please enter your full name:- ")
# count = 0
# for i in fullName:
#     if i == " ":
#         continue
#     else:
#         count = count + 1
# print("The number of words in your sentence is:-",count)

# Q.27.Remove spaces from a string



# Q.28.Replace substring in a string



# Q.29.Print patterns (stars, numbers)



# Q.30.Sum of first N natural numbers



# 🟡 INTERMEDIATE LEVEL (31–70)
# Data Structures, Functions, Files, OOP
# Lists & Tuples

# Q.31.Find max and min in a list



# Q.32.Remove duplicates from a list



# Q.33.Find second largest number



# Q.34.Sort list without using sort()

# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
# nums = [1,10,2,9,3,8,4,7,5,6]
# sort(nums)
# print(nums)

# Q.35.Merge two lists

# num1 = [1,2,3,4,5]
# num2 = [6,7,8,9,10]
# num3 = num1 + num2
# print("Merged list is",num3)

# Q.36.Rotate a list



# Q.37.Find common elements in two lists

# num1 = [1,2,3,4,5,6,7,8,9,10]
# num2 = [1,3,5,7,9,11,13,15,17,19]
# common_ele = []
# for i in num1:
#     if i in num2:
#         common_ele.append(i)
# print("List with common elements is",common_ele)

# Q.38.Count occurrences of elements

# marks = (11,17,14,10,17)
# occuurence = marks.count(17)
# print("The number od people who got mark 17 is",occuurence)

# Q.39.Flatten a nested list



# Q.40.Find missing number in a list



# Dictionaries & Sets

# Q.41.Word frequency counter using dictionary



# Q.42.Sort dictionary by values



# Q.43.Merge two dictionaries



# Q.44.Find key with maximum value



# Q.45.Invert dictionary



# Q.46.Remove duplicate values from dictionary



# Q.47.Find intersection of two sets



# Q.48.Check subset and superset



# Q.49.Count frequency using defaultdict



# Q.50.Group elements using dictionary



# Functions & Recursion

# Q.51.Write recursive factorial function

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(6))
# print(factorial(5))

# Q.52.Recursive Fibonacci



# Q.53.Lambda function examples

# sum = lambda a,b : a+b
# print(sum(3,9))

# Q.54.Map, filter, reduce usage

# from functools import reduce
# nums = [1,2,3,4,5,6,7,8,9,10]

# even = list(filter(lambda a : a%2==0,nums))
# doubles = list(map(lambda a : a*2, nums))
# sum = reduce(lambda a,b : a+b, nums)

# print("Filter:-",even)
# print("Map:-",doubles)
# print("Reduce:-",sum)

# Q.55.Function to check Armstrong number



# Q.56.Function decorators example



# Q.57.Variable-length arguments (*args, **kwargs)



# Q.58.Memoization using functools



# Q.59.Generator function example

# def TopNSquares(num):
#     i = 1
#     while i<=num:
#         sq = i * i
#         i = i + 1
#         yield sq
# value = TopNSquares(7)
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())

# Q.60.Custom iterator

# class TopSquares:
#     def __init__(self,limit):
#         self.num = 1
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num <= self.limit:
#             squares = self.num * self.num
#             self.num += 1
#             return squares
#         raise StopIteration
# t1 = TopSquares(4)
# print(t1.__next__())
# print(t1.__next__())
# print(t1.__next__())
# print(t1.__next__())
# print(t1.__next__())

# File Handling & Exceptions

# Q.61.Read a file line by line



# Q.62.Write data to a file



# Q.63.Count words in a file



# Q.64.Find longest line in a file



# Q.65.Copy file contents



# Q.66.Handle file not found exception



# Q.67.Custom exception class



# Q.68.Try-except-else-finally example
#Zero Division Error

# try:
#     a = int(input("Enter a number:- "))
#     b = int(input("Enter a number:- "))
#     print("Result is",a/b)
# except ZeroDivisionError as z:
#     print("Divisor cannot be zer",z)
# except ValueError as v:
#     print("Invalid value",v)
# except Exception as e:
#     print("Something went wrong",e)
# finally:
#     print("Completed")

# Q.69.Logging errors to a file



# Q.70.JSON read & write



# #🔵 ADVANCED LEVEL (71–100)
# OOP, Algorithms, Concurrency, Real-World Python
# Object-Oriented Programming

# Q.71.Create a class and object

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.company = "HSBC"
#     def organization(self):
#         return f"{self.name} is working in {self.company}"
# e1 = Employee("Tanishq", 25, 68000)
# print(e1.name)
# print(e1.age)
# print(e1.salary)
# print(e1.organization())

# Q.72.Constructor and destructor



# Q.73.Inheritance example

# class Animal:
#     def name(self):
#         print("My name is Bruno")

# class Dog(Animal):
#     def age(self):
#         print("I am 5 years old")

# d1 = Dog()
# d1.name()
# d1.age()

# Q.74.Multiple inheritance



# Q.75.Method overriding

# class Vinod:
#     def phone(self):
#         print("I have samsung phone")

# class Tanishq(Vinod):
#     def phone(self):
#         print("I have an iPhone")

# t1 = Tanishq()
# t1.phone()

# Q.76.Encapsulation (private variables)



# Q.77.Polymorphism example



# Q.78.Abstract base classes



# Q.79.Operator overloading

# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         m3 = self.m3 + other.m3
#         return (m1,m2,m3)
#     def __sub__(self,other):
#         m1 = self.m1 - other.m1
#         m2 = self.m2 - other.m2
#         m3 = self.m3 - other.m3
#         return (m1,m2,m3)
# s1 = Student(10,15,20)
# s2 = Student(5,10,15)
# s3 = s1-s2
# print(s3)

# Q.80.Dataclasses usage



# Algorithms & Logic

# Q.81.Binary search implementation

# def binarySearch(nums,val):
#     l = 0
#     u = len(nums)-1
#     while l<=u:
#         mid = (l+u)//2
#         if nums[mid]==val:
#             return mid
#         else:
#             if nums[mid]<val:
#                 l = mid + 1
#             else:
#                 u = mid - 1
#     return -1
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(binarySearch(nums,10))

# Q.82.Linear search

# def linearSearch(nums,val):
#     for i in range(0,len(nums)):
#         if nums[i]==val:
#             return i
#     return -1

# nums = [1,8,3,6,4,5,67,99]
# print(linearSearch(nums,889))

# Q.83.Bubble sort

# def bubbleSort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
# nums = [1,10,2,9,3,8,4,7,5,6]
# bubbleSort(nums)
# print(nums)

# Q.84.Selection sort

# def selectionSort(nums):
#     for i in range(0,len(nums)):
#         minpos = i
#         for j in range(i+1,len(nums)):
#             if nums[j]<nums[minpos]:
#                 minpos = j
#         temp = nums[i]
#         nums[i] = nums[minpos]
#         nums[minpos] = temp
# nums = [1,10,2,9,3,8,4,7,5,6]
# selectionSort(nums)
# print(nums)

# Q.85.Insertion sort



# Q.86.Merge sort



# Q.87.Quick sort



# Q.88.Find GCD using Euclidean algorithm



# Q.89.Check balanced parentheses (stack)



# Q.90Longest substring without repeating characters



# Advanced Python Concepts

# Q.91.Multithreading example

# from threading import Thread
# from time import *

# class Hello(Thread):
#     def run(self):
#         for i in range(6):
#             print("Hello")
#             sleep(2)

# class Hi(Thread):
#     def run(self):
#         for i in range(4):
#             print("Hi")
#             sleep(3)

# t1 = Hello()
# t2 = Hi()

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# Q.92.Multiprocessing example



# Q.93.Async/await example



# Q.94.Web scraping using requests & BeautifulSoup



# Q.95.Regex email & phone validator



# Q.96.Command-line tool using argparse



# Q.97.Environment variables handling



# Q.98.Simple REST API using Flask/FastAPI



# Q.99.SQLite database CRUD operations



# Q.100.Mini project: CLI-based To-Do App