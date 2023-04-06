# Ternary Operator Examples
x = 5

# Assign a value based on a condition
y = "positive" if x > 0 else "non-positive"
print(y)

# Assign a value based on two conditions
z = "even" if x % 2 == 0 else "odd" if x % 3 == 0 else "neither"
print(z)

# Execute an action based on a condition
result = True if x > 0 else False
print("x is positive" if result else "x is non-positive")