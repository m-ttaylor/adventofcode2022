import day3

def test_findCorrectPrioritiesTotalForTestData():

  expected = 157

  data = []
  with open('./day3/testday3input.txt') as f:
    data = f.readlines()

  actual = day3.findPriorityOfWrongPocketItem(data)
  assert(expected == actual)

def test_findCorrectPrioritiesTotalForRealData():

  expected = 8139

  data = []
  with open('./day3/day3input.txt') as f:
    data = f.readlines()

  actual = day3.findPriorityOfWrongPocketItem(data)
  assert(expected == actual)

def test_findCorrectPrioritiesTotalOfBadgesForTestData():

  expected = 70

  data = []
  with open('./day3/testday3input.txt') as f:
    data = f.readlines()

  actual = day3.findPriorityOfBadges(data)
  assert(expected == actual)

def test_findCorrectPrioritiesTotalOfBadgesForRealData():

  expected = 2668

  data = []
  with open('./day3/day3input.txt') as f:
    data = f.readlines()

  actual = day3.findPriorityOfBadges(data)
  assert(expected == actual)