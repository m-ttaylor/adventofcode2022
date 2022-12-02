DEBUG = False

class FoeHand:
  ROCK='A'
  PAPER='B'
  SCISSORS='C'

class Outcome:
  LOSS='X'
  DRAW='Y'
  WIN='Z'

class PlayerHand:
  ROCK='X'
  PAPER='Y'
  SCISSORS='Z'

Points = {
  'ROCK': 1,
  'PAPER': 2,
  'SCISSORS': 3,
  'LOSS': 0,
  'DRAW': 3,
  'WIN': 6,
  'X': 1,
  'Y': 2,
  'Z': 3
}

def findMatchOutcomePoints(player1, player2):
  x, y = None, None

  handNumericMap = {
    FoeHand.ROCK: 0,
    FoeHand.PAPER: 1,
    FoeHand.SCISSORS: 2,
    PlayerHand.ROCK: 0,
    PlayerHand.PAPER: 1,
    PlayerHand.SCISSORS: 2,
  }

  x = handNumericMap[player1]
  y = handNumericMap[player2]
  
  outcomeMatrix = [
    [Points['DRAW'], Points['LOSS'], Points['WIN']],
    [Points['WIN'], Points['DRAW'], Points['LOSS']],
    [Points['LOSS'], Points['WIN'], Points['DRAW']]
  ]

  print(f"args are: {x}, {y}")
  return outcomeMatrix[y][x]

def findHandPointsFromOutcome(foeHand: str, outcome: str):
  correctDecryptionHands = {
    Outcome.LOSS: {
      FoeHand.ROCK: Points['SCISSORS'],
      FoeHand.PAPER: Points['ROCK'],
      FoeHand.SCISSORS: Points['PAPER'],
    },
    Outcome.DRAW: {
      FoeHand.ROCK: Points['ROCK'],
      FoeHand.PAPER: Points['PAPER'],
      FoeHand.SCISSORS: Points['SCISSORS'],
    },
    Outcome.WIN: {
      FoeHand.ROCK: Points['PAPER'],
      FoeHand.PAPER: Points['SCISSORS'],
      FoeHand.SCISSORS: Points['ROCK'],
    }
  }

  return correctDecryptionHands[outcome][foeHand]

def findTotalPointsEarned(foeHand: str, playerHand: str = None, outcome: str = None):
  
  outcomesMap = {
    Outcome.LOSS: 'LOSS',
    Outcome.DRAW: 'DRAW',
    Outcome.WIN: 'WIN'
  }

  handsMap = {
    PlayerHand.ROCK: 'ROCK',
    FoeHand.ROCK: 'ROCK',
    PlayerHand.PAPER: 'PAPER',
    FoeHand.PAPER: 'PAPER',
    PlayerHand.SCISSORS: 'SCISSORS',
    FoeHand.SCISSORS: 'SCISSORS',
  }

  if playerHand and foeHand:
    return findMatchOutcomePoints(foeHand, playerHand) + Points[handsMap[playerHand]]

  elif foeHand and outcome:
    return findHandPointsFromOutcome(foeHand, outcome) + Points[outcomesMap[outcome]]


def calculatePointTotal(data: list, decryption: str) -> int:
  score = 0

  for row in data:
    a, b = row.split()
    
    if decryption == 'bad':
      score += findTotalPointsEarned(foeHand=a, playerHand=b, outcome=None)
    elif decryption == 'good':
      score += findTotalPointsEarned(foeHand=a, playerHand=None, outcome=b)

  return score

if __name__ == "__main__":
  DEBUG = True
  TEST = True
  datasets = ['./day2/day2input.txt', './day2/testday2input2.txt']
  filename = datasets[1] if TEST else datasets[0]
  with open(filename, 'r') as file:
    lines = file.readlines()
    print(calculatePointTotal(lines, 'bad'))
    print(calculatePointTotal(lines, 'good'))