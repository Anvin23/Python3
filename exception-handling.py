a = input("Enter a number : ")
# if here we input for example string , it will throw error.It will also disrupt the program
# we can handle this error using try except in python

try:
    print(f"Multiplication table of {a} is ")
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a) * i}")
except :
    # we can also write 'except Exception as e'
    print("Invalid input")

print("---------------------")


# we can also handle specific and multiple errors
try:
    num = int(input("Enter a number : "))
    a = [2,3,4]
    print(a[num])
except ValueError:
    print("Input given is not an integer !!!")
except IndexError:
    print("Index out of bounds !!!")

finally:
    print("I am always executed")

print("Some important code")

print("The end")

print("---------------------")

def func():
    list = [1,2,3]
    n = int(input("Enter a number : "))
    try:
        print(list[n])
        return 1
    except:
        print("Error occured")
        return 0
    
    finally:
        print("I am inevitable")
        # this will always run even if it comes after the return statements

    print("Remaining part of function")
    # since both try and except has a return statement , this print will not run

x = func()
print(x)