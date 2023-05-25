# package Code:
# my_package/my_module.py

def greeting(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

# main.py

from my_package import my_module

my_module.greeting("Alice")
my_module.farewell("Bob")


# modules code

# my_module.py

def greeting(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

# main.py

import my_module

my_module.greeting("Alice")
my_module.farewell("Bob")



