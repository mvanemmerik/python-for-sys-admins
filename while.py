x = 0
while x <= 5:
    print(x)
    x += 1
print('---')
x = 0
while x <= 10:
    if x % 2 == 0:
        print(f'Even: {x}')
        x += 1
        continue
    print(f'Odd: {x}')
    x += 1

x = 1
while x <= 10:
    if x % 2 == 0:
        print(f'Even: {x}')
        x += 1
        break
    print(f'Odd: {x}')
    x += 1


