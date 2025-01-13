import random
import string
import time


def new_random_string(length: int) -> str:
    random.seed(time.time_ns())

    symbols = string.ascii_letters + string.digits

    return "".join(random.choice(symbols) for _ in range(length))
