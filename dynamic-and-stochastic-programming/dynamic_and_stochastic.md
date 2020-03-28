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