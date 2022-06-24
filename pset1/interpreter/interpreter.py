"""
Interpreter: evaluate expressions
"""

# Prompt user for expression
expression = input("Expression: ")

# Determine expression components
components = expression.split(" ")
x = int(components[0])
y = components[1]
z = int(components[2])

# Evaluate expression
if y == "+":
    print('{0:3.1f}'.format(x + z))
elif y == "-":
    print('{0:3.1f}'.format(x - z))
elif y == "*":
    print('{0:3.1f}'.format(x * z))
else:
    print('{0:3.1f}'.format(x / z))
