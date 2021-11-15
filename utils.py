from random import randint, random
from datetime import date, timedelta
from typing import List


def get_random_birth(startdate=date(1998, 1, 1), max_year_range=6):
    return startdate + timedelta(randint(1, 365) * randint(0, max_year_range))


def get_random_number():
    return "0" + str(randint(1, 99999999)).zfill(8)


def get_random_point():
    point = round((random() * 10 + 1), 2)
    if point > 10:
        point = 10
    return point


def get_random_class(list: List):
    return randint(0, len(list) - 1)
