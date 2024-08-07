# Vectors

## The dot product

### Question 1

Given the following vectors, find: $\mathbf{u} = (2, 0, 1)$; $\mathbf{v} = (1, -2, 3)$

a) $\mathbf{u} \cdot \mathbf{v}$

b) The angle between $\mathbf{u}$ and $\mathbf{v}$

#### a) $\mathbf{u} \cdot \mathbf{v}$

$$
\begin{align}
\mathbf{u} \cdot \mathbf{v} &= 2 \times 1 + 0 \times (-2) + 1 \times 3 \\
&= 5
\end{align}
$$

#### b) The angle between $\mathbf{u}$ and $\mathbf{v}$

$$
\begin{align}
\|\mathbf{u}\| &= \sqrt{2^2 + 0^2 + 1^2} \\
&= \sqrt{5} \\
\\
\|\mathbf{v}\| &= \sqrt{1 + 4 + 9} \\
&= \sqrt{14} \\
\\
\cos \theta &= \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} \\
&= \frac{5}{\sqrt{5} \times \sqrt{14}} \\
&= \frac{\sqrt{70}}{14} \\
\\
\theta &= \cos^{-1} \left(\frac{\sqrt{70}}{14}\right)
\end{align}
$$

### Question 2

Given the following vectors, find: $\mathbf{u} = (2, 0, 1)$; $\mathbf{v} = (1, -2, 3)$

a) The projection of $\mathbf{u}$ on $\mathbf{v}$ along $\mathbf{v}$

b) The projection of $\mathbf{u}$ orthogonal to $\mathbf{v}$

#### a) The projection of $\mathbf{u}$ on $\mathbf{v}$ along $\mathbf{v}$

$$
\begin{align}
\mathbf{u} \cdot \mathbf{v} &= 2 \times 1 + 0 \times (-2) + 1 \times 3 \\
&= 5 \\
\\
\mathbf{v} \cdot \mathbf{v} &= 1^2 + (-2)^2 + 3^2 \\
&= 14 \\
\\
\text{proj}_{\mathbf{v}} \mathbf{u} &= \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}} \mathbf{v} \\
&= \frac{5}{14} \times (1, -2, 3) \\
&= \left( \frac{5}{14}, \frac{-5}{7}, \frac{15}{14} \right)
\end{align}
$$

#### b) The projection of $\mathbf{u}$ orthogonal to $\mathbf{v}$

$$
\begin{align}
\mathbf{u} - \text{proj}_{\mathbf{v}} \mathbf{u} &= (2, 0, 1) - \left( \frac{5}{14}, \frac{-5}{7}, \frac{15}{14} \right) \\
&= \left( \frac{23}{14}, \frac{5}{7}, \frac{-1}{14} \right)
\end{align}
$$

### Question 3

Given the following vectors, find: $\mathbf{u} = (2, 0, 1)$; $\mathbf{v} = (1, -2, 3)$

a) $3\mathbf{u} - \mathbf{v}$

b) Find values of $k$ for which: $\| k\mathbf{u} \| = 27$

#### a) $3\mathbf{u} - \mathbf{v}$

$$
\begin{align}
3\mathbf{u} - \mathbf{v} &= 3(2, 0, 1) - (1, -2, 3) \\
&= (5, 2, 0)
\end{align}
$$

#### b) Find values of $k$ for which $\| k\mathbf{u} \| = 27$

$$
\begin{align}
\| k\mathbf{u} \| &= 27 \\
\\
|k| \|\mathbf{u}\| &= 27 \\
\\
|k| \sqrt{5} &= 27 \\
\\
|k| &= \frac{27\sqrt{5}}{5} \\
\\
k &= \pm \frac{27\sqrt{5}}{5} \\
\end{align}
$$

## The cross product

Given the following vectors, find: $\mathbf{u} = (2, 0, 1)$; $\mathbf{v} = (1, -2, 3)$; $\mathbf{w} = (0, 1, 0)$; find:

a) $\mathbf{v} \times \mathbf{u}$

b) The area of a parallelogram constructed with the vectors $\mathbf{u}$ and $\mathbf{v}$

c) The volume of a parallelepiped constructed with vectors $\mathbf{u}$, $\mathbf{v}$, and $\mathbf{w}$ starting from the same initial point

d) $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$

#### a) $\mathbf{v} \times \mathbf{u}$

$$
\mathbf{v} \times \mathbf{u} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & -2 & 3 \\
2 & 0 & 1
\end{vmatrix}
$$

$$
= \mathbf{i} \left((-2)(1) - (3)(0)\right) - \mathbf{j} \left((1)(1) - (3)(2)\right) + \mathbf{k} \left((1)(0) - (-2)(2)\right)
$$

$$
= \mathbf{i} (-2) - \mathbf{j} (1 - 6) + \mathbf{k} (0 + 4)
$$

$$
= -2\mathbf{i} + 5\mathbf{j} + 4\mathbf{k} \\
= (-2, 5, 4)
$$

#### b) The area of a parallelogram constructed with the vectors $\mathbf{u}$ and $\mathbf{v}$

$$
\text{A} = \|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{v} \times \mathbf{u}\| = \|(-2, 5, 4)\| = \sqrt{(-2)^2 + 5^2 + 4^2} = 3\sqrt{5}
$$

#### c) The volume of a parallelepiped constructed with vectors $\mathbf{u}$, $\mathbf{v}$, and $\mathbf{w}$ starting from the same initial point

The volume of the parallelepiped is given by the scalar triple product $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$.

First, compute $\mathbf{v} \times \mathbf{w}$:

$$
\mathbf{v} \times \mathbf{w} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & -2 & 3 \\
0 & 1 & 0
\end{vmatrix}
$$

$$
= \mathbf{i} \left((-2)(0) - (3)(1)\right) - \mathbf{j} \left((1)(0) - (3)(0)\right) + \mathbf{k} \left((1)(1) - (-2)(0)\right)
$$

$$
= \mathbf{i} (0 - 3) - \mathbf{j} (0 - 0) + \mathbf{k} (1 + 0)
$$

$$
= -3\mathbf{i} + 0\mathbf{j} + 1\mathbf{k}
$$

$$
= (-3, 0, 1)
$$

Now compute $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$:

$$
\mathbf{u} \cdot (-3, 0, 1) = (2)(-3) + (0)(0) + (1)(1) = -6 + 0 + 1 = -5
$$

So, the volume of the parallelepiped is $|-5| = 5$.

#### d) $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$

From the previous part, we already calculated $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$:

$$
\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = -5
$$

Thus, $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = -5$.
