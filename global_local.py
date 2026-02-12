a = 10 # Global Variable

def something():
    #a = 15 # Local Variable
    global a
    a = 1234
    print(a,"Inside Function") 

something()

print(a,"Outside Function")
#print(b)