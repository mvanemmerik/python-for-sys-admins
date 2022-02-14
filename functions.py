def hello_world():
    print("Hello World!")

print(hello_world)
print("---")
hello_world()

print("---")
def print_name(name):
    print(f"Hello {name}!")

print_name(input("What is your name? "))

print("---")
def add_two(num):
    return num + 2

result = add_two(5)
print(result)