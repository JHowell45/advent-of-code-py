from pathlib import Path

from shared import LocationSearch


def part_a() -> None:
    search = LocationSearch.new()
    p = Path(__file__).parent.resolve() / "puzzle_a.txt"
    with open(p, "r") as f:
        for index, line in enumerate(f):
            search.add_location_pair(index, line)
    print(f"The total distance is: {search.total_distance()}")


part_a()
