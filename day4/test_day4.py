import day4

data = []
with open('./day4/day4input.txt') as f:
  data = f.readlines()

def test_findOverlap():
  expected = 825
  actual = day4.findBadElfPairs(data, 'overlap')
  assert(expected == actual)
  
def test_findSubset():
  expected = 475
  actual = day4.findBadElfPairs(data, 'subset')
  assert(expected == actual)