"""
Pozwoliłem sobie przyjąć, że min_value, max_value
i input_value są liczbami całkowitymi,
oraz że przedział są obustronnie zamknięty.
Jeżeli, min_value i max_value byłyby liczbami
zmiennoprzecinkowymi, to należałoby, to zrobić tak:
min_value = random.random() * 150
max_value = random.random() * 125 + 75
oraz input_value typować na float.

Została złamana zasada 80 znaków w linijce
przez specyfikę printa.
"""

import random


def get_values():
    """
        Returns  2 random values.
        min_value is always in range 0 - 150,
        max_value is always range 75 - 200 and
        greater than min_value.
    """
    min_value = max_value = 0
    while max_value <= min_value:
        min_value = random.randint(0, 150)
        max_value = random.randint(75, 200)
    return min_value, max_value

def input_number(message):
    """
        Returns user input if its valid.
    """
    while True:
        try:
            input_value = int(input(message))
            return input_value
        except ValueError:
            print('Input must be a number!')
            continue

def is_number_in_range(min_value, max_value, message):
    """
        Checks if user input is between
        closed group of min_value and max_value.
        If true then ends function.
    """
    while True:
        value = input_number(message)
        if min_value <= value <= max_value:
            print(f'Input {value} is in range.')
            return
        elif min_value > value:
            print("The value you've entered is smaller than the minimum value allowed.")
        else:
            print("The value you've entered is greater than the maximum value allowed.")


if __name__ == "__main__":
    min_value, max_value = get_values()
    message = f'Input number in range {min_value} - {max_value}: '
    is_number_in_range(min_value, max_value, message)
