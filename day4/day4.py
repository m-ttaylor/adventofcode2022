DEBUG, TEST = False, False
DAY = "4"

def findIfSubsetPresent(elfA: tuple[str, str], elfB: tuple[str, str]) -> bool:
  perms = ((elfA[0], elfA[1], elfB[0], elfB[1]), 
           (elfB[0], elfB[1], elfA[0], elfA[1]))
  for lowerA, higherA, lowerB, higherB in perms:

    if (int(lowerA) >= int(lowerB) and int(higherA) <= int(higherB)):
      return True

  return False

def findIfOverlapPresent(elfA: tuple[str, str], elfB: tuple[str, str]) -> bool:
  perms = ((elfA[0], elfA[1], elfB[0], elfB[1]), 
           (elfB[0], elfB[1], elfA[0], elfA[1]))
  for lowerA, higherA, lowerB, higherB in perms:

    if (int(lowerA) in range(int(lowerB), int(higherB)+1) 
        or int(higherA) in range(int(lowerB), int(higherB)+1)):
      return True

  return False

def findBadElfPairs(data: list, mode: str) -> int:
  subsets = 0
  for elfPair in data:
    elfA, elfB = (elf.split('-') for elf in elfPair.split(','))
    hasSubset = findIfSubsetPresent(elfA, elfB) if mode == 'subset' else findIfOverlapPresent(elfA, elfB) if mode == 'overlap' else exit(1)

    subsets += 1 if hasSubset else 0

  return subsets
  
if __name__ == "__main__":
  # TEST = True
  datasets = [f'./day{DAY}/day{DAY}input.txt', f'./day{DAY}/testday{DAY}input.txt']
  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()
    print(findBadElfPairs(lines, 'subset'))

