#In python, function is group of related statements that performs specific task

#Function Declaration
def GreetMe(name):
    print('Good Morning : ' + name)

def AddIntegers(a, b):
    print(a+b)

def AddIntegers1(a, b):
    return a+b

    #Function Call
GreetMe("Rohit Deshpande")
AddIntegers(2,3)
print(AddIntegers1(2, 2))


print("---------------------------------------------------")

def Greetings():
    print("Hello Rohit Deshpande")

def Greetings1(name):
    print("Hello, " + name)

Greetings()
Greetings1("Rohit")