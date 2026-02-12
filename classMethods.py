class Student:
    
    school = "LNCT"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def average(self): # Instance Method
        return (self.m1 + self.m2 + self.m3) // 3
    
    @classmethod
    def getSchoolName(cls): #Class Method
        return cls.school
    
    @staticmethod
    def info():
        print("This is a student class")
        
        
s1 = Student(34,67,32)
print(s1.average())
(Student.info())
print(Student.getSchoolName())
s2 = Student(89,32,12)


