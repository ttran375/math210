# Math 210 - Introduction to SCILAB

## Practice

1. Given the following matrices, perform the operation:

$$
A =
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix}
$$

$$ B = \begin{pmatrix}
0 & 1 & 2 \\
-3 & 6 & 1 \\
7 & -23 & 0
\end{pmatrix}
$$

a) $A'$

b) $\text{trace}(B)$

c) $A \times B$

d) $B \times A$

e) $3A - B'$

f) $\text{inv}(B)$

g) $\text{rref}(A)$

h) $A^3$

j) $2B - 3I$

``` python
import numpy as np
from numpy.linalg import inv, matrix_rank

# Define matrices A and B
A = np.array([[1, 2, 0], [8, 1, 2], [0, -2, -43]])
B = np.array([[0, 1, 2], [-3, 6, 1], [7, -23, 0]])
```

### a) $A'$

$$
   A' = \begin{pmatrix}
   1 & 8 & 0 \\
   2 & 1 & -2 \\
   0 & 2 & -43
   \end{pmatrix}
$$

``` python
# a) Transpose of A
A_transpose = A.T
print(A_transpose)
```

    ## [[  1   8   0]
    ##  [  2   1  -2]
    ##  [  0   2 -43]]

### b) $\text{trace}(B)$

$$
   \text{trace}(B) = B_{11} + B_{22} + B_{33} = 0 + 6 + 0 = 6
$$

``` python
# b) Trace of B
B_trace = np.trace(B)
print(B_trace)
```

    ## 6

### c) $A \times B$

$$
\begin{align}
A \times B &=
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix}
\times
\begin{pmatrix}
0 & 1 & 2 \\
-3 & 6 & 1 \\
7 & -23 & 0
\end{pmatrix} \\
&=\begin{pmatrix}
1 \times 0 + 2 \times (-3) + 0 \times 7 & 1 \times 1 + 2 \times 6 + 0 \times (-23) & 1 \times 2 + 2 \times 1 + 0 \times 0 \\
8 \times 0 + 1 \times (-3) + 2 \times 7 & 8 \times 1 + 1 \times 6 + 2 \times (-23) & 8 \times 2 + 1 \times 1 + 2 \times 0 \\
0 \times 0 + (-2) \times (-3) + (-43) \times 7 & 0 \times 1 + (-2) \times 6 + (-43) \times (-23) & 0 \times 2 + (-2) \times 1 + (-43) \times 0
\end{pmatrix} \\
&=
\begin{pmatrix}
-6 & 13 & 4 \\
11 & -32 & 17 \\
-295 & 977 & -2
\end{pmatrix}
\end{align}
$$

``` python
# c) A * B
AB = np.dot(A, B)
print(AB)
```

    ## [[  -6   13    4]
    ##  [  11  -32   17]
    ##  [-295  977   -2]]

### d) $B \times A$

$$
\begin{align}
B \times A &=
\begin{pmatrix}
0 & 1 & 2 \\
-3 & 6 & 1 \\
7 & -23 & 0
\end{pmatrix}
\times
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix} \\
&=\begin{pmatrix}
0 \times 1 + 1 \times 8 + 2 \times 0 & 0 \times 2 + 1 \times 1 + 2 \times (-2) & 0 \times 0 + 1 \times 2 + 2 \times (-43) \\
-3 \times 1 + 6 \times 8 + 1 \times 0 & -3 \times 2 + 6 \times 1 + 1 \times (-2) & -3 \times 0 + 6 \times (-2) + 1 \times (-43) \\
7 \times 1 + (-23) \times 8 + 0 \times 0 & 7 \times 2 + (-23) \times 1 + 0 \times (-2) & 7 \times 0 + (-23) \times 2 + 0 \times (-43)
\end{pmatrix} \\
&= \begin{pmatrix}
8 & -3 & -84 \\
45 & -2 & -31 \\
-177 & -9 & -46
\end{pmatrix}
\end{align}
$$

``` python
# d) B * A
BA = np.dot(B, A)
print(BA)
```

    ## [[   8   -3  -84]
    ##  [  45   -2  -31]
    ##  [-177   -9  -46]]

### e) $3A - B'$

$$
3A = 3 \times \begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix} =
\begin{pmatrix} 3 & 6 & 0 \\
24 & 3 & 6 \\
0 & -6 & -129
\end{pmatrix}
$$

$$
B' = \begin{pmatrix}
0 & -3 & 7 \\
1 & 6 & -23 \\
2 & 1 & 0
\end{pmatrix}
$$

$$
3A - B' = \begin{pmatrix}
3 - 0 & 6 - (-3) & 0 - 7 \\
24 - 1 & 3 - 6 & 6 - (-23) \\
0 - 2 & -6 - 1 & -129 - 0
\end{pmatrix} =
\begin{pmatrix} 3 & 9 & -7 \\
23 & -3 & 29 \\
-2 & -7 & -129
\end{pmatrix}
$$

``` python
# e) 3A - B'
threeA_minus_B_transpose = 3 * A - B.T
print(threeA_minus_B_transpose)
```

    ## [[   3    9   -7]
    ##  [  23   -3   29]
    ##  [  -2   -7 -129]]

### f) $\text{inv}(B)$

$$
B = \begin{pmatrix}
0 & 1 & 2 \\
-3 & 6 & 1 \\
7 & -23 & 0
\end{pmatrix}
$$

Step 1: Calculate the Determinant of $B$

$$
\begin{align}
\text{det}(B) &= a(ei - fh) - b(di - fg) + c(dh - eg) \\
&= 0 \cdot (6 \cdot 0 - 1 \cdot (-23)) - 1 \cdot (-3 \cdot 0 - 1 \cdot 7) + 2 \cdot (-3 \cdot (-23) - 6 \cdot 7) \\
&= 61
\end{align}
$$

Since the determinant is non-zero, the matrix $B$ is invertible.

Step 2: Find the Adjugate of $B$

$$
\text{Minor}_{11} =
\begin{vmatrix}
6 & 1 \\
-23 & 0
\end{vmatrix} =
(6 \times 0) - (1 \times (-23))
= 23
$$

$$ \text{Cofactor}_{11} = (-1)^{1+1} \times 23 = 23 $$

$$
\text{Minor}_{12} =
\begin{vmatrix}
-3 & 1 \\
7 & 0
\end{vmatrix} =
(-3 \times 0) - (1 \times 7)
= -7
$$

$$ \text{Cofactor}_{12} = (-1)^{1+2} \times (-7) = 7 $$

$$
\text{Minor}_{13} =
\begin{vmatrix}
-3 & 6 \\
7 & -23
\end{vmatrix} =
(-3 \times (-23)) - (6 \times 7)
= 27
$$

$$ \text{Cofactor}_{13} = (-1)^{1+3} \times 27 = 27 $$

$$
\text{Minor}_{21} =
\begin{vmatrix}
1 & 2 \\
-23 & 0
\end{vmatrix} =
(1 \times 0) - (2 \times (-23))
= 46
$$

$$ \text{Cofactor}_{21} = (-1)^{2+1} \times 46 = -46 $$

$$
\text{Minor}_{22} =
\begin{vmatrix}
0 & 2 \\
7 & 0
\end{vmatrix} =
(0 \times 0) - (2 \times 7)
= -14
$$

$$ \text{Cofactor}_{22} = (-1)^{2+2} \times (-14) = -14 $$

$$
\text{Minor}_{23} =
\begin{vmatrix}
0 & 1 \\
7 & -23
\end{vmatrix} =
(0 \times (-23)) - (1 \times 7)
= -7
$$

$$ \text{Cofactor}_{23} = (-1)^{2+3} \times (-7) = 7 $$

$$
\text{Minor}_{31} =
\begin{vmatrix}
1 & 2 \\
6 & 1
\end{vmatrix} =
(1 \times 1) - (2 \times 6)
= -11
$$

$$ \text{Cofactor}_{31} = (-1)^{3+1} \times (-11) = -11 $$

$$
\text{Minor}_{32} =
\begin{vmatrix}
0 & 2 \\
-3 & 1
\end{vmatrix} =
(0 \times 1) - (2 \times (-3))
= 6
$$

$$ \text{Cofactor}_{32} = (-1)^{3+2} \times 6 = -6 $$

$$
\text{Minor}_{33} =
\begin{vmatrix}
0 & 1 \\
-3 & 6
\end{vmatrix} =
(0 \times 6) - (1 \times (-3))
= 3
$$

$$ \text{Cofactor}_{33} = (-1)^{3+3} \times 3 = 3 $$

$$
\text{Cofactor Matrix} =
\begin{pmatrix}
23 & 7 & 27 \\
-46 & -14 & 7 \\
-11 & -6 & 3
\end{pmatrix}
$$

$$ \text{Adjugate}(B) = \text{Transpose}(\text{Cofactor Matrix}) =
\begin{pmatrix}
23 & -46 & -11 \\
7 & -14 & -6 \\
27 & 7 & 3 \end{pmatrix}
$$

Step 3: Calculate the Inverse of $B$

$$
\begin{align}
B^{-1} &= \frac{1}{\text{det}(B)} \times \text{Adjugate}(B) \\
&= \frac{1}{61} \times
\begin{pmatrix}
23 & -46 & -11 \\
7 & -14 & -6 \\
27 & 7 & 3
\end{pmatrix} \\
&=
\begin{pmatrix}
\frac{23}{61} & \frac{-46}{61} & \frac{-11}{61} \\
\frac{7}{61} & \frac{-14}{61} & \frac{-6}{61} \\
\frac{27}{61} & \frac{7}{61} & \frac{3}{61}
\end{pmatrix}
\end{align}
$$

``` python
# f) Inverse of B
B_inv = inv(B)
print(B_inv)
```

    ## [[ 0.37704918 -0.75409836 -0.18032787]
    ##  [ 0.1147541  -0.2295082  -0.09836066]
    ##  [ 0.44262295  0.1147541   0.04918033]]

### g) $\text{rref}(A)$

$$
A =
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix}
$$

$$ R2 - 8R1 \rightarrow R2 $$

$$
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix} \rightarrow
\begin{pmatrix}
1 & 2 & 0 \\
0 & -15 & 2 \\
0 & -2 & -43
\end{pmatrix}
$$

$$ -\frac{1}{15}R2 \rightarrow R2 $$

$$
\begin{pmatrix}
1 & 2 & 0 \\
0 & -15 & 2 \\
0 & -2 & -43
\end{pmatrix} \rightarrow
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & -\frac{2}{15} \\
0 & -2 & -43
\end{pmatrix}
$$

$$ R1 - 2R2 \rightarrow R1 $$

$$
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & -\frac{2}{15} \\
0 & -2 & -43
\end{pmatrix} \rightarrow
\begin{pmatrix}
1 & 0 & \frac{4}{15} \\
0 & 1 & -\frac{2}{15} \\
0 & -2 & -43
\end{pmatrix}
$$

$$ R3 + 2R2 \rightarrow R3 $$

$$
\begin{pmatrix}
1 & 0 & \frac{4}{15} \\
0 & 1 & -\frac{2}{15} \\
0 & -2 & -43
\end{pmatrix} \rightarrow
\begin{pmatrix}
1 & 0 & \frac{4}{15} \\
0 & 1 & -\frac{2}{15} \\
0 & 0 & -\frac{647}{15}
\end{pmatrix}
$$

$$ -\frac{15}{647}R3 \rightarrow R3 $$

$$
\begin{pmatrix}
1 & 0 & \frac{4}{15} \\
0 & 1 & -\frac{2}{15} \\
0 & 0 & -\frac{647}{15}
\end{pmatrix} \rightarrow
\begin{pmatrix}
1 & 0 & \frac{4}{15} \\
0 & 1 & -\frac{2}{15} \\
0 & 0 & 1
\end{pmatrix}
$$

$$ R1 - \frac{4}{15}R3 \rightarrow R1 $$

$$
\begin{pmatrix}
1 & 0 & \frac{4}{15} \\
0 & 1 & -\frac{2}{15} \\
0 & 0 & 1
\end{pmatrix} \rightarrow
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & -\frac{2}{15} \\
0 & 0 & 1
\end{pmatrix}
$$

$$ R2 + \frac{2}{15}R3 \rightarrow R2 $$

$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & -\frac{2}{15} \\
0 & 0 & 1
\end{pmatrix} \rightarrow
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

$$ \text{rref}(A) =
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

``` python
# g) Reduced Row Echelon Form of A
# Note: numpy does not have rref, we need to implement it or use sympy
from sympy import Matrix
A_rref, _ = Matrix(A).rref()
print(np.array(A_rref))
```

    ## [[1 0 0]
    ##  [0 1 0]
    ##  [0 0 1]]

### h) $A^3$

$$
\begin{align}
A^2 &=
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix} \times
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix} \\
&= \begin{pmatrix}
1 \times 1 + 2 \times 8 + 0 \times 0 & 1 \times 2 + 2 \times 1 + 0 \times -2 & 1 \times 0 + 2 \times 2 + 0 \times -43 \\
8 \times 1 + 1 \times 8 + 2 \times 0 & 8 \times 2 + 1 \times 1 + 2 \times -2 & 8 \times 0 + 1 \times 2 + 2 \times -43 \\
0 \times 1 + (-2) \times 8 + (-43) \times 0 & 0 \times 2 + (-2) \times 1 + (-43) \times -2 & 0 \times 0 + (-2) \times 2 + (-43) \times -43
\end{pmatrix} \\
&= \begin{pmatrix}
17 & 4 & 4 \\
16 & 13 & -84 \\
-16 & 84 & 1845
\end{pmatrix}
\end{align}
$$

$$
\begin{align}
A^3 &= A \times A^2 \\
&=
\begin{pmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{pmatrix} \times
\begin{pmatrix}
17 & 4 & 4 \\
16 & 13 & -84 \\
-16 & 84 & 1845
\end{pmatrix} \\
&= \begin{pmatrix}
(1 \times 17 + 2 \times 16 + 0 \times -16 & 1 \times 4 + 2 \times 13 + 0 \times 84 & 1 \times 4 + 2 \times -84 + 0 \times 1845) \\
(8 \times 17 + 1 \times 16 + 2 \times -16 & 8 \times 4 + 1 \times 13 + 2 \times 84 & 8 \times 4 + 1 \times -84 + 2 \times 1845) \\
(0 \times 17 + (-2) \times 16 + (-43) \times -16 & 0 \times 4 + (-2) \times 13 + (-43) \times 84 & 0 \times 4 + (-2) \times -84 + (-43) \times 1845)
\end{pmatrix} \\
&= \begin{pmatrix}
49 & 30 & -164 \\
120 & 213 & 3638 \\
656 & -3638 & -79167
\end{pmatrix}
\end{align}
$$

``` python
# e) A^3
A_cubed = np.linalg.matrix_power(A, 3)
print(A_cubed)
```

    ## [[    49     30   -164]
    ##  [   120    213   3638]
    ##  [   656  -3638 -79167]]

### j) $2B - 3I$

$$
\begin{align}
2B - 3I &= 2 \times
\begin{pmatrix}
0 & 1 & 2 \\
-3 & 6 & 1 \\
7 & -23 & 0
\end{pmatrix} - 3 \times
\begin{pmatrix} 1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix}
0 & 2 & 4 \\
-6 & 12 & 2 \\
14 & -46 & 0
\end{pmatrix} -
\begin{pmatrix}
3 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 3 \end{pmatrix} \\
&=
\begin{pmatrix}
-3 & 2 & 4 \\
-6 & 9 & 2 \\
14 & -46 & -3
\end{pmatrix}
\end{align}
$$

``` python
# f) 2B - 3I
I = np.eye(B.shape[0])
twoB_minus_threeI = 2 * B - 3 * I
print(twoB_minus_threeI)
```

    ## [[ -3.   2.   4.]
    ##  [ -6.   9.   2.]
    ##  [ 14. -46.  -3.]]
