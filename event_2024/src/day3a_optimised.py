from re import finditer

from core.file_reader import get_file


@get_file(3)
def main(file) -> None:
    total = 0
    pattern: str = "(mul\\((?P<a>\\d{1,3}),(?P<b>\\d{1,3})\\))"
    for line in finditer(pattern, file.read()):
        total += int(line.group("a")) * int(line.group("b"))
    print(f"Total multiplications: {total}")


if __name__ == "__main__":
    main()
