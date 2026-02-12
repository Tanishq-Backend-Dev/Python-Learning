class Student:
    
    def __init__(self,name,rollno,): #Instance Method
        self.name = name
        self.rollno = rollno
        #self.laptop = self.laptop()

    def show(self): #Instance Method
        print(self.name,self.rollno)
        
    class laptop: #Inner Class
        def __init__(self): #Instance Method
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
            
        def show(self): #Instance Method
            print(self.brand,self.cpu,self.ram)



s1 = Student("Tanishq",115)
s2 = Student("Swarn",113)
#print(s1.name,s1.rollno)
s1.show()

Student.laptop().show()