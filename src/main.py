# RANDOM NUMBER GENERATOR IN PYTHON

import random


class Gen:
    def random_number_generator():

        # Ask user for number ranges
        num1 = int(input("Enter first number range: "))
        num2 = int(input("Enter second number range: "))

        # If num2 is less than num1 then throw an error
        if num2 < num1:
            raise Exception("Second number must be greated than first number")

        # Print out the random number
        print(random.randint(num1, num2))


if __name__ == "__main__":
    Gen.random_number_generator()
