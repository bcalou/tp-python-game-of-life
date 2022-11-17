"""This file contains the utils to read and write a GOL map in a file.
"""

import os

def read_map(filename):
    """Read a map from a file.
    """
    # Check if the file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError("The file does not exist")

    # Read the file
    map: list[list[int]] = []
    with open(filename, "r") as file:
        # Read the file to generate the map
        line: str = file.readline()
        while line:
            map.append([])
            for char in line:
                if char == "0" or char == "1":
                    map[-1].append(int(char))
                else:
                    raise ValueError("Invalid character in the file.")
            line = file.readline()

    return map
