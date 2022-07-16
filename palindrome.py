from cgi import print_arguments


a=int(input("Enter a number : "))
b=int(a)
rev=0
while b>0 :
    rem=b%10
    rev=(rev*10)+rem
    b=int(b/10)
if rev==a :
    print("Number is palindrome \n")
else :
    print("Number not palindrome \n")