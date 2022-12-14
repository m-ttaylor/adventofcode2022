import day2

def test_flexibleCalculateWithBadDecryption():

  data = []
  with open('./day2/testday2input.txt') as f:
    data = f.readlines()
    expected = 15
    actual = day2.calculatePointTotal(data, 'bad')

    assert(expected == actual)

def test_flexibleCalculateWithGoodDecryption():

  data = []
  with open('./day2/testday2input.txt') as f:
    data = f.readlines()
    expected = 12
    actual = day2.calculatePointTotal(data, 'good')

    assert(expected == actual)

def test_flexibleCalculateWithGoodDecryptionMoreData():

  data = []
  with open('./day2/testday2input2.txt') as f:
    data = f.readlines()
    expected = 39
    actual = day2.calculatePointTotal(data, 'good')

    assert(expected == actual)

def test_flexibleCalculateWithGoodDecryptionExhaustiveData():

  data = []
  with open('./day2/testday2input3.txt') as f:
    data = f.readlines()
    expected = 45
    actual = day2.calculatePointTotal(data, 'good')

    assert(expected == actual)

def test_calculateWithBadDecryptionAndRealData():

  data = []
  with open('./day2/day2input.txt') as f:
    data = f.readlines()
    expected = 14163
    actual = day2.calculatePointTotal(data, 'bad')
    assert(expected == actual)

def test_calculateWithGoodDecryptionAndRealData():

  data = []
  with open('./day2/day2input.txt') as f:
    data = f.readlines()
    expected = 12091
    actual = day2.calculatePointTotal(data, 'good')
    assert(expected == actual)