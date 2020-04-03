# Probability & statistics
## Probability
- **Sample space (Ω)**: Set of values we can get from a specific experiment.
- **Event**: Each result we get from an experiment that is in the sample space
  - possible: there is a possibility that it will happen
  - sure: only this event can happen
  - impossible: this event can't happen

### Laplace's rule
```
P(A) = favorable cases of A / possible cases
```

### Compound probability
More than one random event occurs.

#### Event types:
- compatible: when it can be found in each sample space
- incompatible: when it can't be found in each sample space
- complementary: when joining all events in a group, they conform the sample space

#### Union
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

### Combinatorics

#### Variations
Group *n* elements into subroups of *r* elements 
```
Vn,r = n! / (n - r)!
```

#### Permutations
Variations of *n* elements in subroups of *r*, where *n = r*

Each subgroup differs from the others just in the orther of the elements.
```
Pn = n!
```
#### Combinations
Getting subgroups of *r* elements from a group of *n* elements. And none of these subgroups is repeated.
```
Cn,r = n! / r!(n-r)!
```

### Data distribution
- absolute frequency: number of times a data appears (ni)
- relative frequency: number of times a data appears
```
Fi = ni / N
```

#### Graphics
- sectors diagram
- freqüency plygon
- bars graphic

### Central trend measurements
#### mean
![mean](https://wikimedia.org/api/rest_v1/media/math/render/svg/4e3313161244f8ab61d897fb6e5fbf6647e1d5f5)

#### median
Central value of a sorted list of elements.
![median](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3253c25db67454d6f6c763a73cc64dbf0d47b74)

#### trend
Most repeated value