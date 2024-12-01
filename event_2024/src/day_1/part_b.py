from pathlib import Path

from shared import LocationSearch


def part_b() -> None:
    search = LocationSearch.new()
    p = Path(__file__).parent.resolve() / "puzzle_a.txt"
    with open(p, "r") as f:
        for index, line in enumerate(f):
            search.add_location_pair(index, line)
    print(f"The similarity score is: {search.similarity_score()}")


part_b()
