from functools import reduce
# reduce should be imported

num = [1,2,3,4,5,6]

mysum = lambda x,y: x+y

sum = reduce(mysum , num)

# reduce is a higher order function that applies a function to a sequence and returns a single value
# the function arguement is a function that takes in two arguements and returns a single value

# the reduce function applies the function the first two elements in the iterable and then applies
# the function to the result and the next element and so on.
# the reduce function returns the final result