DEBUG, TEST = False, False
DAY = "N"

def part1(data):
  return

def part2(data):
  return

def solve(data: list) -> int:
  return True
  
if __name__ == "__main__":
  # TEST = True
  datasets = [f'./day{DAY}/day{DAY}input.txt', f'./day{DAY}/testday{DAY}input.txt']
  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()
    print(solve(lines))

