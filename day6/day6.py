DEBUG, TEST = False, False
DAY = "6"

def solve(lines: list[str]):
  return findMarker(lines[0], 14)

def findMarker(line: str, markerSize: int):
  lastFour = []
  for i, c in enumerate(line):
    lastFour.append(c)
    print(lastFour)
    if len(lastFour) > markerSize:
      lastFour.pop(0)

    if len(lastFour) == markerSize and len(lastFour) == len(set(lastFour)):
      return str(i+1)
  return 'a'
  
if __name__ == "__main__":
  # TEST = True
  datasets = [f'./day{DAY}/day{DAY}input.txt', 
              f'./day{DAY}/testday{DAY}input.txt',
              f'./day{DAY}/testday{DAY}input2.txt']

  filename = datasets[1] if TEST else datasets[0]

  with open(filename, 'r') as file:
    lines = file.readlines()
    print(solve(lines))