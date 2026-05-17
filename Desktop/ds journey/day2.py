name = input("Enter your name: ")

# Way 1 - Using + (concatenation)
print("Hello, " + name + "! Welcome to Python.")

# Way 2 - Using f-string (most modern & recommended)
print(f"Hello, {name}! Welcome to Python.")

# Way 3 - Using .format()
print("Hello, {}! Welcome to Python.".format(name))
