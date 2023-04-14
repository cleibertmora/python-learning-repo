# functions in python

# function definition
def function_name():
    print("hello world")

# function call
function_name()

# function with arguments
def function_name(name):
    print("hello " + name)

# function call
function_name("john")

# function with return value
def function_name(name):
    return "hello " + name

# function call
print(function_name("john"))

# function with default argument
def function_name(name="john"):
    return "hello " + name

# function call
print(function_name())

# function with variable number of arguments
def function_name(*names):
    for name in names:
        print("hello " + name)

# function call
function_name("john", "jane", "joe")

# function with variable number of keyword arguments
def function_name(**names):
    for name in names:
        print("hello " + names[name])

# function call
function_name(john="john", jane="jane", joe="joe")

# function with variable number of arguments and keyword arguments
def function_name(*names, **names2):
    for name in names:
        print("hello " + name)
    for name in names2:
        print("hello " + names2[name])

# function call
function_name("john", "jane", "joe", john="john", jane="jane", joe="joe")

# function with variable number of arguments 
# and keyword arguments and default arguments

x = 10

def my_function():
    global x
    x += 5
    print(x)

my_function()  # Output: 15
