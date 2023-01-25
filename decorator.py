def status(fx):  # decorator function
    # decorators allow you to modify the behavior of functions and methods

    def mfx(*args , **kwargs):  # the modified function
        print("Start")
        fx(*args , **kwargs)
        print("End")
    
    return mfx

@status
def hello():
    print("Hello World")

def multiply(a,b):
    print(a*b)


hello() # since we put @ above the function , that decorator function will act

# status(hello)()
# we would have to write like this if we did not use @ on the function
status(multiply)(5,6)
# This kind of syntax can be avoided if we use @ on the function that need to be decorated(modified)