for i in range(10):
    print(i)
else:
    print("Loop 1 completed")

# you can use else with for and while as well
# this else will execute only if the loop is finished(completed)

for i in range(10):
    print(i)
    if i==6:
        break
else:
    print("Loop 2 completed")

# this else will not execute since the loop breaks in between and the loop is not "completed"