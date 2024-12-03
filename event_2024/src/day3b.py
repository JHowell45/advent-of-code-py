from re import compile, findall

from core.file_reader import get_file


@get_file(3)
def main(file) -> None:
    total: int = 0
    swap: bool = False
    text: str = file.read()
    pattern: str = "(do\\(\\))|(don't\\(\\))"
    prog = compile(pattern)

    start = 0
    end = 0
    for point in prog.finditer(text):
        if swap:
            if point.group(0) == "do()":
                print(point)
                start = point.end()
                swap = not swap
        else:
            if point.group(0) == "don't()":
                print(point)
                end = point.start()
                swap = not swap
                temp = text[start:end]
                print()
                print()
                print(start)
                print(end)
                # print(temp)
                print()
                print()
                total += mul_total(temp)
    print(f"Total enabled multiplications: {total}")


def mul_total(data: str) -> int:
    total = 0
    for line in findall("(mul\\(\\d+,\\d+\\))", data):
        [a, b] = findall("(\\d+)", line)
        total += int(a) * int(b)
    return total


if __name__ == "__main__":
    main()
