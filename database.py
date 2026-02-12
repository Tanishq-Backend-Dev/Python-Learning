import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "mansi@12345", database = "tanishq") #It stores the database connection object

mycursor = mydb.cursor() #connection to database

mycursor.execute("select * from student")

for i in mycursor:
    print(i)
