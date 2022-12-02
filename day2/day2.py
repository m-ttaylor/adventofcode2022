DEBUG = False

badOutcomeValuesCypher = {
  'X': { # rock
    'A': 3,
    'B': 0,
    'C': 6,
  },
  'Y': { # paper
    'A': 6,
    'B': 3,
    'C': 0,
  },
  'Z': { # scissors
    'A': 0,
    'B': 6,
    'C': 3,
  }
}

goodHandValuesCypher = {
  # determines the hand you play and its point value based on 
  # your opponent and the desired result
  'X': { # lose
    'A': 3, # play scissors
    'B': 1, # play rock
    'C': 2, # play paper
  },
  'Y': { # draw
    'A': 1, # play rock
    'B': 3, # play scissors
    'C': 2, # play paper
  },
  'Z': { # win
    'A': 2, # play paper
    'B': 3, # play scissors
    'C': 1, # play rock
  }
}

badHandValuesCypher = {
  'X': 1, # rock
  'Y': 2, # paper
  'Z': 3 # scissors
}

goodOutcomeValuesCypher = {
  'X': 0, # lose
  'Y': 3, # draw
  'Z': 6, # win
}

def calculatePointTotal(data: list, decryption: str) -> int:
  value1Cypher, value2Cypher = {}, {}

  if decryption == 'bad':
    value1Cypher, value2Cypher = badHandValuesCypher, badOutcomeValuesCypher
  elif decryption == 'good':
    value1Cypher, value2Cypher = goodOutcomeValuesCypher, goodHandValuesCypher

  score = 0
  for row in data:
    foe, self = row.split()
    score += (value1Cypher[self] + value2Cypher[self][foe])

  return score

if __name__ == "__main__":
  DEBUG = True
  TEST = False
  datasets = ['./day2/day2input.txt', './day2/testday2input.txt']
  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()
    print(calculatePointTotal(lines, 'good'))

    # 11732 is too low
