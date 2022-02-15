names_file = open('names.txt', 'r')
print(names_file)
print("---")
print(names_file.read())
print("---")
print(names_file.read())  # no output, end of file from previous read
print("---")
names_file.seek(6) # reset cursor to 6th index
print(names_file.read())
print("---")
names_file.seek(0) # reset cursor
for line in names_file:
    print(line, end = "") # end = "" will  not add the default new line

names_file.close() # close the file when done reading
print(names_file.name) # name of file
print("---")

names_base = open('names.txt', 'r')
new_file = open('new.txt', 'w') # 'w' will truncate file if it exist
new_file.write(names_base.read())
new_file.close() # close before you can read

new_file = open('new.txt', 'r+')  # '+' read  and write
print(new_file.read())
print("---")
# new_file.seek(0)
new_file.write("Emily\n")
new_file.write("Adam\n")
new_file.seek(0)
print(new_file.read())
new_file.close() # close before you can read

print("---")

with open('new.txt', 'a') as f: # will close file after write
    f.write("Peter\n")

new_file = open('new.txt', 'r+')  # '+' read  and write
print(new_file.read())