# def square(x):
#     return x*x

square = lambda x: x*x
# this is the same as the above function
# it takes a variable x and returns x*x

cube = lambda x: x*x*x

# lambda functions are used for simple one line functions

print(square(9))

print(cube(5))

# lambda function is used in passing function as an arguement to a function

def f1(fx , value):
    return fx(value) + 3

x = 5
print(f1(square , x))
# f1 = x^2 + 3

print(f1(lambda x: x*x*x*x , x))
# f1 = x^4 + 3

# lambda function is an anonymous function