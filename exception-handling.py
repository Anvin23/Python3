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


# we can also handle specific and multiple errors
try:
    num = int(input("Enter a number : "))
    a = [2,3,4]
    print(a[num])
except ValueError:
    print("Number entered is not an integer !!!")
except IndexError:
    print("Index out of bounds !!!")

print("Some important code")

print("The end")