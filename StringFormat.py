word = "My name is {} and I am from {}"
name = "Anvin"
country = "India"

print(word.format(name,country))
# name will go to first bracket and country to second bracket in the string word

# this can be done conveniently using fstring
print(f"My name is {name} and I am from {country}")


price = 124.9999999
print(f"Available for only {price:.2f} ruppees")
# .2f restricts the float value to just 2 decimal points

# to print the curly brackets in the string as it is instead of replacing it with a value
# use double curly brackets
print(f"To print {{name}} as it is")