# Introduction to Machine Learning
- **Artificial Intelligence (AI)**: Capacity of the machines to perform tasks that require human intelligence. Solving them equally or with better performance.

- **Machine learning (ML)**: Subfield of AI that uses data to bring machines the hability to perform an action not explicitly programmed.
Types:
  - Supervised learning
  - Unsupervised learning
  - Reinforcement learning

- **Deep learning**: Machine Learning with a lot of layers (artificial neural networks)

## Terminology and linear regression
```
y = f(Σ wi*xi + b)
```
where:
- y : label, what we are predicting
- x : feature, entry variable
- w : weight, how important is the feature for the prediction

### Model
Defines a relation between features and labels

### Training
Giving a dataset to the model and letting it to learn from labeled data.

### Inference
Using the model to make predictions

## Training & loss
### Mean squared error MSE
```
cost = [Σ{i=1 : Nelements}(miPredicción(i)- respuestaReal(i))^2] / Nelements*2
```
### Stochastic gradient descent SGD
Approximation using partial derivatives to the minimum loss.

- **Learning rate**: defines the size of the steps. Affecting the learning rythm.

Instead of using all data, we'll work with a data sample.

#### Learning process
1. Initialize all weight values using the prediction model.
2. Calculate the error (loss) and evaluate model performance
3. Using the gradient, recalculate weights and iterate

## Tensors
- scalar: 1
- vector: [1 2]
- matrix: 
|1 2|
|3 4|
- **tensor**: 
|[1 2] [1 2]|
|[3 4] [3 4]|
data structure that allows to represent complex matrices in a generic way.

