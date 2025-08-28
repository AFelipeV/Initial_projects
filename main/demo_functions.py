from utils import math_utils
import sys

"""Script to import and use functions from math_utils.py"""
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def input_number_list():
    raw = input("Enter a list of numbers separeted by commas: ")
    try:
        return [float(x) if '.' in x else int(x) for x in raw.split(',')]
    except ValueError:
        print("The list can only contain numbers separated by commas.")
        return input_number_list()


def collect_numbers():
    x = int(input("Enter the number of values to add: "))
    values = []
    for i in range(x):
        value = float(input("Enter a number: "))
        values.append(value)
    return values


print("Options:")
try:
    while True:
        print(
            "1. Sum \n"
            "2. Mean \n"
            "3. Median \n"
            "4. Exit"
        )
        try:
            oper = int(input("Select the operation you want to perform: "))
        except ValueError:
            print("Please select a valid option.")
            continue
        if oper == 1:
            numbers = collect_numbers()
            result = math_utils.add_numbers(*numbers)
            print(f"the sum is: {result}")
        elif oper == 2:
            x = int(input("Enter the number of values: "))
            result = math_utils.calculate_mean(x)
            print(f"the median is: {result}")
        elif oper == 3:
            nums = input_number_list()
            result = math_utils.calculate_median(nums)
            print(f"the median is: {result}")
        elif oper == 4:
            print("Exiting...")
            break
        else:
            print("Please select a valid option.")
except KeyboardInterrupt:
    sys.exit("\nExiting...")
