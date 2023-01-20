cube = lambda x: x*x*x

l = [1,2,3,4,5]
# Make a list containing the cubes of the numbers in the list l

# newl = []
# for item in l:
#     newl.append(cube(item))

# newl = map(cube , l)
# this will return a map object

newl = list(map(cube , l))

print(newl)

# Map function applies a function to each element in a sequence and returns a new sequence 
# containing transformed elements 