---
draft: "false"
---

The word _tensor_ comes from the Latin word _tendere_ meaning "to stretch".

## Definition

> [!definition] 
> "A tensor is ==a mathematical object that generalizes scalars, vectors, and matrices to higher dimensions, acting as a multi-dimensional array of numerical values==."
> — Simple Wikipedia

To put in simple words, Tensor are vectors with multiplle dimensions. 


0. A tensor of order zero (zeroth-order tensor) is a scalar (a simple number).
1. A tensor of order one (first-order tensor) is a linear map that maps every vector into a scalar. 
	- A vector is a tensor of order one.
2. A tensor of order two (second-order tensor) is a linear map that maps every vector into a vector
	- Matrix is a 2<sup>nd</sup> order tensor


## What can we do on a Tensor

Tensor is like a matrix of higher dimension. We can do all the matrix functions, as well as vector operations. Like,
1. Dot product - results in scalar
2. Cross product - results in a vector (aka tensor)
3. Addition, subtractions
4. Transpose
5. and etc,.


To do all the above operations (and more), we use numpy and tensorflow or pytorch. 


## More about Tensors

Machine Learning (ML) is all about numbers. **Tensor is a specialised container for those numbers.** You might know tensors from maths or physics, but in machine learning, a tensor is simply PyTorch's data type for storing numbers. Think of it like a more powerful version of a list or array.

**Words** get mapped to numbers. The simplest approach is to assign each word a unique ID. So the sentence hello world becomes [0, 1] - just numbers that PyTorch can work with.

```shell
"hello"  → 0
"world"  → 1
```


**Images** - are nothing more than a grid of pixels, each containing colour information (RGB - Red, Green, Blue) with values ranging from 0 to 255. A 28×28 pixel greyscale image? That's a tensor of shape [28, 28]. A colour image? Shape [3, 28, 28] for the three colour channels. 









## Referencs

1. Simple Wikipedia  on [Tensor](https://simple.wikipedia.org/wiki/Tensor).
2. dev.to - [Tensor Basics: Types, Operations, and Applications in TensorFlow](https://dev.to/gdsclpu/tensor-basics-types-operations-and-applications-in-tensorflow-ill)
3. 0byte - [Intro to PyTorch](https://0byte.io/articles/pytorch_introduction.html?)
4. 