---
title: "Lecture 1: Intro to Deep Learning"
draft: false
tags:
  - DeepLearning
  - Perceptron
  - NeuralNetwork
---

## Perceptron: Forward Propagation

Perceptron is a basic component of Neural network.


![](img_perceptron.png)





$$

 y = g (w_0 + \sum_{i=1}^{m} x_i w_i)
  \newline

  \quad {\ where\   y\ is\ Output,}
  \quad  {g\ is\ non-linear\ activation\ function, }
  \quad { w_0\ is\ bias, }
  \quad {x_i w_i\ is Linear\ Combination\ input    }


$$




### Activation Function

Purpose - To introduce non-linearity into the network.

Examples of Activation Function,
1. Sigmoid function
2. Hyperbolic tangent
3. Rectified Linear Unit




##  Building Neural Networks with Perceptron

### A Single Neuron

When having _m_ number of dimensions, the above equation in Matrix form can be,

$$
 y = g (w_0 + X^T W)
\newline
\quad \\\text{\ where\ } X\ {\ is }
\begin{bmatrix}
x_1 \\ x_2 \\ . \\ . \\ x_m
\end{bmatrix}
\quad {,\ W\ is}
\begin{bmatrix}
w_1 \\ w_2 \\ . \\ . \\ w_m
\end{bmatrix}
$$

![](img_single_neuron.png)


> [!Single Neuron]
> It is a _**dot product**_ + _**bias**_ and applying the _**non-linearity**_.

### Perceptron: Simplified

![](img_simplified_perceptron.png)

$$
z = w_0   +  \sum_{j=i}^m x_j w_j
$$

Then,

$$
y = g(z)
$$

### Multi Output Perceptron

![](img_multi_output.png)

$$
Z_i = w_{o,i}   +  \sum_{j=i}^m x_j w_{j,i}

$$

> [!Dense Layer]
> In Multi output perceptron the _inputs_ are densely connected to _outputs_ its called **Dense Layer**


### Single Layer Neural Network

![](img_single_layer_neural_network.png)

Hidden layer is,

$$

z_i = w_{o,i}^{(1)}   +  \sum_{j=i}^m x_j w_{j,i}^{(1)}

$$

Final output is,

$$
y_{i} = g (w_0^{i} + \sum_{i=1}^{d_{1}}  g(z_{j}) w_{i,j}^{(2)})
$$

### Simplifying Multi  Output Perceptron

The connection are simplified, and those are _matrix multiplication_.

![](img_multi_output_perceptron.png)


## Deep Neural Network

Deep Neural Network a neural network with more than 3 layers.

![](img_deep_neural_network.png)


$$

z_{k,i} = w_{o,i}^{(k)}   +  \sum_{j=i}^n g(z_{k-1,j}) x_j w_{j,i}^{(k)}

$$

---


## Reference

1. Intro to Deep Learning - [Youtube video ](https://www.youtube.com/watch?v=II4giR4vOOo&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)


