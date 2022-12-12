thing = "sdfadsf"


def ints(line: str) -> list[int]:
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


try:
    foo = int(thing)
except ValueError:
    print("gottem")
finally:
    print("success")

bar = "afdsfsdf7 9 3 2"
print(ints(bar))
bust = "3434 332 3 fgafad235dfdsgf foaf2 fdv as"
print(ints(bust))
print(ints("3, 6"))

print(0 % 10)
