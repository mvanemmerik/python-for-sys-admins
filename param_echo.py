import sys

print(f"Argument(s) {sys.argv[1:]}") # output the arguments starting with index 1

# Input: python param_echo.py monty 'van emmerik'
# Output: Argument(s) ['monty', 'van emmerik']

print(f"First rgument(s) {sys.argv[1]}") # this will fail if no arguments
# IndexError: list index out of range
# use argparse instead for better error handling

