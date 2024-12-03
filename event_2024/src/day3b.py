from re import compile, findall

from core.file_reader import get_file


@get_file(3)
def main(file) -> None:
    print(f"Total enabled multiplications: {enabled_mul_total(file.read())}")


def enabled_mul_total(text: str) -> int:
    total: int = 0
    swap: bool = False
    pattern: str = "(do\\(\\))|(don't\\(\\))"
    prog = compile(pattern)

    start = 0
    end = 0
    for point in prog.finditer(text):
        if swap:
            if point.group(0) == "do()":
                start = point.end()
                swap = not swap
        else:
            if point.group(0) == "don't()":
                end = point.start() + 1
                total += mul_total(text[start:end])
                swap = not swap
    if not swap:
        total += mul_total(text[start:])
    return total


def mul_total(data: str) -> int:
    total = 0
    for line in findall("(mul\\(\\d+,\\d+\\))", data):
        [a, b] = findall("(\\d+)", line)
        total += int(a) * int(b)
    return total


if __name__ == "__main__":
    main()
