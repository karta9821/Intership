"""
Pozwoliłem sobie przyjąć, że min_value, max_value
i input_value są liczbami całkowitymi,
oraz że przedział są obustronnie zamknięty.
Jeżeli, min_value i max_value byłyby liczbami
zmiennoprzecinkowymi, to należałoby, to zrobić tak:
min_value = random.random() * 150
max_value = random.random() * 125 + 75
oraz input_value typować na float.
"""

import random


def get_values():
    min_value = max_value = 0
    while max_value <= min_value:
        min_value = random.randint(0, 150)
        max_value = random.randint(75, 200)
    return min_value, max_value

def input_value(min_value, max_value):
    while True:
        try:
            input_value = int(input(f'Input number in range {min_value} - {max_value}: '))
            return input_value
        except ValueError:
            print('Input must be a number!')
            continue

def is_number_in_range(min_value, max_value):
    while True:
        value = input_value(min_value, max_value)
        if min_value <= value <= max_value:
            print(f'Input {value} is in range.')
            return
        elif min_value > value:
            print("The value you've entered is smaller than the minimum value allowed.")
        else:
            print("The value you've entered is greater than the maximum value allowed")


if __name__ == "__main__":
    min_value, max_value = get_values()
    is_number_in_range(min_value, max_value)
