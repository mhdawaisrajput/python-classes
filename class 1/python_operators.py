
# 1. is Operator (Identity Operator):
# The is operator is used to compare the identity of two objects. It checks whether two variables refer to the same memory location.

num1 = 10
num2 = 10
print(num1 is num2) # output: True

# OR:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True → Both refer to the same object in memory
print(a is c)  # False → Different objects with the same value




# 2. is not Operator (Identity Operator):
# The is not operator is used to compare the identity of two objects. It checks whether two variables refer to different memory locations.

num1 = 10
num2 = 20
print(num1 is not num2) # output: True

# OR:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is not b)  # False → Both refer to the same object in memory
print(a is not c)  # True → Different objects with the same value




# 3. in Operator (Membership Operator):
# The in operator checks whether a value exists within an iterable (e.g., list, tuple, string, dictionary keys).

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Apple" in fruits)  # True → "Apple" is in the list
print("Grapes" in fruits)  # False → "Grapes" is not in the list




# 4. not in Operator (Membership Operator):
# The not in operator checks whether a value does not exist within an iterable.

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Apple" not in fruits)  # False → "Apple" is in the list
print("Grapes" not in fruits)  # True → "Grapes" is not in the list