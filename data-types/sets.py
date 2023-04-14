# Sets in Python are unordered collections of unique elements. 
# We can construct them by using the set() function.

# Create a set
x = set()
# Add elements to a set
x.add(1)
# Add a different element
x.add(2)
# Try to add the same element
x.add(1)
# Show
print(x)  # Output: {1, 2}

# Create a list with repeats
l = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
# Cast as set to get unique values
print(set(l))  # Output: {1, 2, 3}

# Remove element from set
x = set([1, 2, 3])
x.remove(1)

# Show
print(x)  # Output: {2, 3}

# We can also perform mathematical set operations like union, 
# intersection, difference etc.

# Create two sets
a = set([1, 2, 3, 4, 5, 6])
b = set([4, 5, 6, 7, 8, 9])

# Union
print(a | b)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Intersection
print(a & b)  # Output: {4, 5, 6}

# Difference
print(a - b)  # Output: {1, 2, 3}

# Symmetric Difference
print(a ^ b)  # Output: {1, 2, 3, 7, 8, 9}

# Sets methods
# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# pop()	Removes and returns an arbitary set element. Raise KeyError if the set is empty
# remove()	Removes an element from the set. If the element is not a member, raise a KeyError
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
# union()	Return the union of sets in a new set
# update()	Update the set with the union of this set and others

# Frozen Sets
# Frozen sets have the characteristics of sets, 
# but we cannot be changed.

# Create a set  
s = frozenset([1, 2, 3, 4])
# Try to add an element
s.add(5)  # Output: AttributeError: 'frozenset' object has no attribute 'add'

# We use them when we have to make sure that the elements 
# of a set remain the same.

# Create a set
s = frozenset([1, 2, 3, 4])
# Use it as a key for a dictionary
d = {s: 'Hello'}
# Show
print(d[s])  # Output: Hello
