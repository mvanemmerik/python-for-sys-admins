# tuples are immuutable
point =(2.0, 3.0)

point_3d  = point + (4.0,) # note, the comma. can only concatenate tuple (not "float") to tuple
print (point_3d)

# assign each item to a variable, unpack a tuple
x, y, z = point_3d
print(x)
print(y)
print(z)

# https://docs.python.org/3/tutorial/inputoutput.html
print(f'X value is {x} and y value is {y}.')

