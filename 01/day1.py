"""
This module provides a solution for Advent of Code, Day 1: Not Quite Lisp.
For more information, see: https://adventofcode.com/2015/day/1
"""
def get_text_from_input_file(file_name):
    """Reads in data from an input file as a string.

    Args:
        file_name ([string]): filename to read in.

    Returns:
        [[integer]]: list of integers read in from file_name.
    """
    # fetch data as one block of text
    text = ""
    with open(file_name, "r", encoding='utf8') as input_file:
        text = input_file.read()

    return text


def day1_pt1(file_name):
    """Computes the current floor based on the sequence of ( and ) in the input file.
    ( increases the floor by 1, and ) decreases the floor by 1.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: current floor based on sequence of ( and ).
    """
    input_text = get_text_from_input_file(file_name)
    return sum(1 if char == "(" else -1 for char in input_text)


def day1_pt2(file_name):
    """Returns the index of input where floor becomes basement (-1)

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: index of character from file_name that causes position to be in the basement.
    """
    input_text = get_text_from_input_file(file_name)

    curr_floor = 0
    for index, char in enumerate(input_text):
        curr_floor += 1 if char == "(" else -1
        if curr_floor < 0:
            return index + 1


print(f"Part 1: {day1_pt1('input.txt')}")
print(f"Part 2: {day1_pt2('input.txt')}")
