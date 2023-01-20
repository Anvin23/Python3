a = 4
b = '4'

print(a is b)
# compares exact location of object in memory

print(a == b)
# compares value

l1 = [1,2,3,4]
l2 = [1,2,3,4]

print(l1 is l2)
# will return false since they are not the same object

print(l1 == l2)
# will return true since value is same

n1 = 5
n2 = 5

# this is an immutable object

# " immutable object " is created only once in python

# here 5 is stored only once and n1 and n2 points to the same object