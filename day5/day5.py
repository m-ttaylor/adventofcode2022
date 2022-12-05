from collections import defaultdict
import math

DEBUG, TEST = False, False
DAY = "5"

class CrateStack:
  crates = []

  def __init__(self, data=[]):
    self.crates = data

  def takeCrate(self):
    # if self.crates != []:
      return self.crates.pop()
    # else:
    #    return None

  def addCrate(self, crate):
    self.crates.append(crate)

  def addCrateDifferent(self, create):
    return

  def __repr__(self):
    return f"[{', '.join(self.crates)}]\n"

  def __eq__(self, other):
    return self.crates == other.crates


def part1(data):
  return

def part2(data):
  return

def readTops(stacks: list[CrateStack]) -> str:
  tops = ''
  for stack in stacks:
    if stack.crates != []:
      tops += stack.takeCrate().strip('[').strip(']')

  return tops

def parseCommand(stacks: list[CrateStack], command: str):
  words = command.split()
  print(words)
  amountOfMoves = int(words[1])
  source = int(words[3])-1
  destination = int(words[5])-1

  # print(f'''interpretting command as making {amountOfMoves} takeCrate() 
  #   calls on stack index {source} and adding them to stack index {destination}''')
  # print('state')
  # print(stacks)
  for m in range(amountOfMoves):
    crate = stacks[source].takeCrate()
    if crate != None:
      stacks[destination].addCrate(crate)

def parseStacks(data) -> list[CrateStack]:

  crateStacks = defaultdict(list)
  crateStacksIndexed: list[CrateStack] = []
  for line in data:
    print(line)
  for line in data:
    spaceCount = 0
    index = 0

    # print(line)

    print(line.split(' '))

    # return [CrateStack()]
    for c in line.split(' '):
      
      if c == '':
        spaceCount += 1
      # if spaceCount == 3:
      #   index += 1
      #   spaceCount = 0
      if c.startswith('['):

        print(f'adding {c.strip()} to stack {index}')
        stack = crateStacks[str( index + math.floor( (spaceCount)/3 ) )]
        stack.insert(len(stack), c.strip())
        index += 1

  print(crateStacks['8'])
  for i in range(len(crateStacks)):
      stack = CrateStack(list(reversed(crateStacks[str(i)])))
      crateStacksIndexed.append(stack)

  # print(crateStacks['8'])
  return crateStacksIndexed

def solve(data: list) -> int:
  # return True
  splitIndex = data.index('\n')
  stacks, commands = data[:splitIndex-1], data[splitIndex+1:]

  # print(stacks)
  # print(commands)

  crateStacksIndexed = parseStacks(stacks)
  # return ''

  for stack in crateStacksIndexed:
    print(stack)

  print(crateStacksIndexed[8])
  # print('state before making moves:', crateStacksIndexed)

  return ''
  for command in commands:

    # print('the whole line', command)

    if command.startswith('move'):
      parseCommand(crateStacksIndexed, command)

  # print(crateStacks)
  # print('-'*20)
  print(crateStacksIndexed)

  # answer = ''
  # for stack in crateStacksIndexed:
  #   if stack.crates != []:
  #     answer += stack.takeCrate().strip('[').strip(']')

  # print('final answer', answer)
  return readTops(crateStacksIndexed)
  
if __name__ == "__main__":
  # TEST = True
  datasets = [f'./day{DAY}/day{DAY}input.txt', 
              f'./day{DAY}/testday{DAY}input.txt',
              f'./day{DAY}/testday{DAY}input2.txt']

  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()
    print(solve(lines))

    # LRSTJLNPG is wrong

