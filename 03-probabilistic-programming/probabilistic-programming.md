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