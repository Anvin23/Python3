def greet():
    print("Hello , Nice to meet you")

# greet()
# if we simply write greet , when another program(testgreet) import this program this greet will get executed
# ie when importing a program , it gets executed


# to avoid this we use if __name__ == "__main__" 
# if we write this statement , the code will get executed only when this very program is run
# it wont get executed while being imported

if __name__=="__main__":
    greet()