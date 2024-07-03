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

### f) $\text{inv}(B)$

$$ B = \begin{bmatrix} 0 & 1 & 2 \\ -3 & 6 & 1 \\ 7 & -23 & 0 \end{bmatrix} $$

$$ 
\begin{align}
\text{det}(B) &= a(ei - fh) - b(di - fg) + c(dh - eg) \\ 
&= 0 \cdot (6 \cdot 0 - 1 \cdot (-23)) - 1 \cdot (-3 \cdot 0 - 1 \cdot 7) + 2 \cdot (-3 \cdot (-23) - 6 \cdot 7) \\
&= 61
\end{align}
$$

Since the determinant is non-zero, the matrix $B$ is invertible.

Step 2: Find the Adjugate of $B$

The adjugate of $B$, denoted as $\text{adj}(B)$, is the transpose of the cofactor matrix of $B$. To find the cofactors, we need to calculate the minors for each element in $B$.

Calculate Cofactors for Each Element

**Cofactor of $b_{11}$ (top left):**
$$ \text{Minor}_{11} = \begin{vmatrix} 6 & 1 \\ -23 & 0 \end{vmatrix} = (6 \cdot 0) - (1 \cdot (-23)) = 0 + 23 = 23 $$
$$ \text{Cofactor}_{11} = (-1)^{1+1} \cdot 23 = 23 $$

**Cofactor of $b_{12}$ (top middle):**
$$ \text{Minor}_{12} = \begin{vmatrix} -3 & 1 \\ 7 & 0 \end{vmatrix} = (-3 \cdot 0) - (1 \cdot 7) = 0 - 7 = -7 $$
$$ \text{Cofactor}_{12} = (-1)^{1+2} \cdot (-7) = 7 $$

**Cofactor of $b_{13}$ (top right):**
$$ \text{Minor}_{13} = \begin{vmatrix} -3 & 6 \\ 7 & -23 \end{vmatrix} = (-3 \cdot (-23)) - (6 \cdot 7) = 69 - 42 = 27 $$
$$ \text{Cofactor}_{13} = (-1)^{1+3} \cdot 27 = 27 $$

**Cofactor of $b_{21}$ (middle left):**
$$ \text{Minor}_{21} = \begin{vmatrix} 1 & 2 \\ -23 & 0 \end{vmatrix} = (1 \cdot 0) - (2 \cdot (-23)) = 0 + 46 = 46 $$
$$ \text{Cofactor}_{21} = (-1)^{2+1} \cdot 46 = -46 $$

**Cofactor of $b_{22}$ (middle middle):**
$$ \text{Minor}_{22} = \begin{vmatrix} 0 & 2 \\ 7 & 0 \end{vmatrix} = (0 \cdot 0) - (2 \cdot 7) = 0 - 14 = -14 $$
$$ \text{Cofactor}_{22} = (-1)^{2+2} \cdot (-14) = -14 $$

**Cofactor of $b_{23}$ (middle right):**
$$ \text{Minor}_{23} = \begin{vmatrix} 0 & 1 \\ 7 & -23 \end{vmatrix} = (0 \cdot (-23)) - (1 \cdot 7) = 0 - 7 = -7 $$
$$ \text{Cofactor}_{23} = (-1)^{2+3} \cdot (-7) = 7 $$

**Cofactor of $b_{31}$ (bottom left):**
$$ \text{Minor}_{31} = \begin{vmatrix} 1 & 2 \\ 6 & 1 \end{vmatrix} = (1 \cdot 1) - (2 \cdot 6) = 1 - 12 = -11 $$
$$ \text{Cofactor}_{31} = (-1)^{3+1} \cdot (-11) = -11 $$

**Cofactor of $b_{32}$ (bottom middle):**
$$ \text{Minor}_{32} = \begin{vmatrix} 0 & 2 \\ -3 & 1 \end{vmatrix} = (0 \cdot 1) - (2 \cdot (-3)) = 0 + 6 = 6 $$
$$ \text{Cofactor}_{32} = (-1)^{3+2} \cdot 6 = -6 $$

**Cofactor of $b_{33}$ (bottom right):**
$$ \text{Minor}_{33} = \begin{vmatrix} 0 & 1 \\ -3 & 6 \end{vmatrix} = (0 \cdot 6) - (1 \cdot (-3)) = 0 + 3 = 3 $$
$$ \text{Cofactor}_{33} = (-1)^{3+3} \cdot 3 = 3 $$

Construct the Cofactor Matrix
$$ \text{Cofactor Matrix} = \begin{bmatrix} 23 & 7 & 27 \\ -46 & -14 & 7 \\ -11 & -6 & 3 \end{bmatrix} $$

Transpose the Cofactor Matrix to get the Adjugate
$$ \text{Adjugate}(B) = \text{Transpose}(\text{Cofactor Matrix}) = \begin{bmatrix} 23 & -46 & -11 \\ 7 & -14 & -6 \\ 27 & 7 & 3 \end{bmatrix} $$

Step 3: Calculate the Inverse of $B$

The inverse of $B$ is given by:

$$ B^{-1} = \frac{1}{\text{det}(B)} \cdot \text{Adjugate}(B) $$

We found $\text{det}(B) = 61$ and the adjugate matrix is:

$$ \text{Adjugate}(B) = \begin{bmatrix} 23 & -46 & -11 \\ 7 & -14 & -6 \\ 27 & 7 & 3 \end{bmatrix} $$

Therefore:

$$ B^{-1} = \frac{1}{61} \begin{bmatrix} 23 & -46 & -11 \\ 7 & -14 & -6 \\ 27 & 7 & 3 \end{bmatrix} $$

$$ B^{-1} = \begin{bmatrix} \frac{23}{61} & \frac{-46}{61} & \frac{-11}{61} \\ \frac{7}{61} & \frac{-14}{61} & \frac{-6}{61} \\ \frac{27}{61} & \frac{7}{61} & \frac{3}{61} \end{bmatrix} $$

Final Answer:

$$ B^{-1} = \begin{bmatrix} \frac{23}{61} & \frac{-46}{61} & \frac{-11}{61} \\ \frac{7}{61} & \frac{-14}{61} & \frac{-6}{61} \\ \frac{27}{61} & \frac{7}{61} & \frac{3}{61} \end{bmatrix} $$

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
