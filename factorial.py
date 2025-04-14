#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Apr 14, 2025
# This program calculates the factorials.


def main():
    # Ask the user for input
    user_num_string = input("Enter a number as positive integer: ")

    try:
        # Convert to an integer
        user_num = int(user_num_string)

        # if the user number is less than 0
        if user_num < 0:
            print("Please enter a positive integer.")
        else:
            # Set the counter and the initial product
            counter = 0
            product = 1

            # Do..while loop using True
            while True:
                counter = counter + 1
                product = product * counter

                # If the counter is greater than or equal to the user number.
                if counter >= user_num:
                    break
            # Print out the output
            print("The factorial of {}! is {}.".format(user_num, product))
    # Exception where try cast does not work because of an invalid input.
    except Exception:
        print("Invalid input. Please enter a non-negative whole number.")
