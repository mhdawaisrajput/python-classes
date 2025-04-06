
# Print Hello World

print ("Hello World!")

###############################################################################


# List

sehar_items: list[str] = ["Paratha", "Chai", "Dahi", "Sabzi", "Pheni"]
sehar_items.pop(1)
sehar_items.append("Pani Puri")
sehar_items.insert(1, "Chicken")
sehar_items.remove("Chicken")

print(sehar_items)


###############################################################################


# Tuple => Immutable / Ordered / Indexed

iftar_items: tuple[str] = ("Pakorey", "Dahi Balley", "Samosay")
print(iftar_items)


###############################################################################



# A regular set is unordered, mutable, unchangable and holds only unique elements.
iftar_items: set = {"Pakoray", "Khujoor", "Rooh Afza", "Fruit chat", "Rooh Afza", "Pakoray"}
# Even though duplicates are provided, they are stored only once.

# Adding a new element. Note that "Fruit Chat" (with capital 'C') is considered different from "Fruit chat".
iftar_items.add("Fruit Chat")
# Removing an element.
iftar_items.remove("Fruit chat")

# Display the type of the regular set
print("Type of iftar_items:", type(iftar_items))

# A frozenset is an immutable version of a set. Once created, you cannot add or remove items.
iftar_items_frozen_set: frozenset = frozenset(iftar_items)

# Display the type of the frozenset
print("Type of iftar_items_frozen_set:", type(iftar_items_frozen_set))

# Attempting to add an element to the frozenset would raise an error:
# iftar_items_frozen_set.add("Dahi Baray")  # Uncommenting this will cause an AttributeError


###############################################################################


# Input

num1: int = input("Enter Your Number:")
sum: int = 10 + int(num1)
print(sum)


###############################################################################


# Conversions of Data Types

# List to Tuple
sehar_items: list = ["Paratha", "Chai", "Lassi", "Pani", "Pheni", "Chai", "Lassi"]
converted_sehar_items: tuple = tuple(sehar_items)
print(converted_sehar_items)

# Tuple to List
iftar_items: tuple = ("Pakorey", "Dahi Balley", "Samosay")
converted_iftar_items: list = list(iftar_items)
print(converted_iftar_items)

# List to Set
sehar_items: list = ["Paratha", "Chai", "Lassi", "Pani", "Pheni", "Chai", "Lassi"]
converted_sehar_items: set = set(sehar_items)
print(converted_sehar_items)

# Set to List
iftar_items: set = {"Pakorey", "Dahi Balley", "Samosay"}
converted_iftar_items: list = list(iftar_items)
print(converted_iftar_items)


###################################################################################


# Addition of two numbers using input from user 

num1: int = 10
num2 : float = 3.5
sum = num1 + num2
print(type(sum))


###################################################################################


# Type Casting => Convert one data type to another data type


# 1. Implicit Type Casting (Done Automatically by Python)
# Python automatically converts data types when needed, without your intervention.

num1 : int = 10
num2: int = 2
sum = num1 / num2
print(type(sum))     # float

# 💡 Explanation:
# You divided two int values.
# Python automatically converted the result to a float because / always returns a float.
# This is implicit type casting.


# 2. Explicit Type Casting (Done by Developer)
# Developer converts data types manually using built-in functions.

num = "10"
print(type(num))
print(type(int(num)))       # Convert string to int
print(type(float(num)))     # Convert string to float

# 💡 Explanation:
# You converted a string to an int using int() function. or float() function.
# The result is an int or float.


###################################################################################


# import math module and random module

import math
from math import sqrt
import random

print(sqrt(16))   # Square Root of 16 = 4
print(random.randint(1, 10))   # Random Number between 1 and 10


###################################################################################

# import requests module

# !pip install requests => This is used in Jupyter Notebooks or Google Colab.
# pip install requests => This is used in the command line (terminal) or Python environment.

import requests

response = requests.get("https://api.github.com")
print(response.status_code)


###################################################################################


# 🔑 Function with Simple Parameter
# This function just takes a name and prints a greeting directly
def My_Intro(name: str) -> str:
    print(f"Hello {name} How are you?")
My_Intro("Muhammad Awais")



# 🥪 Function: Prints Directly (Void Function)
# 🔑 This function prints the sandwich message directly and doesn't return any value
def Sandwich(name: str, bread: str, filing: str) -> str:
    print(f"{name} Your Sandwich with {bread} bread and {filing} filling is ready!")
Sandwich("Ali:", "Garlic", "Beef Patty")



# 🥪 Function: Returns a String (Return Function)
# 🔑 This version returns the sandwich description, allowing reuse or manipulation later.
def Sandwich(bread: str, filling: str) -> str:
    sandwich_bread = f"{bread} bread"
    sandwich_filling = f"{filling} filling"
    complete_sandwich = f"Your Sandwich with {sandwich_bread} and {sandwich_filling} is ready!"
    return complete_sandwich
    

# 🔑 The result is stored and then printed (more flexible)
ali = Sandwich("Garlic", "Beef Patty")
print("Ali:", ali)

bilal = Sandwich("Simple", "Chicken Patty")
print("Bilal:", bilal)


# This means that whenever Bilal calls this function again,
# the function will execute and return a new sandwich description,
# so you don't have to create a separate variable every time.



# 🔑 Function with Positional and Keyword Arguments
def Name(first_name: str, last_name: str) -> str:
    # Prints a greeting using the provided first and last names.
    print(f"Hello {first_name} {last_name}")

# 💡 Positional arguments: values are assigned based on the order of parameters in the function definition.
Name("Muhammad", "Waqas")
# Here, "Muhammad" is assigned to first_name and "Waqas" to last_name.
# Output: Hello Muhammad Waqas

# 💡 Keyword arguments: values are assigned based on the parameter names, regardless of their order.
Name(last_name="Ali", first_name="Muhammad")
# Here, "last_name" is assigned to "Ali" and "first_name" to "Muhammad".
# Output: Hello Muhammad Ali