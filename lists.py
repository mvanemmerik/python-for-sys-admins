from re import M


my_list = [1, 2, 3, 4, 5,  6, 7, 8, 9, 10]
print(my_list)
print(my_list[1])
print(my_list[-1]) # last item in list
print(len(my_list))
print(my_list[0:2]) # slices
print(my_list[:3]) 
print(my_list[1:]) 
print(my_list[1::2]) # with step value
my_list[0] = 11
print(my_list)
print(my_list*2)

my_list.append(12)  # add to list
my_list.append(13)
print(my_list)

my_list  += [14, 15, 16]
print(my_list)

my_list[0:2] = ['a', 'b', 'c', 'd']
print(my_list)

my_list[4:]  = [] # replace part of list with empty list
print(my_list)

my_list.remove('b') # remove item placed on value
print(my_list)

pop_item = my_list.pop() #  remove last item from list
print(my_list)
print(pop_item)

my_list.pop(0) # specify which item to pop
print(my_list)
