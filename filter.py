# Filter function filters a sequence of elements on a given predicate (a function that returns a boolean
#  value) and returns a new sequence containing only the elements that meet the predicate


l = [4,7,9,-3,-4,78,200,-103]

def filter_fun(a):
    return a>=0

newl = filter(filter_fun , l)
# it filters the values greater than or equal to 0
# we can also use lambda functions
# it returns a filter object

print(list(newl))