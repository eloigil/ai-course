# Asymptotic notation

use worst case by default **BIG O**

### Sum rule
```
O(n) + O(n) = O(2n) = O(n)

O(n) + O(n²) = O(n + n²) = O(n)
```

### Product rule
```
O(n) * O(n) = O(n * n) = O(n²)
```

### Multiple recursivity
```
eg.

def fibonacci(n):
    if n == 0or n ==1:
        return1

     return fibonacci(n - 1) + fibonacci(n - 2)

O(2**n)
```
## Algorithm complexity

O(1): Constant
O(n): Lineal
O(log n): Logarithmic
O(n log n): log lineal
O(n\**2): Polynomial
O(2\**n) : Exponential
