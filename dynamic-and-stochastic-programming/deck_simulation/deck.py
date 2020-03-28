import random
import collections

SUITS = ['spades', 'hearts', 'diamonds', 'clubs']
VALUES = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def create_deck():
  deck = []
  for suit in SUITS:
    for value in VALUES:
      deck.append((suit, value))
  
  return deck

def get_hand(deck, hand_size):
  hand = random.sample(deck, hand_size)

  return hand

def main(hand_size, attempts_n):
  deck = create_deck()

  hands = []
  for _ in range(attempts_n):
    hand = get_hand(deck, hand_size)
    hands.append(hand)

  pairs = 0
  for hand in hands:
    values = []
    for card in hand:
      values.append(card[1])

    counter = dict(collections.Counter(values))
    for val in counter.values():
      if val == 2:
        pairs += 1
        break
  pair_probability = pairs / attempts_n
  print(f'The probability of finding a pair in a hand of {hand_size} cards is {pair_probability}')


if __name__ == "__main__":
  hand_size = int(input('Hand size: '))
  attempts_n = int(input('Number of attempts: '))
  main(hand_size, attempts_n)