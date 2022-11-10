# assign 4 to the variable x
x = 4
print(x)

# now x is a string
x = 'hello' 
print(x)

# now x is a list
x = [1, 2, 3]

y = x
print(y)

x.append(4) # append 4 to the list pointed to by x
print(y) # y's list is modified as well!

# x = 'something else'
# print(y)  # y is unchanged

x = 10
y = x
x = x + 5  # add 5 to x's value, and assign it to x
print("x =", x)
print("y =", y)

