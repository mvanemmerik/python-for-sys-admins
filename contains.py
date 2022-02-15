import argparse

parser =  argparse.ArgumentParser(description='Search for words')
parser.add_argument('snippet', help='partial or complete string to search in  words')
args = parser.parse_args()
snippet =  args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

# matches = []

# for word in  words:
#     if snippet in  word.lower():
#         matches.append(word)

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# list comprehensions
matches = [word.strip() for word in words if snippet in word.lower()]

print(matches)
