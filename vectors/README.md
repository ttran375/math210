# Vectors. The dot product

## Question 1

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

## Question 2

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

## Question 3

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
