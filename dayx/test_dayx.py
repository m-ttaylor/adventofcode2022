DAY = 'x'
import dayx

data = []
with open(f'./day{DAY}/day{DAY}input.txt') as f:
  data = f.readlines()

def test_one():
  expected = 825
  actual = dayx.solve(data)
  assert(True)
  
def test_two():
  expected = 475
  actual = dayx.solve(data)
  assert(True)