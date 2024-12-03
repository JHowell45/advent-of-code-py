from re import findall


def main():
    total = 0
    with open("puzzle_inputs/day3.txt", "r") as file:
        for line in findall("(mul\\(\\d+,\\d+\\))", file.read()):
            [a, b] = findall("(\\d+)", line)
            total += int(a) * int(b)
    print(f"Total mul(): {total}")


if __name__ == "__main__":
    main()
