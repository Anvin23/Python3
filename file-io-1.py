
# file can be opened in different modes
#  r - read mode  (this is the default mode)
#  w - write mode
#  a - append mode

# x - create mode
# t - text mode
# b - binary mode


# read mode will give error if the file does not exist

# write mode will create a new file it the specified file does not exist
# write mode will overwrite any existing data during writing

# create mode creates a new file . gives error it the file already exist

# text mode opens the file as text file (syntax :  f = open('testfile.txt' , 'rt'))

# binary mode opens the file as a binary file (syntax :  f = open('testfile.txt' , 'rb'))



# READING TO THE FILE

f = open('testfile.txt' , 'r')
text = f.read()
f.close()

print(text)


# WRITING TO THE FILE

f = open('testfile2.txt' , 'w')
f.write("Hello World\n")
# Overwriting will happen
f.close()


# APPENDING TO THE FILE

f = open('testfile2.txt' , 'a')
f.write("Appended this line\n")
f.close()


with open('testfile.txt' , 'a') as f:
    f.write("\nIt worked")

# with statement will automatically clost the file for you