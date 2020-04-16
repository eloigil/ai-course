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

## Graphs
Non-linear data structure with a dynamic nature.
$$
G=(V,A)
$$
V: vertex or nodes, the elements we are connecting.
A: arcs, connections between nodes.

Graphs can be:
- directed: it has directionality in its arcs.
- non-directed

A graph is complete if $A = VxV$

### Adjacency matrix
Matrix with all the elements of a graph that shows if there's a relation between the nodes of a graph.
![graph](https://en.wikipedia.org/wiki/File:6n-graph2.svg)
![adjacency matrix](https://wikimedia.org/api/rest_v1/media/math/render/svg/a773011024de5e3cbe8da03e97c79e1fe3101937)

### Bipartite graph
![bipartite graph](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Simple-bipartite-graph.svg/440px-Simple-bipartite-graph.svg.png)

#### Pairing
Relations between each of the subsets of a graph

#### Hall's marriage theorem
In a XY bipartite graph, if Xi is a subset of X, the number of elements of Y connected with Xi must be greater or equal to the number of elements in Xi to assure a complete pairing.

## Trees (I)
A tree is a rooted graph
- **root**: primitive instance of the tree
- **branches**: each branched path
- **leaves**: the ending instance of a branch

## Logics
- ¬ negation NOT
- ∨ disjunction AND
- ^ conjunction OR
- → implication THEN
- ↔ equivalence IS EQUIVALENT


---

## Algorithms
### Classification
Predicting categorical class tags of a new set based on previous data.
- binary
- multiclass

we can classificate them in:
- linearly splittable
- linearly non-splittable

#### Logistic regression
<!-- $$
logit(P)=log\dfrac{P}{1-P}
$$ -->
Separates two classes.
**Sigmoid**
Inverse of logit function.
$$
\phi(Z)=\dfrac{1}{1+e^{-z}}
$$
$$
\lim_{x \to +\infty} \phi(Z) = 1
$$
$$
\lim_{x \to -\infty} \phi(Z) = 0
$$

#### Support Vector Machines
![SVM](https://static.javatpoint.com/tutorial/machine-learning/images/support-vector-machine-algorithm.png)

$$
||w||=\sqrt{\sum_{j=1}^{m}w_{j}^2}
$$
*w*: coordinates of a vector
$$
margin=\dfrac{1}{2}||w||^2
$$
$$
ERROR=\dfrac{1}{2}||w||^2 + C(\sum_{i}\xi^{(i)})
$$
- high C: hard to separate
- low C: easy to separate

**Kernelization**:
Adding an extra dimension to separate classes.
- lineal
- RFB (Radial Function Base or Gaussian)
- Polynomical
- Sigmoid

#### Trees (II)
- regression trees
- classification trees

**Classification trees**:
Random forests: with diferent criteria they can get a final class.

#### KNN (K-Nearest Neighbors)
Lazy Algorithms, it doesn't get big picture (and constructiong a model).

Evaluates *k* neighbors of the element we are studying and assigns a tag to it.

Low efficiency.


### Dependency learning
#### Bayesian Networks
Association rules

### Logic Inductive Programming
Base knowledge
Training
Induced Hypothesis

### Optimization
1. generate population
2. calculate elements aptidtude
3. select the apt ones
4. apply reproduction

5. loop again from step 2

### Q-Learning
Reinforced learning (Q, quality)
$$
Q_{st,at}=Q_{st,at}+\alpha\cdot (r_t+\gamma\cdot max Q(st+1,a)-Q_{st,at})
$$
- $Q_{st,at}$: value
- $\alpha$: learning
- $r_t$: reward
- $\gamma$: discount
- $st$: future estimation



