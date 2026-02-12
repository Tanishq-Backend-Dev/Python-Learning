class A:                              #Parent Class or Super Class
    def __init__(self):
        print("In A init")
        
    def feature1(self):
        print("feature 1 is working")
        
    def feature2(self):
        print("feature 2 is working")

class B:                               #Child Class or Sub Class
    def __init__(self):
        #super().__init__()
        print("In B Init")
    
    def feature3(self):
        print("feature 3 is working")
    
    def feature4(self):
        print("feature 4 is working")
        
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C Init")
    

# a1 = A()

# b1 = B()

c1 = C()