import random
import math

def mean (X):
  return sum(X)/len(X)

def variance (X):
  mu = mean(X)

  accumulator = 0
  for x in X:
    accumulator += (x - mu)**2

  return accumulator / len(X)

def standard_deviation (X):
  return math.sqrt(variance(X))

if __name__ == "__main__":
    X = [random.randint(1, 21) for i in range(20)]
    mu = mean(X)
    Var = variance(X)
    sigma = standard_deviation(X)

    print(f'X: {X}')
    print(f'Mean: {mu}')
    print(f'Variance: {Var}')
    print(f'Standard deviation: {sigma}')