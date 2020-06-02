#!/usr/bin/env python3
"""A module for math exercises


"""
from statistics import random


def quantity_discrimination(list_of_numbers):
    """Choose which value, "a" or "b", is greater.
    Pass in a list of int values to compare.

    :param list_of_numbers: List of ints to compare,
                            usually provided as range()
    :return: String of "correct" or "incorrect" to be used by score function
             Returns "exit" if user does not enter "a" or "b"
    """
    a, b = random.choices(list_of_numbers, k=2)
    if a < b:
        correct = "b"
    else:
        correct = "a"

    response = input(f"Which is larger?\na = {a}  or b = {b}\n")

    if (response.lower() != "a") and (response.lower() != "b"):
        return "exit"

    if response.lower() == correct:
        print("Congratulations! Your are correct.\n")
        return "correct"
    else:
        print("Incorrect\n")
        return "incorrect"


def add_integers(list_of_numbers):
    a, b = random.choices(list_of_numbers, k=2)
    answer = a + b
    response = input(f"{a} + {b} = ?")


    if response == answer