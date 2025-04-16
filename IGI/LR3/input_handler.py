"""
User input handling utilities
"""


def input_float(prompt):
    """
    Get validated float input from user

    Args:
        prompt (str): Display prompt

    Returns:
        float: Validated input
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_int(prompt = ''):
    """
    Get validated integer input from user

    Args:
        prompt (str): Display prompt

    Returns:
        int: Validated input
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_list(prompt = ''):
    """
    Get a validated list of floats from user input.

    Args:
        prompt (str): Display prompt.

    Returns:
        list: List of floats.
    """
    while True:
        try:
            user_input = input(prompt)
            return [float(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter a space-separated list of numbers.")