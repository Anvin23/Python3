f = open('Python.txt' , 'r')
i = 1

while True:
    line = f.readline()

    if not line:
        break

    print(f"line {i}")
    print(line , "\n")
    i+=1

# ' readlines ' can read the text line by line

f.close()