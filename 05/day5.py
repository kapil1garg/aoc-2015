"""
This module provides a solution for Advent of Code, Day 5: Doesn't He Have Intern-Elves For This?.
For more information, see: https://adventofcode.com/2015/day/5
"""
import re

def get_lines_from_input_file(file_name):
    """Reads in data from an input file as a list of strings.

    Args:
        file_name ([string]): filename to read in.

    Returns:
        [[string]]: list of strings from file_name.
    """
    # fetch data as lines of text
    lines = ""
    with open(file_name, "r", encoding='utf8') as input_file:
        lines = input_file.readlines()

    return lines


def day5_pt1(file_name):
    """Counts how many strings from the input file are nice.
    A string is nice if:
    (1) it has 3 or more vowels;
    (2) has at least 1 double letter; and
    (3) does not contain any of the unallowed strings.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: number of nice strings.
    """
    # get input text
    input_lines = get_lines_from_input_file(file_name)

    # create regex patterns to look for
    vowels_pattern = r"[aeiou]"
    double_letters_pattern = r"(.)\1"
    ignore_strings_pattern = r"ab|cd|pq|xy"

    # check each string against the regex patterns
    num_nice_strs = 0
    for curr_string in input_lines:
        num_vowels = len(re.findall(vowels_pattern, curr_string))
        num_double_letters = len(re.findall(double_letters_pattern, curr_string))
        num_ignore_strings = len(re.findall(ignore_strings_pattern, curr_string))

        # check if string is nice
        if num_vowels >= 3 and num_double_letters >= 1 and num_ignore_strings == 0:
            num_nice_strs += 1

    return num_nice_strs

def day5_pt2(file_name):
    """Counts how many strings from the input file are nice.
    A string is nice if:
    (1) it has a pair of letters that is found at least twice in the string; and
    (2) has a sequence of strings such as xyx.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: number of nice strings.
    """
    # get input text
    input_lines = get_lines_from_input_file(file_name)

    # create regex patterns to look for
    letter_pair_pattern = r"(\w{2}).*?(\1)"
    sequence_pattern = r"(\w).{1}\1"

    # check each string against the regex patterns
    num_nice_strs = 0
    for curr_string in input_lines:
        num_letter_pair_pattern = len(re.findall(letter_pair_pattern, curr_string))
        num_sequence_pattern = len(re.findall(sequence_pattern, curr_string))

        # check if string is nice
        if num_letter_pair_pattern >= 1 and num_sequence_pattern >= 1:
            num_nice_strs += 1

    return num_nice_strs


print(f"Part 1: {day5_pt1('input.txt')}")
print(f"Part 2: {day5_pt2('input.txt')}")
