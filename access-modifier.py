class Employee:
    def __init__(self):
        self.text = "Hello world" # variables are public by default in python
    
    def _speak(self): 
        # using _ is a "convention" to indicate it is a protected variable/function
        # this is only a convention and has no effect in reality(unlike private)
        print("I am an employee")


class Programmer(Employee):
    def __init__(self):

        self.__language = "Python"
        # using __ (2 _) is a "convention" to indicate it is a private variable/function
        # cannot access from outside directly
        # But it can be accessed indirectly
        # 'mangling' is done when __ is used
        


a = Employee()
b=Programmer()

print(a.text)

# print(b.__language)
# this statement will give error

print(b._Programmer__language)
# object._classname__variable


a._speak()
b._speak()