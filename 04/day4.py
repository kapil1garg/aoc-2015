"""
This module provides a solution for Advent of Code, Day 4: The Ideal Stocking Stuffer.
For more information, see: https://adventofcode.com/2015/day/4
"""
import hashlib

def has_n_leading_zeros(computed_hash, n_zeros):
    """Checks if a hash_string has n leading zeros.

    Args:
        computed_hash ([string]): hash string to check for leading zeros.
        n_zeros ([integer]): number of zeros to look for.

    Returns:
        [boolean]: true if hash has n_zeros leading zeros.
    """
    return computed_hash[:n_zeros] == ("0" * n_zeros)

def day4_pt1(secret_key):
    """Determines the smallest number that, when appended to secret_key,
    yields an md5 hash with 5 leading 0's.

    Args:
        secret_key ([string]): key to add numbers to.

    Returns:
        [integer]: number to append to secret_key to get a md5 hash with 5 leading zero's.
    """
    number = 1
    while True:
        # create a key and hash by adding the current number to the secret_key
        curr_key = secret_key + str(number)
        curr_hash = hashlib.md5(curr_key.encode("utf-8")).hexdigest()

        # check if we have 6 leading zeros in the hash
        if has_n_leading_zeros(curr_hash, 5):
            return number

        # continue searching for a number
        number += 1


def day4_pt2(secret_key):
    """Determines the smallest number that, when appended to secret_key,
    yields an md5 hash with 6 leading 0's.

    Args:
        secret_key ([string]): key to add numbers to.

    Returns:
        [integer]: number to append to secret_key to get a md5 hash with 6 leading zero's.
    """
    number = 1
    while True:
        # create a key and hash by adding the current number to the secret_key
        curr_key = secret_key + str(number)
        curr_hash = hashlib.md5(curr_key.encode("utf-8")).hexdigest()

        # check if we have 6 leading zeros in the hash
        if has_n_leading_zeros(curr_hash, 6):
            return number

        # continue searching for a number
        number += 1


print(f"Part 1: {day4_pt1('bgvyzdsv')}")
print(f"Part 2: {day4_pt2('bgvyzdsv')}")
