# Discrete maths
## Graphs theory
**Nodes** conected with **edges** 
Types:
- simple: one edge between two nodes
- multigraph: more than one edge between two nodes
- pseudograph: edges to the same node
- ponderate: associates values to edges
- directed: edges have directionality
- directed multigraph: more than one edge with directionality between two nodes

**Degree of a vertex ($\delta$):** Number of edges converging in that node.

- **chain**: Association of nodes and edges
- **path**: A chain with no repetitions on edges or nodes
- **cycle**: Chain that ends at the same node it started without repeating other nodes.
- **closed chain**: Chain that ends at the same node it started repeating other nodes.

- **connected**: We can create a chain that connects all nodes.
- **non-connected**: We can't create a chain that connects all nodes.

#### Eulerian paths and eulerian cycles
- eulerian path: a path that travels through all edges just once.
- eulerian cycle: a path that travels through all edges once and ends at the same node it started.
All node degrees are even.

#### Hamiltonian paths and eulerian cycles
- hamiltonian path: a path that travels through all nodes just once.

$$
\delta(a)+\delta(b)\geq{n_{nodes}-1}
$$

*If it doesn't match this condition, it's not exclusive. It may be a hamiltonian pathe either.*

- hamiltonian cycle: a path that travels through all nodes once and ends at the same node it started.

If a node has $\delta = 1$ it can't be a hamiltonian cycle**


## Trees
- free: main node not clear
- rooted: root node
- expansion: each edge is ponderated





