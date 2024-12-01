import click

from src.day_1.part_a import part_a


@click.command()
@click.argument("day", type=int)
@click.argument("part", type=click.Choice(["a", "b"]))
def aoc(day: int, part: str):
    match day:
        case 1:
            match part:
                case "a":
                    part_a()
                case "b":
                    pass
        case _:
            print(f"Day {day} has not yet been implemented!")


if __name__ == "__main__":
    aoc()
