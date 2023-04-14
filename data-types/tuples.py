# Description: Tuples in Python
# A tuple is a collection which is ordered and unchangeable. 
# In Python tuples are written with round brackets.
my_tuple = (1, 2, 3)

# Accessing tuple items
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
print(my_tuple[2])  # Output: 3

# Slicing in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:3])  # Output: (2, 3)

# Negative indexing in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-1])  # Output: 5
print(my_tuple[-2])  # Output: 4

# Changing a tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 6  # This will raise an error
# Tuple items are unchangeable
# But you can change the tuple itself
# You can convert the tuple into a list, change the list, 
# and convert the list back into a tuple.

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list[0] = 6
my_tuple = tuple(my_list)

# Looping through a tuple
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)

# Checking if an item exists in a tuple
my_tuple = (1, 2, 3, 4, 5)
if 3 in my_tuple:
    print("3 is in the tuple")

# Tuple length
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5

# Adding items to a tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple.append(6)  # This will raise an error
# Tuples are unchangeable, so you cannot add items to it

# Removing items from a tuple
my_tuple = (1, 2, 3, 4, 5)
del my_tuple  # This will raise an error
# Tuples are unchangeable, so you cannot remove items from it

# Tuple methods
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(1))  # Output: 1
print(my_tuple.index(1))  # Output: 0

# Tuple constructor
my_tuple = tuple((1, 2, 3, 4, 5))
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Tuple unpacking
my_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Tuple unpacking with *
my_tuple = (1, 2, 3, 4, 5)
a, b, *c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3, 4, 5]

