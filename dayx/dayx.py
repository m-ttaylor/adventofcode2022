DEBUG = False

def main(data):
  return 'foo'
  
if __name__ == "__main__":
  DEBUG = True
  TEST = True
  datasets = ['./dayx/dayxinput.txt', './dayx/testdayxinput.txt']
  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()
    print(main(lines))