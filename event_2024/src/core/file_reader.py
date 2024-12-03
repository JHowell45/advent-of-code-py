from io import TextIOWrapper
from typing import Generator


def read(day: int) -> Generator[TextIOWrapper, None, None]:
    with open(f"puzzle_inputs/day{day}.txt") as f:
        yield f
