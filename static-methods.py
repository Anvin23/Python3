class Compute:
    def __init__(self , num):
        self.num = num
    
    def addToNum(self,n):
        self.num = self.num + n
    
    def printNum(self):
        print(self.num)

    @staticmethod
    def add(a,b):
        # this is now a static method because of the decorator
        # the parameter self is not required as static method can be accessed without an object
        return a+b
    

a = Compute(9)

a.printNum()

a.addToNum(7)

a.printNum()

print(a.add(2,3))

print(Compute.add(4,6))

# add(3,4)
# cannot be used like this

# you cannot use add(static method) directly like normal independent functions
# the object can be used to access the function
# an object is not necessary to access a static method
# the classname can be used to access the static method