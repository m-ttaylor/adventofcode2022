"""foo"""

DEBUG, TEST = False, False
DAY = "11"


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


class Test:
    """Represents the number to check divisibility for and which monkey to throw to
    in the divisible (A) or not divisible (B) case"""

    condition: int = None
    monkeyA: "Monkey" = None
    monkeyB: "Monkey" = None

    def __init__(self, condition, monkeyA, monkeyB):
        self.condition = condition
        self.monkeyA = monkeyA
        self.monkeyB = monkeyB


class Operation:
    """Represents the operation to perform on an item's worry level during inspection:
    - add a constant
    - multiply by a constant
    - square
    """

    operand: str = None
    constant: int = None

    def __init__(self, operand, constant):
        self.operand = operand
        self.constant = constant


class Monkey:
    """A monkey with a list of items, an operation to perform while inspecting an item,
    and test criteria to determine which monkey to throw to"""

    monkeyId: int
    items: list[int]
    operation: Operation
    test: Test
    inspections = 0

    def __init__(self, monkeyId):
        self.monkeyId = monkeyId

    def setItems(self, items):
        """Set items"""
        self.items = items

    def setOperation(self, operation):
        """Set operation"""
        self.operation = operation

    def setTest(self, test):
        """Set test"""
        self.test = test

    def popItem(self) -> int:
        """Pop and return the monkey's last item"""
        return self.items.pop()

    def inspect(self, item):
        """Simulate the monkey inspecting the current item"""

        self.inspections += 1
        if DEBUG:
            print(f"  Monkey inspects an item with a worry level of {item}.")

        if self.operation.operand == "*":
            item = item * self.operation.constant
            if DEBUG:
                print(
                    f"    Worry level is multiplied by {self.operation.constant} to {item}."
                )
        elif self.operation.operand == "+":
            item += self.operation.constant
            if DEBUG:
                print(
                    f"    Worry level increases by {self.operation.constant} to {item}."
                )
        elif self.operation.operand == "^":
            item = item**2
            if DEBUG:
                print(f"    Worry level is multiplied by itself to {item}.")

        return item

    def calmDown(self, item, method):
        """reduce worry level of item"""
        if method == 1:
            item = item // 3
            # item = item % 96577

        if DEBUG:
            print(
                f"    Monkey gets bored with item. Worry level is divided by 3 to {item}."
            )
        return item

    def testAndThrow(self, item):
        """perform test on item and throw to the relevant monkey"""
        if item % self.test.condition == 0:
            monkeyA = self.test.monkeyA
            # item = item / self.test.condition
            # item = math.lcm(item, monkeyA.test.condition)
            # item = item % monkeyA.test.condition
            # item = item % (self.test.condition * monkeyA.test.condition)
            if DEBUG:
                print(f"    Current worry level is divisible by {self.test.condition}.")
                print(
                    f"    Item with worry level {item} is throw to monkey {monkeyA.monkeyId}"
                )
            monkeyA.items.append(item)
        else:
            monkeyB = self.test.monkeyB
            # item = math.lcm(item, monkeyB.test.condition)
            # item = item % monkeyB.test.condition
            # item = item % (self.test.condition * monkeyB.test.condition)
            if DEBUG:
                print(
                    f"    Current worry level is not divisible by {self.test.condition}."
                )
                print(
                    f"    Item with worry level {item} is throw to monkey {monkeyB.monkeyId}"
                )
            monkeyB.items.append(item)

    def __repr__(self):

        return str(
            {
                "monkeyId": self.monkeyId,
                "items": self.items,
                "operation": self.operation,
                "test": self.test,
            }
        )


def splitLine(line: str):
    "split line on semicolon"
    return line.strip().split(":")[1].strip()


def readInMonkeys(data: list):
    """just get the monkeys"""
    monkeys: list[Monkey] = []
    monkeyId: int
    items: list = []
    monkeyId: str
    monkeyA: str
    monkeyB: str
    condition: int
    # just get the monkeys
    for line in data:
        if line.startswith("Monkey"):
            monkeyId = int(line.strip().split(" ")[1].removesuffix(":"))
            monkeys.append(Monkey(monkeyId))

    # populate the monkeys
    for line in data:

        if line.startswith("Monkey"):
            monkeyId = int(line.strip().split(" ")[1].removesuffix(":"))

        elif line.strip().startswith("Starting items"):
            items = ints(splitLine(line))
            monkeys[monkeyId].setItems(items)

        elif line.strip().startswith("Operation:"):
            operand, constant = splitLine(line).split(" ")[3:]
            if constant == "old":
                operand = "^"
                constant = "-1"
            monkeys[monkeyId].setOperation(Operation(operand, int(constant)))

        elif line.strip().startswith("Test:"):
            condition = int(splitLine(line).split(" ")[2])

        elif line.strip().startswith("If true:"):
            monkeyA = int(splitLine(line).split(" ")[3])

        elif line.strip().startswith("If false:"):
            monkeyB = int(splitLine(line).split(" ")[3])
            monkeys[monkeyId].setTest(
                Test(condition, monkeys[monkeyA], monkeys[monkeyB])
            )

    return monkeys


def solve(data: list, method=1, rounds=20):
    """foo"""

    monkeys = readInMonkeys(data)

    for mbizround in range(rounds):
        for monkey in monkeys:
            if DEBUG:
                print(f"Monkey {monkey.monkeyId}:")
            while len(monkey.items) > 0:
                item = monkey.popItem()
                item = monkey.inspect(item)
                item = monkey.calmDown(item, method)
                monkey.testAndThrow(item)

        if DEBUG:
            print(
                f"After round {mbizround+1}, the monkeys are holding items with these worry levels:"
            )
            for monkey in monkeys:
                print(f"Monkey {monkey.monkeyId}: {monkey.items}")

    print(f"== After round {rounds} ==")

    inspections = []
    for monkey in monkeys:
        print(f"Monkey {monkey.monkeyId} inspected items {monkey.inspections} times")
        inspections.append(monkey.inspections)
    max1, max2 = sorted(inspections, reverse=True)[:2]

    print(f"monkey business score: {max1*max2}")
    return max1 * max2


if __name__ == "__main__":
    TEST = True
    # DEBUG = True
    datasets = [f"./day{DAY}/day{DAY}input.txt", f"./day{DAY}/testday{DAY}input.txt"]
    filename = datasets[1] if TEST else datasets[0]
    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
        print(solve(lines, 1, 20))
        # print(solve(lines, 2, 10000))
