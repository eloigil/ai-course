import random


def roll_dice(dice_roll_n):
  rolls_sequence = []
  
  for _ in range(dice_roll_n):
    roll = random.choice([1, 2, 3, 4, 5, 6])
    rolls_sequence.append(roll)

  return rolls_sequence

def main(dice_roll_n, attempts_n):
  rolls = []
  for _ in range(attempts_n):
    rolls_sequence = roll_dice(dice_roll_n)
    rolls.append(rolls_sequence)
  
  got_1 = 0
  for roll in rolls:
    if 1 in roll:
      got_1 += 1

  probability_rolls_1 = got_1 / attempts_n
  print(f'Probability to get at least a 1 in {dice_roll_n} rolls = {probability_rolls_1}')

if __name__ == "__main__":
    dice_roll_n = int(input('Dice rolls: '))
    attempts_n = int(input('Simulation attempts: '))

    main(dice_roll_n, attempts_n)