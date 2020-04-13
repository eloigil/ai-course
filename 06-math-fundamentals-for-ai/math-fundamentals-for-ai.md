# Math fundamentals for AI
## Combinatorics
### Binomial coeficient
**N above R**:
- number combinations of *n* elements taken in groups of *r* elements
- number of subsets of *r* elements that has a set of *n* elements

$$
\begin{pmatrix}
n\\
r
\end{pmatrix}
=
\dfrac{n!}{r!(n-r)!}
$$

### Little theorem of Fermat

$a^p-a$ is divisible by *p*

### Non-repetition
#### Permutations
Possible ordinations for a set of *n* different elements
$$
n!
$$
#### Variations
Possible sorted subsets of *r* different elements in a set of *n* elements
$$
n * (n-1) * ... * (n-r+1)
$$
#### Combinations
Possible non-sorted subsets of *r* different elements in a set of *n* elements
$$
\begin{pmatrix}
n\\
r
\end{pmatrix}
$$

### with repetition
#### Permutations
$$
\dfrac{n!}{\alpha! * \beta! * \gamma!}
$$
where α, β, γ are the numbers of repetitions
#### Variations
$$
n^r
$$

#### Combinations
$$
\begin{pmatrix}
n+r-1\\
r
\end{pmatrix}
$$
