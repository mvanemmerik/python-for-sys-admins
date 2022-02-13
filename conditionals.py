print(2 in [1, 2, 3])
print(2 not in [1, 2, 3])

# indentation four spaces

if 1 == 2:
    print('this is true')
else:
    print('this is false')

name = 'Joe'
if len(name) >= 6:
    print(f'{name} is long')
elif len(name) == 5:
    print(f'{name} is five characters')
elif len(name) >= 4:
    print(f'{name} is four characters')
else:
    print(f'{name} is short')
