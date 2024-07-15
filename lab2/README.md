# Math 210: Lab \#2

## Example 1

Solve the following system:

$$
\begin{cases}
3x - 2y = 8 \\
x + 4y = -3
\end{cases}
$$

Augmented matrix

$$ \begin{pmatrix}
3 & -2 & | & 8 \\
1 & 4 & | & -3
\end{pmatrix} $$

Gauss-Jordan Elimination

$$ 3R2 - R1 \rightarrow R2 $$

$$ \begin{pmatrix}
3 & -2 & | & 8 \\
0 & 14 & | & -17
\end{pmatrix} $$

$$ \frac{1}{14}R2 \rightarrow R2 $$

$$ \begin{pmatrix}
3 & -2 & | & 8 \\
0 & 1 & | & -\frac{17}{14}
\end{pmatrix} $$

$$ R1 + 2R2 \rightarrow R1 $$

$$ \begin{pmatrix}
3 & 0 & | & \frac{39}{7} \\
0 & 1 & | & -\frac{17}{14}
\end{pmatrix} $$

$$ \frac{1}{3}R1 \rightarrow R1 $$

$$ \begin{pmatrix}
1 & 0 & | & \frac{13}{7} \\
0 & 1 & | & -\frac{17}{14}
\end{pmatrix} $$

$$
\begin{cases}
x = \frac{13}{7} \\
y = -\frac{17}{14}
\end{cases}
$$

``` python
import numpy as np

# Coefficients matrix
A1 = np.array([[3, -2],
               [1,  4]])

# Constants vector
B1 = np.array([8, -3])

# Solving the system
solution1 = np.linalg.solve(A1, B1)
print(solution1)
```

    ## [ 1.85714286 -1.21428571]

## Example 2

Solve the system simultaneously:

$$ \begin{cases}
3x - y + z = b_1 \\
-x + 2y + 3z = b_2 \\
x - 4z = b_3
\end{cases} $$

``` python
# Coefficients matrix
A2 = np.array([[ 3, -1,  1],
               [-1,  2,  3],
               [ 1,  0, -4]])
```

1)  

$$ \begin{cases}
b_1 = 1 \\
b_2 = -1 \\
b_3 = 7
\end{cases} $$

### a)

$$ \begin{cases}
3x - y + z = 1 \\
-x + 2y + 3z = -1 \\
x - 4z = 7
\end{cases} $$

Augmented matrix

$$ \begin{pmatrix}
3 & -1 & 1 & | & 1 \\
-1 & 2 & 3 & | & -1 \\
1 & 0 & -4 & | & 7
\end{pmatrix} $$

Gauss-Jordan Elimination

$$ R1 \leftrightarrow R3 $$

$$ \begin{pmatrix}
1 & 0 & -4 & | & 7 \\
-1 & 2 & 3 & | & -1 \\
3 & -1 & 1 & | & 1
\end{pmatrix} $$

$$ R1 + R2 \rightarrow R2 $$

$$ \begin{pmatrix}
1 & 0 & -4 & | & 7 \\
0 & 2 & -1 & | & 6 \\
3 & -1 & 1 & | & 1
\end{pmatrix} $$

$$ -3R1 + R3 \rightarrow R3 $$

$$ \begin{pmatrix}
1 & 0 & -4 & | & 7 \\
0 & 2 & -1 & | & 6 \\
0 & -1 & 13 & | & -20
\end{pmatrix} $$

$$ R2 + 2R3 \rightarrow R3 $$

$$ \begin{pmatrix}
1 & 0 & -4 & | & 7 \\
0 & 2 & -1 & | & 6 \\
0 & 0 & 25 & | & -34
\end{pmatrix} $$

$$ \frac{1}{25}R3 \rightarrow R3 $$

$$ \begin{pmatrix}
1 & 0 & -4 & | & 7 \\
0 & 2 & -1 & | & 6 \\
0 & 0 & 1 & | & -\frac{34}{25}
\end{pmatrix} $$

$$ R1 + 4R3 \rightarrow R1 $$

$$ \begin{pmatrix}
1 & 0 & 0 & | & \frac{39}{25} \\
0 & 2 & -1 & | & 6 \\
0 & 0 & 1 & | & -\frac{34}{25}
\end{pmatrix} $$

$$ R2 + R3 \rightarrow R2 $$

$$ \begin{pmatrix}
1 & 0 & 0 & | & \frac{39}{25} \\
0 & 2 & 0 & | & \frac{116}{25} \\
0 & 0 & 1 & | & -\frac{34}{25}
\end{pmatrix} $$

$$ \frac{1}{2}R2 \rightarrow R2 $$

$$ \begin{pmatrix}
1 & 0 & 0 & | & \frac{39}{25} \\
0 & 1 & 0 & | & \frac{58}{25} \\
0 & 0 & 1 & | & -\frac{34}{25}
\end{pmatrix} $$

$$
\begin{cases}
x = \frac{39}{25} \\
y = \frac{58}{25} \\
z = -\frac{34}{25}
\end{cases}
$$

``` python
# Constants vector for a)
B2a = np.array([1, -1, 7])

# Solving the system
solution2a = np.linalg.solve(A2, B2a)
print(solution2a)
```

    ## [ 1.56  2.32 -1.36]

2)  

$$ \begin{cases}
b_1 = -2 \\
b_2 = 3 \\
b_3 = 1
\end{cases} $$

### b)

$$ \begin{cases}
3x - y + z = -2 \\
-x + 2y + 3z = 3 \\
x - 4z = 1
\end{cases} $$

Augmented matrix

$$ \begin{pmatrix}
3 & -1 & 1 & | & -2 \\
-1 & 2 & 3 & | & 3 \\
1 & 0 & -4 & | & 1
\end{pmatrix} $$

Gauss-Jordan Elimination

$$ R1 \leftrightarrow R3 $$

$$
\begin{pmatrix}
1 & 0 & -4 & | & 1 \\
-1 & 2 & 3 & | & 3 \\
3 & -1 & 1 & | & -2
\end{pmatrix}
$$

$$ R1 + R2 \rightarrow R2 $$

$$
\begin{pmatrix}
1 & 0 & -4 & | & 1 \\
0 & 2 & -1 & | & 4 \\
3 & -1 & 1 & | & -2
\end{pmatrix}
$$

$$ -3R1 + R3 \rightarrow R3 $$

$$
\begin{pmatrix}
1 & 0 & -4 & | & 1 \\
0 & 2 & -1 & | & 4 \\
0 & -1 & 13 & | & -5
\end{pmatrix}
$$

$$ R2 + 2R3 \rightarrow R2 $$

$$
\begin{pmatrix}
1 & 0 & -4 & | & 1 \\
0 & 2 & -1 & | & 4 \\
0 & 0 & 25 & | & -34
\end{pmatrix}
$$

$$ \frac{1}{25}R3 \rightarrow R3 $$

$$
\begin{pmatrix}
1 & 0 & -4 & | & 1 \\
0 & 2 & -1 & | & 4 \\
0 & 0 & 1 & | & -\frac{6}{25}
\end{pmatrix}
$$

$$ R1 + 4R3 \rightarrow R1 $$

$$
\begin{pmatrix}
1 & 0 & 0 & | & \frac{1}{25} \\
0 & 2 & -1 & | & 4 \\
0 & 0 & 1 & | & -\frac{6}{25}
\end{pmatrix}
$$

$$ R2 + R3 \rightarrow R2 $$

$$
\begin{pmatrix}
1 & 0 & 0 & | & \frac{1}{25} \\
0 & 2 & 0 & | & \frac{47}{25} \\
0 & 0 & 1 & | & -\frac{6}{25}
\end{pmatrix}
$$

$$ \frac{1}{2}R2 \rightarrow R2 $$

$$
\begin{pmatrix}
1 & 0 & 0 & | & \frac{1}{25} \\
0 & 1 & 0 & | & \frac{47}{25} \\
0 & 0 & 1 & | & -\frac{6}{25}
\end{pmatrix}
$$

$$
\begin{cases}
x = \frac{1}{25} \\
y = \frac{47}{25} \\
z = -\frac{6}{25}
\end{cases}
$$

``` python
# Constants vector for b)
B2b = np.array([-2, 3, 1])

# Solving the system
solution2b = np.linalg.solve(A2, B2b)
print(solution2b)
```

    ## [ 0.04  1.88 -0.24]

## Practice 1

Solve the following systems of equations using the method from Example
1.

### a)

$$
3x_1 - 5x_2 = 7 \\
x_1 + 9x_2 = 11
$$

``` python
import numpy as np

# Coefficients matrix
A1a = np.array([[3, -5],
                [1, 9]])

# Constants vector
B1a = np.array([7, 11])

# Solving the system
solution1a = np.linalg.solve(A1a, B1a)
print("Solution for Practice 1a:", solution1a)
```

    ## Solution for Practice 1a: [3.6875 0.8125]

### b)

$$
3x_1 + 2x_2 - x_3 = 8 \\
2x_1 - 5x_2 + x_3 = 3 \\
6x_1 + x_3 = 2
$$

``` python
# Coefficients matrix
A1b = np.array([[ 3,  2, -1],
                [ 2, -5,  1],
                [ 6,  0,  1]])

# Constants vector
B1b = np.array([8, 3, 2])

# Solving the system
solution1b = np.linalg.solve(A1b, B1b)
print("Solution for Practice 1b:", solution1b)
```

    ## Solution for Practice 1b: [ 1.40540541 -1.32432432 -6.43243243]

## Practice 2

Solve the systems simultaneously using the method from Example 2.

$$
3x_1 + 2x_2 - x_3 = b_1 \\
2x_1 - 5x_2 + x_3 = b_2 \\
6x_1 + x_3 = b_3
$$

``` python
# Coefficients matrix
A2 = np.array([[ 3,  2, -1],
               [ 2, -5,  1],
               [ 6,  0,  1]])
```

### a) For $b_1 = 2$, $b_2 = 6$, $b_3 = 8$

``` python
# Constants vector for a)
B2a = np.array([2, 6, 8])

# Solving the system
solution2a = np.linalg.solve(A2, B2a)
print("Solution for Practice 2a:", solution2a)
```

    ## Solution for Practice 2a: [ 1.24324324 -0.59459459  0.54054054]

### b) For $b_1 = -2$, $b_2 = -6$, $b_3 = -8$

``` python
# Constants vector for b)
B2b = np.array([-2, -6, -8])

# Solving the system
solution2b = np.linalg.solve(A2, B2b)
print("Solution for Practice 2b:", solution2b)
```

    ## Solution for Practice 2b: [-1.24324324  0.59459459 -0.54054054]
