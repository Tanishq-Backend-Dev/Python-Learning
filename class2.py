class Computer:
    def __init__(self):
        self.name = "Tanishq"
        self.age = 25
        
    def update(self):
        self.age = 21

c1 = Computer()
c2 = Computer()
c1.name = "Prince"
c1.age = 16

c1.update()
print(c1.name)
print(c2.name)