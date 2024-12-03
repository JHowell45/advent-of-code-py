from typing import Callable


def get_file(day: int):
    def wrapper(f: Callable):
        def inner(*args, **kwargs):
            with open(f"puzzle_inputs/day{day}.txt") as file:
                return f(*args, **kwargs, file=file)

        return inner

    return wrapper
