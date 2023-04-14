# dictonaries in python are like hash tables in other languages
# or objects in javascript and PHP
# they are key value pairs

# Create a dictionary
d = {'x': 10, 'y': 20}

# Show
print(d['x'])  # Output: 10

# Add a value
d['z'] = 30

# Show
print(d['z'])  # Output: 30

# Remove a key
del d['x']

# Show
print(d)  # Output: {'y': 20, 'z': 30}

# the keys of a dictionary can be any immutable type
# strings, numbers, tuples
# the values can be any type

# Create a dictionary
d = {'x': 10, 'y': 20, 'z': 30}

# Iterate over dictionary
for k, v in d.items():
    print(k, 'corresponds to', v)
# Output:
# x corresponds to 10
# y corresponds to 20
# z corresponds to 30

# Iterate over dictionary keys
for k in d:
    print(k)
# Output:
# x
# y
# z

# Iterate over dictionary values
for v in d.values():
    print(v)
# Output:
# 10
# 20
# 30

# Dictionary methods
# Method	Description
# clear()	Removes all items from the dictionary
# copy()	Returns a shallow copy of the dictionary
# fromkeys()	Returns a new dictionary with keys from seq and values set to value
# get()	Retrieves a key value pair or default if key is not found
# has_key()	Returns true if key in dictionary, false otherwise
# items()	Returns a list of dictionary's (key, value) tuple pairs
# keys()	Returns a list of dictionary keys
# pop()	Removes and returns an element from a dictionary having the given key
# popitem()	Removes and returns an arbitrary element (key, value) from the dictionary
# setdefault()	Returns the given key value if present in the dictionary. If not, inserts the key with a value to the dictionary
# update()	Updates the dictionary with the key value pairs from other, overwriting existing keys
# values()	Returns a list of dictionary values

# Converting a dictionary in a json string
import json

# Create a dictionary
d = {'x': 10, 'y': 20, 'z': 30}

# Convert to json
json.dumps(d)  # Output: '{"y": 20, "x": 10, "z": 30}'
# json.dumps() converts a dictionary to a json string

# Converting a json string in a dictionary

# Create a json string
json_string = '{"y": 20, "x": 10, "z": 30}'
# json.loads() converts a json string to a dictionary
# Convert to dictionary
d = json.loads(json_string)



