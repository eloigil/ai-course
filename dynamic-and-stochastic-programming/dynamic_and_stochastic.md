# Dynamic programming
- **optimal substructure:** combining optimal solutions to subproblems
- **spliced problem:** an optimal solution that involves solving the same problem multiple times

## Memoization
Optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.
```
def fibonacci_dynamic(n, memo = {}):
  if n == 0 or n == 1:
    return 1
  try:
    return memo[n]
  except KeyError:
    resultado = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)
    memo[n] = resultado
    
    return resultado
```
*\* use **sys** library to set recursion limit if exceeded `sys.setrecursionlimit(num)`*


# Stochastic programming
Stochastic programming is a framework for modeling optimization problems that involve uncertainty.
## Probability
### Laws of probability
- complementary law of probability
`P(A) + P(~A) = 1`
- multiplication law of probability
`P(A & B) = P(A) * P(B)`
- additive law of probability
`P(A o B) = P(A) + P(B) [mutually exclusive]`
`P(A o B) = P(A) + P(B) -  P(A & B) [mutually non-exclusive]`

## Statistical inference
Statistical inference is the process of using data analysis to deduce properties of an underlying distribution of probability

### Law of large numbers
The average of the results obtained from a large number of trials should be close to the expected value and will tend to become closer to the expected value as more trials are performed.

![law of large numbers](https://wikimedia.org/api/rest_v1/media/math/render/svg/bd76c5b48534e2a4821e5c0bc577c031ecf498b1)

### Mean
Central value of a discrete set of numbers: specifically, the sum of the values divided by the number of values.

![mean](https://wikimedia.org/api/rest_v1/media/math/render/svg/4e3313161244f8ab61d897fb6e5fbf6647e1d5f5)

- population mean: μ (mu)
- sample mean: x̄ (x bar)

### Variance
variance is the expectation of the squared deviation of a random variable from its mean

![variance](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c5c6e7bbd52e69c29e2d5cfe21989313aba55d4)

### Standard deviation
Square root of the variance.
It has the same units as the mean.

![standard deviation](https://wikimedia.org/api/rest_v1/media/math/render/svg/4c98cfcd7dc201f65aa452ed555666f1b23bf477)

