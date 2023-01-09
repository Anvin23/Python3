runs = [34,78,65,90,100,45,76]

# enumerate function is a built-in function in Python that allows you to loop over a sequence(list,tuple or string)
# and get the index and value of each element in the sequence at the same time
# enumerate returns a tuple
for index,run in enumerate(runs):
    print(run)
    if(index == 4):
        print("Century")