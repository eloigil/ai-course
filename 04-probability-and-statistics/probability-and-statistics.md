# Probability & statistics
- **Sample space (Ω)**: Set of values we can get from a specific experiment.
- **Event**: Each result we get from an experiment that is in the sample space
  - possible: there is a possibility that it will happen
  - sure: only this event can happen
  - impossible: this event can't happen

## Laplace's rule
```
P(A) = favorable cases of A / possible cases
```

## Compound probability
More than one random event occurs.

### Event types:
- compatible: when it can be found in each sample space
- incompatible: when it can't be found in each sample space
- complementary: when joining all events in a group, they conform the sample space

### Union
Event formed with all elements that match A or B
```
P(A∪B) = P(A) + P(B) - P(A∩B)
```

### Intersection
Event formed with all elements that match A and B
```
P(A∩B) = P(A|B) * P(B)
P(B|A) = P(A∩B) / P(A) si P(A)≠0
```

## Combinatorics

### Variations
Group *n* elements into subroups of *r* elements 
```
Vn,r = n! / (n - r)!
```

### Permutations
Variations of *n* elements in subroups of *r*, where *n = r*

Each subgroup differs from the others just in the orther of the elements.
```
Pn = n!
```
### Combinations
Getting subgroups of *r* elements from a group of *n* elements. And none of these subgroups is repeated.
```
Cn,r = n! / r!(n-r)!
```

## Data distribution
- absolute frequency: number of times a data appears (ni)
- relative frequency: number of times a data appears
```
Fi = ni / N
```

### Graphics
- sectors diagram
- freqüency plygon
- bars graphic

## Central trend measurements
### mean
![mean](https://wikimedia.org/api/rest_v1/media/math/render/svg/4e3313161244f8ab61d897fb6e5fbf6647e1d5f5)

### median
Central value of a sorted list of elements.
![median](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3253c25db67454d6f6c763a73cc64dbf0d47b74)

### trend
Most repeated value

## Correlation
- direct
- inverse
- null
### Covariance
Indicates the degree of variation of two random variables with respect to their means

## Dispersion measurements
### Range
Difference between max and min value. It tracks the total dispersion.
```
R = max - min
```

### Mean deviation
For non-clustered data: is the arithmetic mean of the absolute values of the deviatoins of all data with respect to the mean.
For grouped data:
![mean deviation](https://wikimedia.org/api/rest_v1/media/math/render/svg/d3b7f03e504d1a16a212827c21decae2e30f7f7fz)

### Standard deviation
### Variance

### Pearson correlation coefficient
Quotient between the covariance and the product of the standard deviation of each variable
- direct --> 1
- indirect --> -1
- no correlation --> 0

![Pearson correlation coefficient](https://wikimedia.org/api/rest_v1/media/math/render/svg/f76ccfa7c2ed7f5b085115086107bbe25d329cec)

## Position parameters
### Quartiles
Q1=25%,Q2= 50% & Q3=75%, divide data in 4 parts. Q2 matches the mean.
### Deciles
Divide data in 10 parts: D1=10%, D2=20% … D9=90%. D5 matches the mean.
### Percentiles
Percentles: P1=1%, P2=2% … P99=99%. P50 matches the mean.



