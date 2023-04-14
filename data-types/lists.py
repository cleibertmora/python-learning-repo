# lists in python are mutable
# lists in python are ordered
# lists in python are indexed
# lists in python are iterable
# lists in python are dynamic
# lists in python are heterogeneous

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# access the first element
print(x[0])

# access the last element
print(x[-1])

# access the first 5 elements
print(x[0:5])

# access the last 5 elements
print(x[-5:])

# list of strings
names = ["John", "Jane", "Doe"]

# list of mixed data types
mixed = [1, "John", 2.5, True]

# list of lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# list methods
# append
x.append(11)
x.append(3)
print(x)

# insert
x.insert(0, "item") # insert at index 0
print(x)

# extend
x.extend([12, 13, 14])
print(x)

# remove
x.remove("item")
print(x)

# pop
x.pop() # remove last element
print(x)

# pop
x.pop(0) # remove first element
print(x)

# clear
#x.clear()
#print(x)

# index
# returns the index of the first occurence of the element
print(x.index(3))

# count
# returns the number of occurences of the element
print(x.count(3))

# sort
# sorts the list in ascending order
x.sort()
print(x)

# reverse
# reverses the list
x.reverse()
print(x)

# copy
# returns a shallow copy of the list
y = x.copy()
print(y)

# list comprehension
# creates a new list based on the existing list
# syntax: [expression for item in list]
# syntax: [expression for item in list if condition]
# syntax: [expression if condition else expression for item in list]
# syntax: [expression for item1 in list1 for item2 in list2]

# create a list of squares of numbers from 1 to 10
squares = [i**2 for i in range(1, 11)]
print(squares)

# create a list of squares of even numbers from 1 to 10
squares = [i**2 for i in range(1, 11) if i % 2 == 0]

# create a list of squares of even numbers from 1 to 10
# if the number is even, then the square is even
# if the number is odd, then the square is odd
squares = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]

# iterate over a list
# create a list of squares of numbers from 1 to 10
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# iterate over a list
# create a list of squares of even numbers from 1 to 10
squares = []
for i in range(1, 11):
    if i % 2 == 0:
        squares.append(i**2)

# iterate over a list with while loop
# create a list of squares of numbers from 1 to 10
squares = []
i = 1
while i <= 10:
    squares.append(i**2)
    i += 1
print(squares)



# iterate over two lists
# create a list of products of corresponding elements
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
products = [i * j for i in list1 for j in list2]
print(products)