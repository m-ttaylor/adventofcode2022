from ast import literal_eval

TEST = True
# TEST = False


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


lines = None
if TEST:
    with open(file="day13/test13input.txt", mode="r", encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
else:
    with open(file="day13/13input.txt", mode="r", encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)


def parse(s):
    if s == "":
        return

    def rParse(s):
        output = []
        i = 0
        num = ""
        while i < len(s):
            c = s[i]
            i += 1
            if c.isdigit():
                num += c
            if c in ",]" and num:
                output.append(int(num))
                num = ""
            if c == "[":
                substring, offset = rParse(s[i:])
                output.append(substring)
                i += offset
            elif c == "]":
                break
        return output, i

    return rParse(s)[0][0]


# print(lines[5] == "")
# print(parse(lines[3]))

pairs = [[]]
index = 0
for line in lines:
    if line == "":
        index += 1
        pairs.append([])
    elif line != "":
        pairs[index].append(literal_eval(line))

for i, p in enumerate(pairs):
    print(f"pair {i+1}:", p)


def compareAandB(a, b, i):
    bad = False
    for j in range(max(len(a), len(b))):
        left = a[j] if j < len(a) else None
        right = b[j] if j < len(b) else None
        if isinstance(left, int) and isinstance(right, list):
            left = [left]
        if isinstance(right, int) and isinstance(left, list):
            right = [right]
        if isinstance(left, list) and isinstance(right, list):
            return compareAandB(left, right, i)

        print(f"left: {left}")
        print(f"right: {right}")
        if left is None:
            print("left side ran out of items so input are in right order")
            continue
        if right is None:
            print("right side ran out of items, so inputs are not in right order")
            bad = True
            break
        if left > right:
            print("right side is smaller, so inputs are not in right order")
            bad = True
            break
        if left == right or left < right:
            continue
    return not bad


def checkOrder(pairs):
    goodCount = 0
    for i, (a, b) in enumerate(pairs):
        # print(f"a: {a}")
        # print(f"b: {b}")
        print(f"pair {i + 1}:")
        good = compareAandB(a, b, i)

        if good:
            print(f"things were fine at pair {i+1}")
            goodCount += i + 1
    # bad += i + 1

    return goodCount


print(checkOrder(pairs))


# print(parseInts(lines[0]))
# for line in lines:
#     rtn.append(parseInts(line))

# print(rtn)

# print(ints("1 1 3 1 1"))
