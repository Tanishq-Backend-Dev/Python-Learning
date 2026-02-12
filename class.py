class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        
    def config(self):
        print("Config is", self.cpu, self.ram)


com1 = Computer("i5", 16)
com2 = Computer("Ryzen",8)

# Computer.config(com1)
# Computer.config(com2)

com1.config()
com2.config()


class Employee:
    def __init__(self,salary,position,company):
        self.salary = salary
        self.position = position
        self.company = company

tanishq = Employee(68000,"Conversational AI Engineer","HSBC")
print(tanishq.salary)