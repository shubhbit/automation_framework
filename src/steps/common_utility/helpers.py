import random, string, re


def random_word(size):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(size))


def random_number(st, end):
    return random.randint(st, end)