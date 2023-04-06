# String Formatting in Python
name = "Alice"
age = 30
height = 1.65

# Using format()
message = "My name is {} and I am {} years old. My height is {:.2f} meters.".format(name, age, height)
print(message)

# Using f-strings
message = f"My name is {name} and I am {age} years old. My height is {height:.2f} meters."
print(message)

"""
The format specifier :.2f is used to format a number
as a floating-point value with two decimal places 
after the decimal point.
"""