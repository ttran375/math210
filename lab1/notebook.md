# Math 210 - Introduction to SCILAB

## Startup Execution

Loading initial environment

## Operations with Numbers

1. **Addition** – use `+`
2. **Subtraction** – use `-`
3. **Multiplication** – use `*`
4. **Powers** – use `^`
5. **Division** – use `/`

### Examples

``` scilab
--> 3 + 5
ans =
8.

--> 3 * 5
ans =
15.

--> 2 ^ 4
ans =
16.

--> ceil(2.3)
ans =
3.

--> floor(4.7)
ans =
4.
```

## Matrices and Operations with Matrices

### Writing a Matrix

Name the matrix using a letter. Use brackets. Use a semicolon after each
row.

### Example

``` scilab
--> A = [3 4 5; 0 1 2; -1 2 7]
A =
3. 4. 5.
0. 1. 2.
-1. 2. 7.

--> B = [0 -1 -2; -3 0 2; 7 8 9]
B =
0. -1. -2.
-3. 0. 2.
7. 8. 9.
```

### Operations with Matrices

Use the same symbols as for the operations with numbers.

``` scilab
--> A + B
ans =
3. 3. 3.
-3. 1. 4.
6. 10. 16.

--> A * B
ans =
23. 37. 47.
11. 16. 20.
43. 57. 69.

--> A - B
ans =
3. 5. 7.
3. 1. 0.
-8. -6. -2.
```

### The Inverse of a Matrix

``` scilab
--> inv(A)
ans =
0.5 -3. 0.5
-0.3333333 4.3333333 -1.
0.1666667 -1.6666667 0.5

--> inv(A) * A
ans =
1. 2.220D-16 8.882D-16
0. 1. 0.
0. 1.110D-16 1.
```

Clean command will restore the matrix to the identity matrix (see
below).

``` scilab
--> clean(inv(A) * A)
ans =
1. 0. 0.
0. 1. 0.
0. 0. 1.
```

### Transpose of a Matrix

``` scilab
--> A'
ans =
3. 0. -1.
4. 1. 2.
5. 2. 7.
```

### Trace of a Matrix

``` scilab
--> trace(A)
ans =
11.
```

### Solving Systems of Linear Equations by Applying the Reduced Row Echelon Command to the Augmented Matrix Associated with the System

``` scilab
--> C = [2 3 4 1; 0 2 5 6; 3 -1 -2 2]
C =
2. 3. 4. 1.
0. 2. 5. 6.
3. -1. -2. 2.

--> rref(C)
ans =
1. 0. 0. 1.173913
0. 1. 0. -4.3913043
0. 0. 1. 2.9565217
```

The solution of the system can be found in the last column of the matrix
above.

## Practice

1. Given the following matrices, perform the operation:

    $A = \begin{bmatrix} 1 & 2 & 0 \\ 8 & 1 & 2 \\ 0 & -2 & -43 \end{bmatrix}$,
    $B = \begin{bmatrix} 0 & 1 & 2 \\ -3 & 6 & 1 \\ 7 & -23 & 0 \end{bmatrix}$

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

``` python
# d) B * A
BA = np.dot(B, A)
print(BA)
```

    ## [[   8   -3  -84]
    ##  [  45   -2  -31]
    ##  [-177   -9  -46]]

``` python
# e) 3A - B'
threeA_minus_B_transpose = 3 * A - B.T
print(threeA_minus_B_transpose)
```

    ## [[   3    9   -7]
    ##  [  23   -3   29]
    ##  [  -2   -7 -129]]

``` python
# f) Inverse of B
B_inv = inv(B)
print(B_inv)
```

    ## [[ 0.37704918 -0.75409836 -0.18032787]
    ##  [ 0.1147541  -0.2295082  -0.09836066]
    ##  [ 0.44262295  0.1147541   0.04918033]]

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

``` python
# e) A^3
A_cubed = np.linalg.matrix_power(A, 3)
print(A_cubed)
```

    ## [[    49     30   -164]
    ##  [   120    213   3638]
    ##  [   656  -3638 -79167]]

``` python
# f) 2B - 3I
I = np.eye(B.shape[0])
twoB_minus_threeI = 2 * B - 3 * I
print(twoB_minus_threeI)
```

    ## [[ -3.   2.   4.]
    ##  [ -6.   9.   2.]
    ##  [ 14. -46.  -3.]]
