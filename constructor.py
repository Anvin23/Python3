class Person:

    def __init__(self , name , age):  # Constructor
        self.name = name
        self.age = age
    
    def info(self):
        print(f"{self.name} is {self.age} years old")


a = Person("Thor" , 1500)
# the object a is automatically passed to the constructor

a.info()