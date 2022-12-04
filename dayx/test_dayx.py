import dayx

def test_main():

  data = []
  with open('./dayx/testdayxinput.txt') as f:
    data = f.readlines()
  expected = 'foo'
  actual = dayx.main(data)
  assert(expected == actual)