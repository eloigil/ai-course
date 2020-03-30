# Probabilistic programming
## Conditional probability
Conditional probability is a measure of the probability of an event occurring given that another event has (by assumption, presumption, assertion or evidence) occurred.

`P(A&B) = P(A) * P(B|A) + P(¬A) * P(B|¬A)`

### Bayes' theorem
Describes the probability of an event, based on prior knowledge of conditions that might be related to the event.

![Bayes' theorem](https://wikimedia.org/api/rest_v1/media/math/render/svg/87c061fe1c7430a5201eef3fa50f9d00eac78810)

*developed:*
```
P(Hypothesis & Event) = P(H&E) / P(E) = P(H)P(E|H) / (P(H)P(E|H) + P(¬H)P(E|¬H))
```

- **P(H)** *(prior)* Hypothesis before evidence
- **P(H|E)** *(posterior)*
- **P(E|H)** *(likelihood)* probability that this situation is correct

## Statistics fallacies
### Garbage in, garbage out
Nonsense input data produces nonsense output or "garbage".

### Cum Hoc Ergo Propter Hoc
Correlation doesn't mean causality

### Prejudice in sampling
Is a fallacy not having a representative sample of the population.

### Texas sharpshooter fallacy
Is committed when differences in data are ignored, but similarities are overemphasized.

It is related to the clustering illusion, which is the tendency in human cognition to interpret patterns where none actually exist.

### Regression fallacy
It assumes that something has returned to normal because of corrective actions taken while it was abnormal.

This fails to account for natural fluctuations. It is frequently a special kind of the post hoc fallacy.


## Machine learning
### Feature vectors
Represent symbolic or numerical features, allowing to analize an object from a mathematical perspective.

Define which elements are important for an algorithm.

### Distance metrics
Quantify how closer are the vectors incorporated into the algorithm

### Clustering
Group similar* objects into clusters that identify them
- hard clustering: each object belongs to a cluster
- soft clustering: each object is assigned a certain probability to belong to a cluster

#### Hierarchical clustering
- **Agglomerative**: *This is a "bottom-up" approach*: each observation starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.
- **Divisive**: *This is a "top-down" approach*: all observations start in one cluster, and splits are performed recursively as one moves down the hierarchy.
Dendogram:
![Dendogram](https://upload.wikimedia.org/wikipedia/commons/1/12/Iris_dendrogram.png)

#### K-means
Uses the centroids(mean of a cluster) to group the objects.

#### *Similitude
There are 4 aproximations to define similitude:
- **connective models**: Similar points are the ones closer to the search space.
- **centroid models**: defines similitude in terms of closeness to the centroid of the cluster.
- **distribution models**: Tries to assign probabilities to each data unit, in order to determine if it belongs to a specific distribution.
- **density models**: analyze the density of data in different regions and divide the set in clusters.

*You can use more than a model to get better results*

