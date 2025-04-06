"""
+----------------------------------------------------------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------------------------------------------------------+
|                                                   Sir Ali Aftab:                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------|
|                                                   Saturday Class:                                                                |
+----------------------------------------------------------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------------------------------------------------------+

"""

# Topic -1: (Use of byte string): It is a collection of bytes that are ordered and immutable. and it is used to store binary data.

byte_data: bytes = b"Hello World"
print(byte_data)                    # b'Hello World'     
print(byte_data[0])                 # 72                   
print(byte_data[0:5])               # b'Hello'
print(byte_data[6:])                # b'World'
print(byte_data[:5])                # b'Hello'
print(byte_data[-1])                # 100
print(byte_data[-5:])               # b'World'                   
print(byte_data[:-5])               # b'Hello'
print(byte_data[0:5:2])             # b'Hlo'
print(byte_data[::2])               # b'HloWrd'

"""+============================================================================================================================+"""

# Topic 0: (String methods)

message =  "Hello ,  World"
print(message.upper())              # HELLO ,  WORLD
print(message.lower())              # hello ,  world
print(message.count("l"))           # 3
print(message.find("l"))            # 2
print(message.find("z"))            # -1    bcz z is not present in the string. so it returns -1.
print(message.replace("World", "Universe"))  # Hello ,  Universe
print(message.replace(" ", ""))     # Hello,World
print(message.replace(",", ""))     # Hello  World
print(message.split())              # ['Hello', ',', 'World']
print(message.split(","))           # ['Hello ', '  World']

"""+============================================================================================================================+"""

# Topic 1: (split function)

my_sting: str = "Hello World"

modified_string: str = my_sting.split()   
print(modified_string)
# This will split the string into a list of words and return a list of words.
# output: ['Hello', 'World']

modified_string: str = my_sting.split("l")      # output: ['He', '', 'o Wor', 'd']
print(modified_string)

modified_string: str = my_sting.split("o")      # output: ['Hell', ' W', 'rld']
print(modified_string)

"""+============================================================================================================================+"""

# Topic 2: (replace function)

message: str = "Pakistan won all the matches of champions trophy!, Pakistan is the best team in the world!"
new_message: str = message.replace("Pakistan", "India")
print(new_message)  # output: India won all the matches of champions trophy!, India is the best team in the world!

"""+============================================================================================================================+"""

# Topic 3: (join function)
countries: str = " , "      # This is the separator between the countries 
joined_coutires: str = countries.join(["Pakistan", "India", "Afghanistan"])
print(joined_coutires)  # output: Pakistan , India , Afghanistan


# OR:

pak_team = ["Muhammad", "Awais", "Manzoor", "Hussain"]    

print(pak_team)               # output: ['Muhammad', 'Awais', 'Manzoor', 'Hussain']
print("".join(pak_team))      # output: MuhammadAwaisManzoorHussain
print(" ".join(pak_team))     # output: Muhammad Awais Manzoor Hussain
print(",".join(pak_team))     # output: Muhammad,Awais,Manzoor,Hussain
print(" , ".join(pak_team))   # output: Muhammad , Awais , Manzoor , Hussain
print(", ".join(pak_team))    # output: Muhammad, Awais, Manzoor, Hussain


"""+============================================================================================================================+"""

# Topic 4: (length function)

name: str = "Muhammad Awais"
print(len(name))  # output: 14

# OR:
length_of_name: int = len(name)
print(length_of_name)  # output: 14

"""+============================================================================================================================+"""

# Topic 5: (id/type function)

# id function:
name: str = "Muhammad Awais"
print(id(name))  # output: 2144160211376

# OR:
id_of_name: int = id(name)
print(id_of_name)  # output: 2144160211376

# Type function:
fruits: set = {"Mango", "Grapes", "Banana", "Mango"}
print(type(fruits))  # output: <class 'set'>

"""+============================================================================================================================+"""

# Topic 6: (Importing the sys module for system-specific functions)

import sys  # Importing the sys module to use sys.intern()

a = "hello"  # Assigning string "hello" to variable a
b = "world"  # Assigning string "world" to variable b
c = "helloworld"  # Normal string assignment (creates a new string)

d = sys.intern(a + b)  # Forces Python to store "helloworld" in a shared memory pool

print(c is d)  # Checks if c and d refer to the same memory location, output: True


# OR:

# Exploring sys functions
print(sys.getsizeof(c))  # Returns memory size of c in bytes        # output: 51
print(sys.getsizeof(d))  # Returns memory size of d in bytes        # output: 51

print(sys.version)  # Prints Python version being used                  # output: 3.13.2
print(sys.platform)  # Prints OS platform (e.g., 'win32', 'linux')      # output: win32

print(sys.intern("Python") is sys.intern("Python"))  # Demonstrates interning works globally

# What Happens?
# sys.intern("Python") → Python stores "Python" in a special interned string pool.
# sys.intern("Python") (again) → Instead of creating a new string, Python reuses the same one.
# is checks if both refer to the same memory location.
# ✅ Output is True because "Python" is stored only once in memory.


print(sys.intern("Python") is sys.intern("Javascript"))  # Demonstrates interning works globally  
# output: False

"""+============================================================================================================================+"""

# Topic 7: (dir() is a built-in function in Python that returns a list of attributes (methods & properties) of the class.)

get_string_methods: str = dir(str)   # dir(str): Returns a list of all attributes (methods & properties) of the str class.
print(get_string_methods)

# Explaination:

# 🔹 Output Includes:
# Special dunder methods (e.g., __len__, __add__, __str__, etc.)
# Standard string manipulation methods (e.g., isalnum, lower, replace, split, etc.)

# output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


isalnum_method: str = "isalnum"
print(isalnum_method in get_string_methods)  # output: True bcz isalnum is a method of the str class.


###### Filtering Out Dunder Methods ######
get_string_methods: str = dir(str)
filtered_methods: str = [method for method in get_string_methods if not method.startswith("__")]
print(filtered_methods)

# Explaination:

# This list comprehension removes all dunder methods (methods starting with "__").
# The result is a list of only useful string methods.

# output: ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


###### Filtering Out Standard string manipulation methods ######
string_methods = dir(str)
dunder_methods = [method for method in string_methods if method.startswith("__")]
print(dunder_methods)

# Explaination:

# This list comprehension removes all standard string manipulation methods (methods starting with "__").

# output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

"""+============================================================================================================================+"""

# Topic 8: (List[]): It is a collection of items that are ordered and mutable.

fruits: list[str] = ["apple", "banana", "cherry", "date", "elderberry"]

# 1. using the Slice method: it returns a new list of the specified elements

print(fruits[1:3])  # output: ['banana', 'cherry']

# 2. using the append method: it adds the item to the end of the list

fruits.append("Orange" )
fruits.append("Pineapple")
fruits.append("Kiwi")

print(fruits)  # output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'Orange', 'Pineapple', 'Kiwi']

# 3. using the insert method: it adds the item to the specified index

fruits.insert(0, "Mango")
print(fruits)  # output: ['Mango', 'apple', 'banana', 'cherry', 'date', 'elderberry', 'Orange', 'Pineapple', 'Kiwi']

# 4. using the remove method: it removes the first item with the specified value

fruits.remove("apple")
print(fruits)  # output: ['Mango', 'banana', 'cherry', 'date', 'elderberry', 'Orange', 'Pineapple', 'Kiwi']

# 5. using the pop method:

fruits.pop()    # It removes the last item from the list
print(fruits)  # output: ['Mango', 'banana', 'cherry', 'date', 'elderberry', 'Orange', 'Pineapple']

fruits.pop(2)  # It removes the item present at index 2.
print(fruits)  # output: ['Mango', 'banana', 'date', 'elderberry', 'Orange', 'Pineapple']

# 6. using the clear method: it removes all items from the list

fruits.clear()
print(fruits)  # output: []


# 7. using the del keyword: it deletes the list completely

del fruits
# print(fruits)  # output: NameError: name 'fruits' is not defined

"""+============================================================================================================================+"""

# Topic 9: (dictionary): Its work like a key value pair(object). but in dic key is in double quotes.

person: dict = {
    "name": "Muhammad Awais",
    "age": 23,
    "country": "Pakistan",
    "city": {
        "phone": 1234567890,
        "email": "awais@gmail.com",
    }
}

person["name"]                              # Accessing the value of the key "name"  and output: Muhammad Awais
print(person["name"])                       # output: Muhammad Awais
print(person["city"]["phone"])              # output: 1234567890 

print(person.get("name"))                   # output: Muhammad Awais
print(person.get("city").get("phone")) 

"""+============================================================================================================================+"""

# Topic 10: (random module): It is a module that provides various functions to generate random numbers and perform other random operations.


# Part-A (random module)
import random
bobzi_runs = random.randint(0,10)
print(bobzi_runs)


# Part-B (if and else statement using random module)
import random

babar_score: int = random.randint(0, 120)

if (babar_score > 100):
    print("👑 King")
else:
    print("🔔 King")

print(babar_score)


# Part-C: (if and else statement using random module and (and) operator)

bobzi_runs = random.randint(0, 150)
ball_faced = 80
print(bobzi_runs)

if (bobzi_runs >= 100 and ball_faced < bobzi_runs):
  #               True      True   =  King Print
    print("🤴 King")
else:
    print("🔔 King")



"""+============================================================================================================================+"""

# Topic 11: ( List[] ): It is a collection of items that are ordered and mutable.

team_players: list = ["Babar Azam", "Shadab Khan", "Shaheen Shah", "Mohammad Rizwan"]

team_players[1] = "Hasan Ali"  # That,s why list is mutable.

print(team_players)  # output: ['Babar Azam', 'Hasan Ali', 'Shaheen Shah', 'Mohammad Rizwan']

"""+============================================================================================================================+"""

# Topic 12: ( Tuple() ): It is a collection of items that are ordered and immutable.

team_players: tuple = ("Babar Azam", "Shadab Khan", "Shaheen Shah", "Mohammad Rizwan")

# team_players[1] = "Hasan Ali"         # gives an error bcz tuple is immutable.
# team_players.append("Hasan Ali")      # give an error bcz tuple is immutable.

print(team_players)  # output: ('Babar Azam', 'Shadab Khan', 'Shaheen Shah', 'Hasan Ali', 'Mohammad Rizwan')

"""+============================================================================================================================+"""

# Topic 13: Set{} 
# A set is a collection of items that is unordered, unindexed, mutable, and does not allow duplicate values.

# ---------------------------
# Example 1: Basic Operations on a Set
# ---------------------------
team_players = {"Babar Azam", "Shadab Khan", "Shaheen Shah", "Mohammad Rizwan"}

# Adding a new element
team_players.add("Asad Shafiq")      # Adds "Asad Shafiq" to the set

# Removing elements
team_players.remove("Babar Azam")     # Removes "Babar Azam"; raises an error if not found
team_players.discard("Shadab Khan")   # Removes "Shadab Khan"; does nothing if not found

print("After add/remove/discard operations:", team_players)


# ---------------------------
# Example 2: Updating a Set
# ---------------------------
# Reinitialize the set for clarity:
team_players = {"Babar Azam", "Shadab Khan", "Shaheen Shah", "Mohammad Rizwan"}

# Note: Modifying an element by index is not allowed because sets are unordered and unindexed.
# The following line would raise an error:
# team_players[1] = "Hasan Ali"  

# To add multiple elements, use update(). Note:
# Using update() with a string iterates over each character, so pass a list instead.

# Incorrect: team_players.update("Shoaib Akhtar")
# This would add individual characters instead of the whole string.

# Correct usage:
team_players.update(["Shoaib Akhtar"])  
# You can also add multiple new elements at once:
team_players.update(["Shoaib Akhtar", "Asad Shafiq"])  # Duplicates will be ignored

print("After update operations:", team_players)


# OR
value: set = {0, 1, 2, 4, 1, 2}
print(value)

# OR:
value: set = set([0, 1, 2, 4, 1, 2])
print(value)

"""+============================================================================================================================+"""

"""
Comparison Table: List vs Tuple vs Set (Vertical Format)

Feature: Definition
  - List  : Ordered collection of items that is mutable.
  - Tuple : Ordered collection of items that is immutable.
  - Set   : Unordered, unindexed collection that is mutable and does not allow duplicate values.

Feature: Syntax
  - List  : [...]
  - Tuple : (...)
  - Set   : {...} or set([...])

Feature: Mutability
  - List  : Mutable: Items can be modified.
  - Tuple : Immutable: Items cannot be changed.
  - Set   : Mutable: Items can be added or removed.

Feature: Indexing
  - List  : Supports indexing and slicing.
  - Tuple : Supports indexing and slicing.
  - Set   : Does NOT support indexing due to unordered nature.

Feature: Duplicate Values
  - List  : Allows duplicates.
  - Tuple : Allows duplicates.
  - Set   : Does NOT allow duplicate values.

Feature: Common Methods
  - List  : append(), insert(), pop(), etc.
  - Tuple : (Read-only; no methods for modification.)
  - Set   : add(), remove(), discard(), update(), etc.

"""