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

- O(1): Constant
- O(n): Linear
- O(log n): Logarithmic
- O(n log n): log lineal
- O(n\*\*2): Polynomial
- O(2\*\*n) : Exponential

## Search & sorting algorithms
### Linear search
It sequentially checks each element of the list until a match is found or the whole list has been searched.

O(n)

### Binary search
Search a sorted array by repeatedly dividing the search interval in half.

O(log n)

### Bubble sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

O(n\*\*2)

### Insertion sort
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms

![insertion sort](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

O(n\*\*2)

### Merge sort
Conceptually, a merge sort works as follows:

1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

![merge sort](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

O(n * log n)



## Data visualisation with (Bokeh)[docs.bokeh.org]

