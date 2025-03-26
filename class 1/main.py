##############################################################################################################################
##############################################################################################################################
########################################### Saturday Class Sir Ali Aftab: ####################################################
##############################################################################################################################
##############################################################################################################################

print("########################################### Saturday Class Sir Ali Aftab: ###########################################\n")

# Topic 1:
print("Hello, World!")  # Output: Hello, World!

# Topic 2:
full_name = "Muhammad Awais"
print(type(full_name))  # <class 'str'>

# Topic 3:
any_number: int = 20
print(type(any_number))  # <class 'int'>

# Topic 4:
any_float: float = 20.5
print(type(any_float))  # <class 'float'>

# Topic 5:
any_boolean: bool = True
print(type(any_boolean))  # <class 'bool'>

# Topic 6:
first_name: str = "Muhammad"
last_name: str = "Awais"
full_name: str = first_name + " " + last_name
print(full_name)  # Output: Muhammad Awais

# Topic 7:
first_name: str = "Muhammad"
last_name: str = "Awais"
full_name: str = f"{first_name} {last_name}"  # f-string
print(full_name)  # Output: Muhammad Awais

# Topic 8:
achievement: str = """Thrilled to 
share i am passing quarter 3
exam"""
print(achievement)  # (f """ it is used to write multi-line string """) this is called doc-string

# Topic 9:
quarter: str = "Q3"
achievement: str = f"""Thrilled to
share i am passing {quarter}
exam"""
print(achievement)

# Topic 10:
quarter: str = "Q3"
achievement: str = f"""Thrilled to
share i am passing {quarter}
exam"""
print(id(achievement))  # output: 2147483648 unique id for each time we run the code

# Topic 11:
fruits = ["apple", "banana", "cherry"]
print(fruits[0: 2])  # output: ['apple', 'banana']
print("\n")


# Home-Work
# 1. Assignment 1: Modern AI Python Steps  
    #  Complete the first seven steps of Sir Zia's repository: 
    # https://github.com/panaversity/learn-modern-ai-python/


# 2. Assignment 2: Growth Mindset Challenge ✅ 
    # Review and complete the Growth Mindset Challenge:  
    # https://github.com/panaversity/learn-modern-ai-python/blob/main/Growth_Mindset_Challenge.md


# 3. Assignment 3: Python Operators (is vs in) ✅ 
    # Research and explain the difference between the is and in operators in Python. Provide examples to demonstrate their usage.

    # is operator:
    # fruits = ["Apple", "Banana", "Mango", "Orange"]
    # print("Apple" in fruits)        # output: True bcz Apple is in the list.
    # print("Apple" not in fruits)    # output: False bcz Apple is in the list.

    # in operator:
    # num1 = 10
    # num2 = 3
    # print(num1 is num2)    # output: False bcz num1 and num2 are not the same.
    #print(num1 is not num2)    # output: True bcz num1 and num2 are not the same.


# 4. Assignment 4: Agentic AI Presentation 
    # Prepare a presentation on the topic of Agentic AI.



##############################################################################################################################
##############################################################################################################################
########################################### Friday Class Sir Hamzah Syed: ####################################################
##############################################################################################################################
##############################################################################################################################



print("######################################### Friday Class Sir Hamzah Syed: ############################################\n")


# Topic 1:  ( simple print function. )


print("Hello World!")
# Terminal Command: python file-name.py likewise:  python main.py
# Output: Hello World!



# Topic 2: ( variables in python with data types + id() function  + type() function )

first_name: str = "Awais"       # str is a data type for string
print(first_name)
print(type(first_name))         # output: <class 'str'>
print(id(first_name))          # output: 2147483648 unique id for each time we run the code


height: float = 5.8             # float is a data type for decimal numbers
print(height)
print(type(height))             # output: <class 'float'>
print(id(height))               # output: 2147483648 unique id for each time we run the code


age: int = 25                   # int is a data type for integer numbers
print(age)
print(type(age))                # output: <class 'int'>
print(id(age))                  # output: 2147483648 unique id for each time we run the code


is_student: bool = True         # bool is a data type for boolean values
print(is_student)
print(type(is_student))         # output: <class 'bool'>
print(id(is_student))           # output: 2147483648 unique id for each time we run the code

####*******
first_name: str = 123           # yaha error nahi ayga bcz abhi developed nahi hai.
print(type(first_name))         # output: <class 'int'>
####*******



# Topic 3: ( concatenation of strings in simple way. )

first_name = "Muhammad"
last_name = "Awais"
print(first_name + " " + last_name)     # output: Muhammad Awais

full_name = first_name + " " + last_name
print(full_name)                        # output: Muhammad Awais



# Topic 4: ( concatenation of strings with the help of f-string )

first_name = "Muhammad"
last_name = "Awais"
print( f"{first_name} {last_name}" )    # output: Muhammad Awais




# Topic 5: ( line-break and tab like space in python with the help of \n, \t )

email = "Hi, Muhammad Awais \n How are you?"
print(email)         
# Hi, Muhammad Awais
#  How are you?

email = "Hi, Muhammad Awais \t How are you?"
print(email)         
# Hi, Muhammad Awais     How are you?




# Topic 6: ( Line Breaks in Python using Doc-Strings (""" """ / ''' ''') )

email = """Hi, Muhammad Awais
How are you?"""
print(email)         
#  Hi, Muhammad Awais
# How are you?

message =  '''Hi, Muhammad Awais
How are you?'''
print(message)
#  Hi, Muhammad Awais
# How are you?

# Or
name = "Muhammad Awais"
email = f"""Hi, {name}
How are you?"""
print(email)
#  Hi, Muhammad Awais
# How are you?



# Topic 7: ( list in python with square brackets )

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)   # output: ['Apple', 'Banana', 'Mango', 'Orange']




# Topic 8: ( list in python with square brackets and with different data types. )
data = ["Muhammad Awais", 25, 5.8, True]
print(data)   # output: ['Muhammad Awais', 25, 5.8, True]




# Topic 9: ( length of list with len() function. )

print(len(fruits))   # output: 4
print(len(data))     # output: 4


# Topic 10: ( access the elements of list with index number. )
print(fruits[0])    # output: Apple

print(fruits[1])     # output: Banana
print(fruits[-1])   # negative index number to access the elements from the end of list. output: Orange


print(fruits[2])     # output: Mango
print(fruits[-2])   # negative index number to access the elements from the end of list. output: Banana


print(fruits[3])     # output: Orange
print(fruits[-3])   # negative index number to access the elements from the end of list. output: Apple





# Topic 11: ( slicing of list with colon(:) operator. )


fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0:2])  # start index is inclusive and end index is exclusive. or 0 index se lekr 2 se phele tak. output: ['Apple', 'Banana']

print(fruits[1:3])  # 1 index se lekr 3 se phele tak. output: ['Banana', 'Mango']   

print(fruits[:3])   # start index is optional. output: ['Apple', 'Banana', 'Mango']

print(fruits[1:])   # end index is optional. output: ['Banana', 'Mango', 'Orange']

print(fruits[:])    # both start and end index are optional. output: ['Apple', 'Banana', 'Mango', 'Orange']


# Topic 12: ( Arithmetic Operators in python. +, -, *, /, %, **, // )

num1 = 10
num2 = 3

print(num1 + num2)  # Addition          # Output: 13 
print(num1 - num2)  # Subtraction       # Output: 7
print(num1 * num2)  # Multiplication    # Output: 30
print(num1 / num2)  # Division          # Output: 3.3333333333333335
print(num1 % num2)  # Modulus           # Output: 1
print(num1 ** num2) # Exponentiation    # Output: 1000
print(num1 // num2) # Floor Division    # Output: 3





# Topic 13: ( Comparison Operators in python. ==, !=, >, <, >=, <= )

num1 = 10
num2 = 3

print(num1 == num2) # Equal                     # Output: False
print(num1 != num2) # Not Equal                 # Output: True
print(num1 > num2)  # Greater than              # Output: True  
print(num1 < num2)  # Less than                 # Output: False

print(num1 >= num2) 
# Greater than or Equal         # Output: True      # if one of the condition is true then the output is true. like 10 is greater than 3.

print(num1 <= num2) # Less than or Equal        # Output: False 




# Topic 14: ( Logical Operators in python. and, or, not )

num1 = 10
num2 = 3

print(num1 > 5 and num2 < 5)
#        True   +    True = True     # Output: True


print(num1 > 5 or num2 < 1)
#        True   +    False = False     # Output: True     # if one of the condition is true then the output is true.


# print(num1 > 5 not num2 < 5) >>> Gives error. bcz not operator is not used in this way.

print(not(num1 > 5 and num2 < 5))
#        True   +    True = True     # Output: False    # not operator is used to reverse the condition.

print(not(num1 > 5 and num2 < 1))
#        True    +   False = False   # Output: True     # not operator is used to reverse the condition.




# Topic 15: ( Assignment Operators in python. =, +=, -=, *=, /=, %=, **=, //= )

num1 = 10
num2 = 3

# Addition Assignment Operator
num1 += num2
# num1 = num1(10) + num2(3)
print(num1)  # output: 13


# Subtraction Assignment Operator
num1 -= num2
# num1 = num1(13) - num2(3)
print(num1)  # output: 10


# Multiplication Assignment Operator
num1 *= num2
# num1 = num1(10) * num2(3)
print(num1)  # output: 30


# Division Assignment Operator
num1 /= num2
# num1 = num1(30) / num2(3)
print(num1)  # output: 10.0


# Modulus Assignment Operator
num1 %= num2
# num1 = num1(10.0) % num2(3)
print(num1)  # output: 1.0


# Exponentiation Assignment Operator
num1 **= num2
# num1 = num1(1.0) ** num2(3)
print(num1)  # output: 1


# Floor Division Assignment Operator
num1 //= num2
# num1 = num1(1) // num2(3)
print(num1)  # Output: 0.0




# Topic 16: ( Membership Operators in python. in, not in )


fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Apple" in fruits)        # output: True bcz Apple is in the list.

print("Apple" not in fruits)    # output: False bcz Apple is in the list.



# Topic 17: ( Identity Operators in python. is, is not )

num1 = 10
num2 = 3

print(num1 is num2)    # output: False bcz num1 and num2 are not the same.

print(num1 is not num2)    # output: True bcz num1 and num2 are not the same.




# Topic 18: ( Bitwise Operators in python. &, |, ^, ~, <<, >> )

num1 = 10  # Binary:  1010
num2 = 3   # Binary:  0011

# Bitwise AND
print(num1 & num2)     # output: 2

# Explaination:
# The bitwise AND (&) operator works by comparing each bit in the same position of two binary numbers. It follows this rule:
# 1 & 1 = 1
# 0 & 1 = 0
# 1 & 0 = 0
# 0 & 0 = 0

# 1010  (10)
# 0011  (3)
# ----  
# 0010  (2)  is come from 1010 and 0011.



# Bitwise OR 
print(num1 | num2)     # output: 11
    
# Explaination:
# The bitwise OR (|) operator works by comparing each bit in the same position of two binary numbers. It follows this rule:
# 1 | 1 = 1
# 0 | 1 = 1
# 1 | 0 = 1
# 0 | 0 = 0

# 1010  (10)
# 0011  (3)
# ----
# 1011  (11)  is come from 1010 and 0011.



# Bitwise XOR
print(num1 ^ num2)     # output: 9
    
# Explaination:
# The bitwise XOR (^) operator works by comparing each bit in the same position of two binary numbers. It follows this rule:
# 1 ^ 1 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 0 ^ 0 = 0

# 1010  (10)
# 0011  (3)
# ----
# 1001  (9)  is come from 1010 and 0011.




# Bitwise NOT
print(~num1)          # output: -11       

# Explaination:
# The bitwise NOT (~) operator works by inverting all the bits of a binary number. It follows this rule:
# ~1 = -2
# ~0 = -1

# 1010  (10)
# ----
# 0101  (-11)  is come from 1010. bcz ~1 = -2,  ~0 = -1.




# Bitwise Left Shift
print(num1 << num2)  # 10 << 3 = 80
# 1010  (10)
# ----
# 1010 + 000 = 1010000 (binary) = 80 (decimal)
# A left shift (<<) moves all bits to the left and fills the empty spaces with 0 on the right.

# Mathematical Formula

# Left shifting a number by n positions is equivalent to multiplying it by 2^n.
# num1 << num2 = num1 * 2^num2  ===>>>  10 << 3 =>>> 10 * 2^3 = 10 * 8 = 80


# Bitwise Right Shift
print(num1 >> num2)     #  10 >> 3 = 1
# ----
# 0001  (1)  is come from 1010. bcz 10 >> 3 = 1.

# Mathematical Formula
# Right shifting a number by n positions is equivalent to dividing it by 2^n.
# num1 >> num2 = num1 / 2^num2  ===>>>  10 >> 3 =>>> 10 / 2^3 = 10 / 8 = 1


# Decimal	        Binary
# 0	                0000
# 1	                0001
# 2	                0010
# 3	                0011
# 4	                0100
# 5	                0101
# 6	                0110
# 7	                0111
# 8	                1000
# 9	                1001


# Binary Addition       
# 1 & 0 →            0
# 0 & 0 →            0
# 1 & 1 →            1
# 0 & 1 →            0


# Binary Subtraction
# 1 & 0 →            0
# 0 & 0 →            0
# 1 & 1 →            1
# 0 & 1 →            0


# Binary Multiplication
# 1 & 0 →            0
# 0 & 0 →            0
# 1 & 1 →            1
# 0 & 1 →            0

# Binary Division
# 1 & 0 →            0
# 0 & 0 →            0
# 1 & 1 →            1
# 0 & 1 →            0

# Binary Modulus
# 1 & 0 →            0
# 0 & 0 →            0
# 1 & 1 →            1
# 0 & 1 →            0

# Binary Exponentiation
# 1 & 0 →            0
# 0 & 0 →            0
# 1 & 1 →            1
# 0 & 1 →            0