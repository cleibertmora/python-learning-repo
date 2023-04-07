# strigns in python
x = "Hello World"
name = 'John Doe'

# access the first character
print(x[0])

# access the last character
print(x[-1])

# access the first 5 characters
print(x[0:5])

# access the last 5 characters
print(x[-5:])

# string methods
message = " Hello, world! "
#print(message.strip())      # Output: "Hello, world!"
#print(message.lower())      # Output: " hello, world! "
#print(message.upper())      # Output: " HELLO, WORLD! "
#print(message.replace(",", ";"))  # Output: " Hello; world! "


# string concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
#print(full_name)

# string formatting
age = 36
txt = "My name is {}, and I am {}"
#print(txt.format(first_name, age))

# string formatting with f-strings
txt = f"My name is {first_name}, and I am {age}"
#print(txt)

# string formatting with placeholders
txt = "My name is %s, and I am %d"
#print(txt % (first_name, age))

# string formatting with placeholders
txt = "My name is {0}, and I am {1}"
#print(txt.format(first_name, age))

# string formatting with placeholders
txt = "My name is {name}, and I am {age}"
#print(txt.format(name=first_name, age=age))

# escape characters
txt = "We are the so-called \"Vikings\" from the north."
#print(txt)

# string methods
txt = "Hello, welcome to my world."
x = txt.capitalize()

txt = "Hello, welcome to my world."
x = txt.casefold()

txt = "banana"
x = txt.center(20)

txt = "Hello, welcome to my world."
x = txt.count("e")

txt = "Hello, welcome to my world."
x = txt.encode()

txt = "Hello, welcome to my world."
x = txt.endswith(".")

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)

txt = "Hello, welcome to my world."
x = txt.find("welcome")

txt = "For only {price:.2f} dollars!"
#print(txt.format(price = 49))

txt = "Hello, welcome to my world."
x = txt.index("e")

txt = "Company12"
x = txt.isalnum()

txt = "CompanyX"
x = txt.isalpha()

txt = "50800"
x = txt.isdecimal()

txt = "Demo"
x = txt.isdigit()

txt = "565543"
x = txt.isnumeric()

txt = "Demo"
x = txt.isidentifier()
print(x)

txt = "Hello world!"
x = txt.islower()

txt = "   "
x = txt.isspace()

txt = "Hello World!"
x = txt.istitle()
# print(x)

txt = "THIS IS NOW!"
x = txt.isupper()
# print(x)

txt = ("apple", "banana", "cherry")
x = ", ".join(txt)
#print(x)

txt = "Hello, welcome to my world."
x = txt.ljust(20)
# print(x)

txt = "Hello, welcome to my world."
x = txt.rjust(20)

txt = "Hello, welcome to my world."
x = txt.lower()

