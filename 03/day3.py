"""
This module provides a solution for Advent of Code, Day 3: Perfectly Spherical Houses in a Vacuum.
For more information, see: https://adventofcode.com/2015/day/3
"""
from itertools import chain
from collections import Counter

def get_directions_from_input_file(file_name):
    """Reads in data from an input file as a string.

    Args:
        file_name ([string]): filename to read in.

    Returns:
        [string]: string of directions in which to move to deliver packages.
    """
    # fetch data as lines of text
    text = ""
    with open(file_name, "r", encoding='utf8') as input_file:
        text = input_file.read()

    return text


def compute_next_position(curr_position, direction):
    """Get Santa's (or Robo Santa's) new position given the current position and direction to go in.

    Args:
        curr_position ([(integer, integer)]): tuple of (x, y) grid positions.
        direction ([string]): direction to move in.
            ^ = 1 north; v = 1 south; > = 1 east; < = 1 west.

    Returns:
        [(integer, integer)]: tuple with new (x, y) grid position.
    """
    new_position = ()
    if direction == "^":
        new_position = (curr_position[0] + 1, curr_position[1])
    elif direction == "v":
        new_position = (curr_position[0] - 1, curr_position[1])
    elif direction == ">":
        new_position = (curr_position[0], curr_position[1] + 1)
    elif direction == "<":
        new_position = (curr_position[0], curr_position[1] - 1)

    return new_position


def get_delivered_packages(directions):
    """Compute where packages were delivered, given a string of directions.

    Args:
        directions ([string]): path for delivery.

    Returns:
        [[(integer, integer)]]: list of tuples of (x, y) coordinates where packages were delivered.
    """
    curr_position = (0, 0)
    delivered_packages = [curr_position]

    for direction in directions:
        # compute new position based on direction
        new_position = compute_next_position(curr_position, direction)

        # add new position to delivered packages and update curr_position
        delivered_packages.append(new_position)
        curr_position = new_position

    return delivered_packages


def day3_pt1(file_name):
    """Computes number of unique homes that Santa delivered packages to.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: number of houses that received at least 1 package.
    """
    # get all directions from input file
    directions = get_directions_from_input_file(file_name)

    # get the list of coordinates where packages were delivered
    delivered_packages = get_delivered_packages(directions)

    # count unique delivered packages
    packages_to_addresses = Counter(chain(delivered_packages))
    return len(packages_to_addresses.keys())


def day3_pt2(file_name):
    """Computes number of unique homes packages are delivered to between Santa and Robo-Santa.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: number of houses that received at least 1 package.
    """
    # get all directions from input file
    directions = get_directions_from_input_file(file_name)

    # directions are alternated between santa and robo-santa
    santa_directions = directions[::2]
    robo_santa_directions = directions[1::2]

    # get the list of coordinates where packages were delivered
    santa_delivered_packages = get_delivered_packages(santa_directions)
    robo_santa_delivered_packages = get_delivered_packages(robo_santa_directions)
    all_delivered_packages = santa_delivered_packages + robo_santa_delivered_packages

    # count unique delivered packages
    packages_to_addresses = Counter(chain(all_delivered_packages))
    return len(packages_to_addresses.keys())


print(f"Part 1: {day3_pt1('input.txt')}")
print(f"Part 2: {day3_pt2('input.txt')}")
