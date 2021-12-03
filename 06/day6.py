"""
This module provides a solution for Advent of Code, Day 6: Probably a Fire Hazard.
For more information, see: https://adventofcode.com/2015/day/6
"""
import re


def get_instructions_from_input_file(file_name):
    """Reads in data from an input file as tuple of (instruction, (start x, start y) (end x end y)).

    Args:
        file_name ([string]): filename to read in.

    Returns:
        [[string]]: list of strings from file_name.
    """
    # fetch data as lines of text
    lines = ""
    with open(file_name, "r", encoding='utf8') as input_file:
        lines = input_file.readlines()

    # parse instructions from lines
    match_pattern = r"(turn off|turn on|toggle).(\d{1,3},\d{1,3}) through (\d{1,3},\d{1,3})"

    # parse each line into an instruction with a command, start coords, and end coords
    instructions = []
    for line in lines:
        match_obj = re.match(match_pattern, line)
        start_coords = match_obj.group(2).split(",")
        end_coords = match_obj.group(3).split(",")
        instructions.append((match_obj.group(1),
        (int(start_coords[0]), int(start_coords[1])),
        (int(end_coords[0]), int(end_coords[1])),))

    return instructions


def sum_light_values(light_matrix):
    """Sums the values of all lights in the light matrix.

    Args:
        light_matrix ([[integer]]): matrix representing lights and their values.

    Returns:
        [integer]: total value of lights.
    """
    return sum(sum(row) for row in light_matrix)


def day6_pt1(file_name):
    """Compute number of on lights in the 1000x1000 light matrix after running instructions.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: number of lights on after running instructions.
    """
    # get input instructions
    instructions = get_instructions_from_input_file(file_name)

    # create empty 1000x1000 matrix
    light_matrix = [[False for j in range(0, 1000)] for i in range(0, 1000)]

    # work through each instruction and update lights
    for instruction in instructions:
        # loop over start to end coordinates
        for row in range(instruction[1][0], instruction[2][0] + 1):
            for col in range(instruction[1][1], instruction[2][1] + 1):
                if instruction[0] == "turn off":
                    light_matrix[row][col] = False
                elif instruction[0] == "turn on":
                    light_matrix[row][col] = True
                elif instruction[0] == "toggle":
                    light_matrix[row][col] = not light_matrix[row][col]

    return sum_light_values(light_matrix)


def day6_pt2(file_name):
    """Computes the total brightness in the 1000x1000 light matrix after running instructions.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: total brightness of lights on after running instructions.
    """
    # get input instructions
    instructions = get_instructions_from_input_file(file_name)

    # create empty 1000x1000 matrix
    light_matrix = [[0 for j in range(0, 1000)] for i in range(0, 1000)]

    # work through each instruction and update lights
    for instruction in instructions:
        # loop over start to end coordinates
        for row in range(instruction[1][0], instruction[2][0] + 1):
            for col in range(instruction[1][1], instruction[2][1] + 1):
                if instruction[0] == "turn off":
                    light_matrix[row][col] = max(light_matrix[row][col] - 1, 0)
                elif instruction[0] == "turn on":
                    light_matrix[row][col] += 1
                elif instruction[0] == "toggle":
                    light_matrix[row][col] += 2

    return sum_light_values(light_matrix)


print(f"Part 1: {day6_pt1('input.txt')}")
print(f"Part 2: {day6_pt2('input.txt')}")
