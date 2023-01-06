a = int(input("Enter a number between 0 and 9 : "))

if(a<0 or a>9):
    raise ValueError("Number should be between 0 and 9")
    # we can use ' raise ' to raise custom errors(exceptions)

print(a)