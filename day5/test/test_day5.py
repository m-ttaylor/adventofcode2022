DAY = '5'
from day5.day5 import *

data = []
with open(f'./day{DAY}/day{DAY}input.txt') as f:
  data = f.readlines()

a = '[a]'
b = '[b]'
c = '[c]'
d = '[d]'
e = '[e]'
f = '[f]'
g = '[g]'
h = '[h]'
j = '[i]'
k = '[j]'

def test_canAddCrateToStack():
  expected = CrateStack([a])

  stackA = CrateStack()
  stackA.addCrate(a)
  
  assert(expected == stackA)

def test_canRemoveCrateFromStack():
  expected = CrateStack()
  stackA = CrateStack()
  stackA.addCrate(a)
  crate = stackA.takeCrate()

  assert(expected == stackA)
  assert(crate == a)

def test_addAndRemoveSeveral():

  expected = CrateStack()

  stackA = CrateStack()
  stackA.addCrate(a)
  stackA.addCrate(b)
  stackA.addCrate(c)

  removed = []
  
  for _ in range(3):
    removed.append(stackA.takeCrate())

  assert(expected == stackA)
  assert([c, b, a])

def test_removeFromEmptyStackThrowsException():

  stackA = CrateStack()
  exceptionHappened = False
  try:
    stackA.takeCrate()
  except:
    exceptionHappened = True

  assert(exceptionHappened)


def test_moveCrates():
  stackA = CrateStack()
  stackB = CrateStack()

  stackA.addCrate(a)
  stackB.addCrate(b)
  stacks = [stackA, stackB]
  parseCommand(stacks, 'move 1 from 1 to 2')

  assert(CrateStack() == stackA)
  assert(CrateStack([a, b]) == stackB)


def test_readTops_shouldReturnEmptyWhenEmpty():

  stacks = [CrateStack(), CrateStack(), CrateStack()]
    
  assert('' == readTops(stacks))

def test_readTops_shouldReturnCorrectResultWithStacksOfOne():

  stacks = [CrateStack([a]), CrateStack([b]), CrateStack([c])]
    
  assert('abc' == readTops(stacks))

def test_readTops_shouldReturnCorrectResultWithUnevenStacks():

  stacks = [CrateStack([a]), CrateStack([b, c, d, e, f, g]), CrateStack([h])]
    
  assert('agh' == readTops(stacks))

  


# def test_one():
#   expected = 825
#   actual = day5.solve(data)
#   assert(expected == actual)
  
# def test_two():
#   expected = 475
#   actual = day5.solve(data)
#   assert(expected == actual)