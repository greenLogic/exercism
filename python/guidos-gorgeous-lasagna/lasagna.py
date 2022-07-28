"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(actual_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - actual_time


def preparation_time_in_minutes(number_layers):
    """Calculate the preparation time in minutes.

    :param number_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes.

    Function that takes the number of layers in the lasagna and returns the number of minutes
    it will take to prepare the lasagna.
    """
    return number_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_layers, elapsed_bake_time):
    """Calculate the time of the lasagna spent baking in the oven
    :param number_layers: int - number of layers in the lasagna
    :param elapsed_bake_time: int - the number of minutes the lasagna has been taking in the oven
    :return: int - total of minutes you've been cooking

    Function that takes the number of layers in the lasagna and the elapesed bake time as arguments
    and returns the time the lasagna has already spent baking in the oven.
    """
    return number_layers * 2 + elapsed_bake_time
