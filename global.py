x = 5

print(x)

def update():
    global x
    # now the x we will use is the global x

    # The global keyword is used to declare that a variable is a global variaale and should be accessed 
    # from global scope

    x+=2
    # this will update the global x 

update()

print(x)