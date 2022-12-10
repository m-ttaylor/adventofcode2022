"""-- Day 10: --"""

from collections import deque

DEBUG, TEST = False, False
DAY = "10"


def simulate(data: list):
    cycle = 1
    commands = deque()
    x = 1
    signalStrengths = []
    spritePos = [-1, 0, 1]
    output = ["", "", "", "", "", ""]

    for c in data:
        command = c.strip()

        if command == "noop":
            commands.appendleft({"cycles": 1, "change": 0, "command": "noop"})
        if command.startswith("addx"):
            amount = command.split(" ")[1]
            commands.appendleft({"cycles": 2, "change": int(amount), "command": "addx"})

    command = commands.pop()
    while len(commands) > 0:

        if command["cycles"] == 2:
            print(
                f"Start cycle: {cycle}: begin executing {command['command']} {command['change']}"
            )

        drawPosX = (cycle - 1) % 40 - 1
        drawPosY = (cycle - 1) // 40

        if drawPosX in spritePos:
            output[drawPosY] += "#"
        else:
            output[drawPosY] += "."

        print(f"During cycle {cycle}: CRT draws pixel in position {drawPosX}")
        print(f"Current CRT row: {output[drawPosY]}")

        if cycle == 20 or ((cycle - 20) % 40 == 0):
            signalStrengths.append(cycle * x)

        command["cycles"] -= 1
        if command["cycles"] == 0:
            x += command["change"]
            for i, _ in enumerate(spritePos):
                spritePos[i] += command["change"]
                print("verify sprite")

            print(
                f"End of cycle {cycle}: finish executing {command['command']} {command['change']} (register X is now {x})"
            )

            spritePosOutput = "".join(
                ["." if i not in spritePos else "#" for i in range(40)]
            )
            print(f"Sprite position: {spritePosOutput}")
            command = commands.pop()

        print()
        cycle += 1

    for line in output:
        print(line)

    return sum(signalStrengths)


if __name__ == "__main__":
    # TEST = True
    # DEBUG = True
    datasets = [f"./day{DAY}/day{DAY}input.txt", f"./day{DAY}/testday{DAY}input.txt"]
    filename = datasets[1] if TEST else datasets[0]
    with open(file=filename, mode="r", encoding="utf8") as file:
        lines = file.readlines()
        print(simulate(lines))
