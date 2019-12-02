#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: Dec 2019
# This program uses an array

import random


def main():
    # this function uses an array

    random_numbers = []
    average = 0
    # input
    for loop_counter in range(0, 9+1):
        random_number = random.randint(0, 100)
        random_numbers.append(random_number)
    print("")

    print("Here are the numbers:")

    for loop_counter in range(0, 9+1):
        print("{0} ".format(random_numbers[loop_counter]), end="")

    print("")

    print("Here is the average")

    for loop_counter in range(0, 9+1):
        average = random_numbers[loop_counter] + average
    average = (average/10)
    print("{0}".format(average))


if __name__ == "__main__":
    main()
