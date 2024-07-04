# Math 210 - Introduction to SCILAB

## Practice

1. Given the following matrices, perform the operation:

$$
A = 
\begin{bmatrix}
1 & 2 & 0 \\
8 & 1 & 2 \\
0 & -2 & -43
\end{bmatrix}
$$

$$ B = \begin{bmatrix}
0 & 1 & 2 \\
-3 & 6 & 1 \\
7 & -23 & 0
\end{bmatrix} $$

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
   A' = \begin{bmatrix}
   1 & 8 & 0 \\
   2 & 1 & -2 \\
   0 & 2 & -43
   \end{bmatrix}
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
\begin{bmatrix}
1 \times 0 + 2 \times (-3) + 0 \times 7 & 1 \times 1 + 2 \times 6 + 0 \times (-23) & 1 \times 2 + 2 \times 1 + 0 \times 0 \\
8 \times 0 + 1 \times (-3) + 2 \times 7 & 8 \times 1 + 1 \times 6 + 2 \times (-23) & 8 \times 2 + 1 \times 1 + 2 \times 0 \\
0 \times 0 + (-2) \times (-3) + (-43) \times 7 & 0 \times 1 + (-2) \times 6 + (-43) \times (-23) & 0 \times 2 + (-2) \times 1 + (-43) \times 0
\end{bmatrix} \\
&=
\begin{bmatrix}
-6 & 13 & 4 \\
11 & -32 & 17 \\
-295 & 977 & -2
\end{bmatrix}
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
B \times A &= \begin{bmatrix}
0 \times 1 + 1 \times 8 + 2 \times 0 & 0 \times 2 + 1 \times 1 + 2 \times (-2) & 0 \times 0 + 1 \times 2 + 2 \times (-43) \\
-3 \times 1 + 6 \times 8 + 1 \times 0 & -3 \times 2 + 6 \times 1 + 1 \times (-2) & -3 \times 0 + 6 \times (-2) + 1 \times (-43) \\
7 \times 1 + (-23) \times 8 + 0 \times 0 & 7 \times 2 + (-23) \times 1 + 0 \times (-2) & 7 \times 0 + (-23) \times 2 + 0 \times (-43)
\end{bmatrix} \\
&= \begin{bmatrix}
8 & -3 & -84 \\
45 & -2 & -31 \\
-177 & -9 & -46
\end{bmatrix}
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
3A = 3 \times \begin{bmatrix} 1 & 2 & 0 \\ 8 & 1 & 2 \\ 0 & -2 & -43 \end{bmatrix} = \begin{bmatrix} 3 & 6 & 0 \\ 24 & 3 & 6 \\ 0 & -6 & -129 \end{bmatrix}
$$

$$
B' = \begin{bmatrix} 0 & -3 & 7 \\ 1 & 6 & -23 \\ 2 & 1 & 0 \end{bmatrix}
$$

$$
3A - B' = \begin{bmatrix} 3 - 0 & 6 - (-3) & 0 - 7 \\ 24 - 1 & 3 - 6 & 6 - (-23) \\ 0 - 2 & -6 - 1 & -129 - 0 \end{bmatrix} = \begin{bmatrix} 3 & 9 & -7 \\ 23 & -3 & 29 \\ -2 & -7 & -129 \end{bmatrix}
$$

``` python
# e) 3A - B'
threeA_minus_B_transpose = 3 * A - B.T
print(threeA_minus_B_transpose)
```

    ## [[   3    9   -7]
    ##  [  23   -3   29]
    ##  [  -2   -7 -129]]
