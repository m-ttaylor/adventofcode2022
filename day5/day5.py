from collections import defaultdict

DEBUG, TEST = False, False
DAY = "5"

class CrateStack:
  crates: list[str] = []

  def __init__(self, data: list[str]=None):
    if (data): 
      self.crates = data
    else:
      self.crates = []

  def takeCrate(self) -> str:
    return self.crates.pop()

  def takeCrates(self, amount: int) -> 'CrateStack':
    length = len(self.crates)
    takenCrates = self.crates[length-amount:length]
    self.crates = self.crates[:length-amount]
    return CrateStack(takenCrates)

  def addCrate(self, crate):
    self.crates.append(crate)

  def addCrates(self, crates: 'CrateStack'):
    self.crates += crates.crates

  def __repr__(self) -> str:
    return f"[{', '.join(self.crates)}]\n"

  def __eq__(self, other) -> bool:
    return self.crates == other.crates

def readTops(stacks: list[CrateStack]) -> str:
  tops = ''
  for stack in stacks:
    if stack.crates != []:
      tops += stack.takeCrate().strip('[').strip(']')

  return tops

def parseCommand(stacks: list[CrateStack], command: str, version=''):
  words = command.split()
  moves = int(words[1])
  source = int(words[3])-1
  dest = int(words[5])-1

  if version == '9001':
    crates = CrateStack()
    crates = stacks[source].takeCrates(moves)
    stacks[dest].addCrates(crates)

  else:
    for _ in range(moves):
      crate = stacks[source].takeCrate()
      if crate != None:
        stacks[dest].addCrate(crate)

def parseStacks(data: list[str]) -> list[CrateStack]:

  crateStacks = defaultdict(list)
  crateStacksIndexed: list[CrateStack] = []

  for line in data:
    spaceCount, index = 0, 0
    
    for c in line.split(' '):
      
      if spaceCount == 4:
        index += 1
        spaceCount = 0

      if c == '':
        spaceCount += 1

      elif c.startswith('['):
        stack = crateStacks[str(index)]
        stack.insert(len(stack), c.strip())
        index += 1

  for i in range(len(crateStacks)):
      stack = CrateStack(list(reversed(crateStacks[str(i)])))
      crateStacksIndexed.append(stack)

  return crateStacksIndexed

def splitData(data: list[str]):

  splitIndex = data.index('\n')
  stacks, commands = data[:splitIndex-1], data[splitIndex+1:]

  return (stacks, commands)

def solve(data: list[str], version='') -> int:
  stacks, commands = splitData(data)
  crateStacksIndexed = parseStacks(stacks)

  for command in commands:
    parseCommand(crateStacksIndexed, command, version)

  return readTops(crateStacksIndexed)
  
if __name__ == "__main__":
  # TEST = True
  datasets = [f'./day{DAY}/day{DAY}input.txt', 
              f'./day{DAY}/testday{DAY}input.txt',
              f'./day{DAY}/testday{DAY}input2.txt']

  filename = datasets[1] if TEST else datasets[0]

  with open(filename, 'r') as file:
    lines = file.readlines()
    print(solve(lines, '9001'))