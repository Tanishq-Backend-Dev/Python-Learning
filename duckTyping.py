class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor():
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()        
ide.execute()
lap1 = Laptop()
lap1.code(ide)