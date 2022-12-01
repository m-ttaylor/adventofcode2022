import day1

data = []

with open('./day1/testday1input.txt') as f:
  data = f.readlines()

def test_findMostCaloricShouldReturnHighestSum():
  expected = 6   
  actual = day1.findMostCaloricElf(data)
  assert(expected == actual)

def test_findThreeMostCaloricShouldReturnThreeHighestSums():
  expected = [4, 5, 6]
  actual = day1.findThreeMostCaloricElves(data)
  assert(expected == actual)