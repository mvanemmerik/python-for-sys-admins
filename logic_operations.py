name = ""
print(bool(name))
print(bool(not name))
if not name:
    print('No name given')

print('---')

first=''
last = 'Smith'

if first or last:
    print('Name given')
print('---')
last_name = last or "Doe"
print(last_name)
print(0 or  False or 'This will print' or 'This will not print')
print('---')

first='Monty'
last = 'van Emmerik'

if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")
else:
    print('No name given.')

print('---')
print(1 and 2 and "print this")
print (first and last)
print(f"{first} {last}")
print('---')
print (first and last and f"{first} {last}")