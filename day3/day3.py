import math
import string

DEBUG = False

ascii = string.ascii_letters
points = { letter: v+1 for v, letter in enumerate(ascii)}

def findPriorityOfWrongPocketItem(data):
  wrongItems = []
  priorityTotal = 0
  for rucksack in data:
    size = len(rucksack)
    half = math.floor(size/2)
    pocketA, pocketB = rucksack[:half], rucksack[half:]
    if DEBUG:
      print(f'pocketA: {pocketA}')
      print(f'pocketB: {pocketB}')

    wrongItem = None
    for i in range(half):
      if pocketA[i] in pocketB:
        wrongItem = pocketA[i]
      
    wrongItems.append(wrongItem)
    priorityTotal += points[wrongItem]

  if DEBUG:
    print('all wrong items', wrongItems)

  return(priorityTotal)
  

def findPriorityOfBadges(data):

    chunked = [[] for i in range(math.floor(len(data)/3))]
    for i, x in enumerate(data):
      chunked[i//3].append(x)  

    priorityTotal = 0
    for chunk in chunked:
      elfOneVisited, elfTwoVisited, elfThreeVisited = (set(elf.strip()) for elf in chunk)

      badge = list(elfOneVisited & elfTwoVisited & elfThreeVisited)[0]
      priorityTotal += points[badge]
    
    return priorityTotal

if __name__ == "__main__":
  TEST = False
  datasets = ['./day3/day3input.txt', './day3/testday3input.txt']
  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()
    print(findPriorityOfWrongPocketItem(lines))
    print(findPriorityOfBadges(lines))