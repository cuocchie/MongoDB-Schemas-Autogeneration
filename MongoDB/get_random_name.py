import random


def get_name_list(first_name, last_name):
    """Get all first names, last names from files into 2 list.

    Args:
        first_name (list): contains all first names
        last_name (list): contain all last names

    Returns:
        [2-value tuple]: length of first and last name lists 
    """

    with open("name_list.txt", 'rb') as f:
        first_name_file = f.readlines()

    with open("last_name_list.txt", 'rb') as f:
        last_name_file = f.readlines()

    for lines in first_name_file:
        lines = lines.decode().strip()
        first_name.append(lines)

    for lines in last_name_file:
        lines = lines.decode().strip()
        last_name.append(lines)

    return [len(first_name) - 1, len(last_name) - 1]


def get_name(first_name, last_name, NUMBER_OF_FIRST_NAME, NUMBER_OF_LAST_NAME):
    """Get a random name from first and last name list.
    For optimozation, number of first name and last name is pre-defined.

    Args:
        first_name (list): list of first names
        last_name (list): list of last names
        NUMBER_OF_FIRST_NAME (int): number of first names
        NUMBER_OF_LAST_NAME (int): number of last names

    Returns:
        str: name
    """
    random_name = f'{last_name[random.randint(0, NUMBER_OF_LAST_NAME)]} {first_name[random.randint(0, NUMBER_OF_FIRST_NAME)]}'
    return random_name
