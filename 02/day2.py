"""
This module provides a solution for Advent of Code, Day 2: I Was Told There Would Be No Math.
For more information, see: https://adventofcode.com/2015/day/2
"""
def get_dims_from_input_file(file_name):
    """Reads in data from an input file as tuples with 3 dimensions.

    Args:
        file_name ([string]): filename to read in.

    Returns:
        [[(integer, integer, integer)]]: list of tuples of integers (length, width, height).
    """
    # fetch data as lines of text
    lines = ""
    with open(file_name, "r", encoding='utf8') as input_file:
        lines = input_file.readlines()

    # convert each line into a tuple of dimensions
    splitter = lambda x: (int(x[0]), int(x[1]), int(x[2]))
    return [splitter(package_dims.strip().split("x")) for package_dims in lines]


def get_total_surface_area(dims):
    """Computes the surface area of a box, given a tuple of length, width, and height dimensions.

    Args:
        dims ([(integer, integer, integer)]): tuple of length, width, and height dimensions.

    Returns:
        [integer]: total surface area of box.
    """
    return 2 * (dims[0] * dims[1] + dims[1] * dims[2] + dims[2] * dims[0])


def get_area_of_smallest_side(dims):
    """Computes the surface area of the smallest side of a box,
    given a tuple of length, width, and height dimensions.

    Args:
        dims ([(integer, integer, integer)]): tuple of length, width, and height dimensions.

    Returns:
        [integer]: surface area of smallest side of box.
    """
    return min([dims[0] * dims[1], dims[1] * dims[2], dims[2] * dims[0]])


def get_perimeter_of_smallest_side(dims):
    """Computes the perimeter of the smallest side of a box,
    given a tuple of length, width, and height dimensions.

    Args:
        dims ([(integer, integer, integer)]): tuple of length, width, and height dimensions.

    Returns:
        [integer]: perimeter of smallest side of box.
    """
    return min([2 * dims[0] + 2 * dims[1], 2 * dims[1] + 2 * dims[2], 2 * dims[2] + 2 * dims[0]])


def get_volume(dims):
    """Computes the volume of a box, given a tuple of length, width, and height dimensions.

    Args:
        dims ([(integer, integer, integer)]): tuple of length, width, and height dimensions.

    Returns:
        [integer]: volume of the box.
    """
    return dims[0] * dims[1] * dims[2]


def day2_pt1(file_name):
    """Computes the amount of wrapping paper for all packages.
    Wrapping paper needed for each package is the total surface area of the package +
    surface area of smallest side.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: total amount of wrapping paper for all packages.
    """
    package_dims = get_dims_from_input_file(file_name)
    return sum(get_total_surface_area(curr_dims) + get_area_of_smallest_side(curr_dims)
    for curr_dims in package_dims)


def day2_pt2(file_name):
    """Computes the amount of ribbon for all packages.
    Ribbon needed for each package is the perimeter of the smallest side + the volume.

    Args:
        file_name ([string]): file name containing input string.

    Returns:
        [integer]: total amount of ribbon for all packages.
    """
    package_dims = get_dims_from_input_file(file_name)

    return sum(get_perimeter_of_smallest_side(curr_dims) + get_volume(curr_dims)
    for curr_dims in package_dims)


print(f"Part 1: {day2_pt1('input.txt')}")
print(f"Part 2: {day2_pt2('input.txt')}")
