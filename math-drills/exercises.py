#!/usr/bin/env python3
"""A module for math exercises


"""
from statistics import random
from .helpers import process_response


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

    allowed = ("a", "b")
    response = input(f"Which is larger?\na = {a}  or b = {b}\n")

    return process_response(correct, allowed, response)


def add_integers(list_of_numbers):
    """Add two integers.

    :param list_of_numbers: positive list of integers
    :return:
    """
    a, b = random.choices(list_of_numbers, k=2)
    correct = a + b
    sorted_list = sorted(list_of_numbers.copy())
    allowed = list(range(sorted_list.pop() * 2 + 1))
    response = input(f"{a} + {b} = ?")

    return process_response(correct, allowed, response)


def subtract_integers(list_of_numbers):
    """Subtract two integers with a positive answer.

    :param list_of_numbers: positive list of integers
    :return: string indicating "correct", "incorrect", or "exit"
    """
    a, b = random.choices(list_of_numbers, k=2)
    if a < b:
        correct = b - a
        response = input(f"{b} - {a} = ?")
    else:
        correct = a - b
        response = input(f"{a} - {b} = ?")

    allowed = list_of_numbers

    return process_response(correct, allowed, response)
