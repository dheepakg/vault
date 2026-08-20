---
title: "Lecture 1: Intro to Deep Learning"
draft: false
tags:
  - DeepLearning
  - Perceptron
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


## Activation Function

Purpose - To introduce non-linearity into the network.

Examples of Activation Function,
1. Sigmoid function 
2. Hyperbolic tangent
3. Rectified Linear Unit




## 




---
## Reference 

1. Intro to Deep Learning - [Youtube video ](https://www.youtube.com/watch?v=II4giR4vOOo&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)


