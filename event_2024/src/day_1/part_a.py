from pathlib import Path

from src.day_1.shared import LocationSearch


def part_a() -> None:
    p = Path(__file__).parent.resolve() / "puzzle_a.txt"
    search = LocationSearch.new()
    with open(p, "r") as f:
        for index, line in enumerate(f):
            search.add_location_pair(index, line)
    print(f"The total distance is: {search.total_distance()}")
