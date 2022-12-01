DEBUG = False

def findNMostCaloricElves(data: list[int], amount: int) -> list[int]:
  largestValues = [0 for i in range(amount)]
  subtotal = 0

  def smartAppend(value):
    smallest = min(largestValues)
    if value > smallest:
      largestValues[largestValues.index(smallest)] = value

  for val in data:
    if val != '\n':
      subtotal += int(val)
    else:
      smartAppend(subtotal)
      subtotal = 0

  smartAppend(subtotal)
  return sorted(largestValues)

def findMostCaloricElf(data: list[int]) -> int:
  return findNMostCaloricElves(data, 1)[0]

def findThreeMostCaloricElves(data: list[int]) -> list[int]:
  return findNMostCaloricElves(data, 3)

if __name__ == "__main__":
  DEBUG = True
  TEST = False
  datasets = ['./day1/day1input.txt', './day1/testday1input.txt']
  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()

    result = findMostCaloricElf(lines)
    result2 = findThreeMostCaloricElves(lines)
    print(f"The most calories an elf has are {result}")
    print(f"The three most calories any elves have are {result2}")
    print(f"For a sum total of {sum(result2)} calories")

