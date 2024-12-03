from re import findall

from core.file_reader import get_file


@get_file(3)
def main(file):
    total = 0
    for line in findall("(mul\\(\\d+,\\d+\\))", file.read()):
        [a, b] = findall("(\\d+)", line)
        total += int(a) * int(b)
    print(f"Total multiplications: {total}")


if __name__ == "__main__":
    main()
