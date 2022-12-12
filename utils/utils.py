"""bar"""


def ints(line: str) -> list[int]:
    "find and return all ints in string separated by spaces or commas"
    values = []
    for chunk in line.strip().replace(",", " ").split(" "):
        value: int = None
        try:
            value = int(chunk)
        except ValueError:
            pass
        else:
            values.append(value)

    return values
