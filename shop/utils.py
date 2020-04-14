import random


def get_random_number():
    number = random.randint(1, 10000000)
    if number == 543:
        raise Exception('Error')
    return number


def multiplication(number):
    return number * get_random_number()
