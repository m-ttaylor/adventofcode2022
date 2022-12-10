"""-- Day 10: --"""

from collections import deque

DEBUG, TEST = False, False
DAY = "10"


def simulate(data: list):
    """foo"""

    cycle = 0
    commands = deque()
    x = 1
    signalStrengths = []

    for c in data:
        command = c.strip()

        if command == "noop":
            commands.appendleft({"cycles": 1, "change": 0})
        if command.startswith("addx"):
            amount = command.split(" ")[1]
            commands.appendleft({"cycles": 2, "change": int(amount)})

    while len(commands) > 0:
        print(f"current x value: {x}")
        cycle += 1
        if cycle == 20 or ((cycle - 20) % 40 == 0):
            # signalStrengths.append({str(cycle): cycle * x})
            signalStrengths.append(cycle * x)

        top = commands[-1]
        print(top)
        top["cycles"] -= 1
        # cycle += 1

        if top["cycles"] == 0:
            toExecute = commands.pop()
            print("to execute:", toExecute)
            x += toExecute["change"]

    print(cycle)
    print(signalStrengths)
    print(len(signalStrengths))
    print(sum(signalStrengths))


if __name__ == "__main__":
    # TEST = True
    # DEBUG = True
    datasets = [f"./day{DAY}/day{DAY}input.txt", f"./day{DAY}/testday{DAY}input.txt"]
    filename = datasets[1] if TEST else datasets[0]
    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
        print(simulate(lines))
