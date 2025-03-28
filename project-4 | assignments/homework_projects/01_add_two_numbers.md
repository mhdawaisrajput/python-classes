# Python Program to Add Two Numbers

## Overview

This Python program takes two integer inputs from the user and calculates their sum. The program performs the following tasks:

- Prompts the user to enter the first number.
- Reads the input and converts it to an integer.
- Prompts the user to enter the second number.
- Reads the input and converts it to an integer.
- Calculates the sum of the two numbers.
- Prints the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the `main()` function guides the user through the process of entering two numbers and displays their sum.

---

## Solution Code

# This function is used to add two numbers.
def add_two_numbers():
    # Prints a message to inform the user about the program's purpose.
    print("This Program helps you add two numbers.")

    # Prompting the user to enter the first number as a string.
    first_number : str = input("Enter first your number: ")

    # Converting the user input from a string to an integer.
    first_number: int = int(first_number)

    # Prompting the user to enter the second number as a string.
    second_number : str = input("Enter your second number:")

    # Converting the second input from a string to an integer.
    second_number: int = int(second_number)

    # Adding the two integers and storing the result in the variable 'sum_of_numbers'.
    sum_of_numbers : int = first_number + second_number

    # Printing the sum of the two numbers in a formatted sentence.
    print(f"{first_number} + {second_number} = {sum_of_numbers}")

# This line ensures that the add_two_numbers() function is executed 
# only when the script is run directly, not when imported as a module.
if __name__ == "__main__":
    add_two_numbers()
