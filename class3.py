class Car:
    
    wheels = 4 # Class Variable
    
    def __init__(self):
        self.mileage = 10 #Instance variable
        self.company = "BMW"
        
c1 = Car()
c2 = Car()

c1.mileage = 15
Car.wheels = 16
print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)