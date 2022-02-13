ages = {
    'Monty': 47,
    'Angela': 46,
    'Parker': 12,
    'Olivia': 11
    }

print(ages)
print(ages['Angela'])

ages['Courtney'] = 21
print(ages)

del ages['Monty']
print(ages)

# pop is safer than del. del ages would delete the dict
ages['Monty'] = 47
ages.pop('Parker')
print(ages)

print(ages.keys())
print(list(ages.keys()))
print(list(ages.values()))

# multiple ways to create a dictionary
weights = dict(kevin=160, bob=240, kayla=135)
income = dict([('kevin', 100), ('bob', 90), ('kayla', 105)])
print(weights)
print(income)