with open('num.txt' , 'r') as f:

    print(f.tell())
    # tell function returns the current position within the file in bytes


    data = f.read(3)
    # reads 3 bits from the first position
    print(data)
    print(f.tell())


    f.seek(5)
    # moves the position in the file to the specified point
    # here cursor moves to position 5

    print(f.tell())

    data = f.read(4)
    # this will read 4 bits starting from position 6()
    print(data)
    print(f.tell())




with open('truncate-sample.txt' , 'w') as f:
    f.write("This file is created to check the working of the truncate function in python")
    f.truncate(10)
    # this will truncate the file size into 10 bits(10 characters)
    # "This file " will be the content of the file