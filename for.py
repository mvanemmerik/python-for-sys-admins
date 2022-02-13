colors =  ['cyan', 'magenta', 'yellow', 'black']

for color in colors:
    print(color)

print(color) # temp variable sill exist outside of loop

for color in colors:
    if color == 'cyan':
        continue
    elif color == 'yellow':
        break
    print(color)

print('---')

point = (1.2, 2.3, 6.8)
for value in point:
    print(value)

print('---')
ages = {
    'Monty': 47,
    'Angela': 46,
    'Parker': 12,
    'Olivia': 11
    }
for name in ages:
    print(name)

print('---')
print(ages.items())
for name, age in ages.items():
    print(f"{name} is {age}.")

print('---')
for char in "Montgomery":
    print(char)

print('---')

list_of_points = [(1,2), (3,4), (5,6)]
print(list_of_points)
for x, y  in list_of_points:
    print(f"x:{x}, y:{y}")