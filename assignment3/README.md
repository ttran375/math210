---
output: pdf_document
---

# MATH 210 - Assignment 3 - Summer 2024

For full marks, provide detailed solutions. Complete questions 4, 5, and 6 using SCILAB. Late assignments submitted within 24 hours after the due date will be penalized by 25%. After 24 hours, no assignments will be accepted.

## 1. Solve the System of Linear Equations [5 marks]

A system of linear equations was reduced to the form below. Continue to use Jordan-Gauss elimination to fully solve the system. Show all steps.

$$
\left( \begin{array}{ccc|c}
1 & -1 & 5 & -6 \\
0 & 1 & \frac{1}{2} & \frac{3}{2} \\
0 & 3 & -13 & 19 \\
\end{array} \right)
$$

1. $R3 = R3 - 3R2$

$$
\left( \begin{array}{ccc|c}
1 & -1 & 5 & -6 \\
0 & 1 & \frac{1}{2} & \frac{3}{2} \\
0 & 0 & -\frac{29}{2} & \frac{29}{2}
\end{array} \right)
$$

2. $R3 = -\frac{2}{29} \times R3$

$$
\left( \begin{array}{ccc|c}
1 & -1 & 5 & -6 \\
0 & 1 & \frac{1}{2} & \frac{3}{2} \\
0 & 0 & 1 & -1
\end{array} \right)
$$

3. $R1 = R1 - 5R3$

$$
\left( \begin{array}{ccc|c}
1 & -1 & 0 & -1 \\
0 & 1 & \frac{1}{2} & \frac{3}{2} \\
0 & 0 & 1 & -1
\end{array} \right)
$$

4. $R2 = R2 - \frac{1}{2}R3$

$$
\left( \begin{array}{ccc|c}
1 & -1 & 0 & -1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & -1
\end{array} \right)
$$

5. $R1 = R1 + R2$

$$
\left( \begin{array}{ccc|c}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & -1
\end{array} \right)
$$

Thus, the solution is:

$$
\begin{cases}
x = 1 \\
y = 2 \\
z = -1
\end{cases}
$$


## 2. Solve the Homogeneous System of Linear Equations [5 marks]

For the following system of homogeneous linear equations:

$$
\begin{cases}
x - 2y + 3z = 0 \\
2x + 3y - 7z = 0
\end{cases}
$$

Use elementary row operations to solve the above system. Identify the free variable(s) if any.

1. $R2 = R2 - 2R1$

$$
\left( \begin{array}{ccc|c}
1 & -2 & 3 & 0 \\
0 & 7 & -13 & 0
\end{array} \right)
$$

2. $R2 = \frac{1}{7}R2$

$$
\left( \begin{array}{ccc|c}
1 & -2 & 3 & 0 \\
0 & 1 & -\frac{13}{7} & 0
\end{array} \right)
$$

3. $R1 = R1 + 2R2$

$$
\left( \begin{array}{ccc|c}
1 & 0 & -\frac{5}{7} & 0 \\
0 & 1 & -\frac{13}{7} & 0
\end{array} \right)
$$

Solving the system of equations:

$$
x - \frac{5}{7}z = 0 \quad \rightarrow \quad x = \frac{5}{7}z
$$

$$
y - \frac{13}{7}z = 0 \quad \rightarrow \quad y = \frac{13}{7}z
$$

Therefore, $z$ can take any value, so it is a free variable:

$$
\begin{cases}
x = \frac{5}{7}t \\
y = \frac{13}{7}t \\
z = t
\end{cases}
$$


## 3. Matrix Operations [12 marks]

Given the following matrices:

$$A = \begin{bmatrix}
  3 & 0 & 2 \\
  -2 & 1 & -1 
\end{bmatrix},
B = \begin{bmatrix}
  -2 & 3 \\
  4 & 0 
\end{bmatrix},
C = \begin{bmatrix}
  3 & 1 & 2 \\
  -1 & 0 & 4 \\
  5 & -2 & 3 
\end{bmatrix},
D = \begin{bmatrix}
  1 & 4 \\
  3 & 0 \\
  1 & -3 
\end{bmatrix},
E = \begin{bmatrix}
  1 & 2 \\
  0 & -3 
\end{bmatrix}$$

### (a) $2A \times D$

$$ 2A = 2 \times \begin{bmatrix}
  3 & 0 & 2 \\
  -2 & 1 & -1 
\end{bmatrix} = \begin{bmatrix}
  6 & 0 & 4 \\
  -4 & 2 & -2 
\end{bmatrix} $$

$$ 2A \times D = \begin{bmatrix}
  6 & 0 & 4 \\
  -4 & 2 & -2 
\end{bmatrix} \times \begin{bmatrix}
  1 & 4 \\
  3 & 0 \\
  1 & -3 
\end{bmatrix} = \begin{bmatrix}
  6 \times 1 + 0 \times 3 + 4 \times 1 & 6 \times 4 + 0 \times 0 + 4 \times (-3) \\
  -4 \times 1 + 2 \times 3 + (-2) \times 1 & -4 \times 4 + 2 \times 0 + (-2) \times (-3) 
\end{bmatrix} = \begin{bmatrix}
  10 & 12 \\
  0 & -10 
\end{bmatrix} $$

### (b) $C^T$

$$ C^T = \begin{bmatrix}
  3 & -1 & 5 \\
  1 & 0 & -2 \\
  2 & 4 & 3 
\end{bmatrix} $$

### (c) $g(B)$ where $g(x) = 3 - 2x^2$

$$ B^2 = \begin{bmatrix}
  -2 & 3 \\
  4 & 0 
\end{bmatrix} \times \begin{bmatrix}
  -2 & 3 \\
  4 & 0 
\end{bmatrix} = \begin{bmatrix}
  -2 \times -2 + 3 \times 4 & -2 \times 3 + 3 \times 0 \\
  4 \times -2 + 0 \times 4 & 4 \times 3 + 0 \times 0 
\end{bmatrix} = \begin{bmatrix}
  16 & -6 \\
  -8 & 12 
\end{bmatrix} $$

$$ 3 - 2B^2 = 3 - 2 \times \begin{bmatrix}
  16 & -6 \\
  -8 & 12 
\end{bmatrix} = 3 - \begin{bmatrix}
  32 & -12 \\
  -16 & 24 
\end{bmatrix} = \begin{bmatrix}
  3 - 32 & 3 + 12 \\
  3 + 16 & 3 - 24 
\end{bmatrix} = \begin{bmatrix}
  -29 & 15 \\
  19 & -21 
\end{bmatrix} $$

### (d) $B + 3E^T$

$$ E^T = \begin{bmatrix}
  1 & 0 \\
  2 & -3 
\end{bmatrix} \rightarrow 3E^T = 3 \times \begin{bmatrix}
  1 & 0 \\
  2 & -3 
\end{bmatrix} = \begin{bmatrix}
  3 & 0 \\
  6 & -9 
\end{bmatrix} $$

$$ B + 3E^T = \begin{bmatrix}
  -2 & 3 \\
  4 & 0 
\end{bmatrix} + \begin{bmatrix}
  3 & 0 \\
  6 & -9 
\end{bmatrix} = \begin{bmatrix}
  -2 + 3 & 3 + 0 \\
  4 + 6 & 0 + (-9) 
\end{bmatrix} = \begin{bmatrix}
  1 & 3 \\
  10 & -9 
\end{bmatrix} $$

## 4. Use SCILAB to solve the following system of equations and attach SCILAB output.

$$
\begin{cases} 
2x - y + 7z - w = 20 \\
x + 3y + z - 3w = 12 \\
x - 3z + 5w = -14 \\
2x + y + 4z - w = 13 
\end{cases} 
$$
```{python}
# Import necessary library for matrix operations
import numpy as np

# Define the coefficient matrix A and the constant vector b for Question 4
A1 = np.array([[2, -1, 7, -1],
               [1, 3, 1, -3],
               [1, 0, -3, 5],
               [2, 1, 4, -1]])

b1 = np.array([20, 12, -14, 13])

# Solve for x using numpy's linear algebra solver
x1 = np.linalg.solve(A1, b1)

# Display the solution
print('Solution for Question 4:')
print(x1)
```

## 5. Use SCILAB to solve the following systems simultaneously and attach SCILAB output.

$$
\begin{cases} 
x - 2y + 4z = a_1 \\
5x + 3y + z = a_2 \\
6x - 2y - 4z = a_3 
\end{cases} 
$$

### a)

$$a_1 = 1, \quad a_2 = 0, \quad a_3 = -\frac{1}{4} $$
```{python}
# Define the coefficient matrix A for Question 5
A2 = np.array([[1, -2, 4],
               [5, 3, 1],
               [6, -2, -4]])

# Define the constants vector b for part (a)
b_a = np.array([1, 0, -1/4])

# Solve for x using numpy's linear algebra solver
x_a = np.linalg.solve(A2, b_a)

# Display the solution
print('Solution for part (a) of Question 5:')
print(x_a)
```

### b)

$$a_1 = 5, \quad a_2 = 1, \quad a_3 = -2 $$
```{python}
# Define the constants vector b for part (b)
b_b = np.array([5, 1, -2])

# Solve for x using numpy's linear algebra solver
x_b = np.linalg.solve(A2, b_b)

# Display the solution
print('Solution for part (b) of Question 5:')
print(x_b)
```

## 6. Use SCILAB to solve the following systems simultaneously and attach SCILAB output.

$$A = \begin{bmatrix} 
1 & 0 & 0 \\ 
0 & -1 & 0 \\ 
0 & 0 & -1 
\end{bmatrix} $$

$$B = \begin{bmatrix} 
-\frac{5}{7} & 7 & -12 \\ 
-1 & 0 & -5 \\ 
3 & -36 & \frac{7}{11} 
\end{bmatrix} $$

$$D = \begin{bmatrix} 
\frac{4}{5} & -1 \\ 
1 & -4 \\ 
0 & 34 
\end{bmatrix} $$

```{python}
# Define the matrices A and B for Question 6
A3 = np.array([[1, 0, 0],
               [0, -1, 0],
               [0, 0, -1]])

B = np.array([[-5/7, 7, -12],
              [-1, 0, -5],
              [3, -36, 7/11]])
```

### a)

$$(A \times B)^T $$
```{python}
# Compute the product A * B
C = np.dot(A3, B)

# Compute the transpose of the result
C_T = C.T

# Display the result
print('Result of (A * B)^T:')
print(C_T)
```

### b)

$$B^T \times D $$
```{python}
# Define the matrix D
D = np.array([[4/5, -1],
              [1, -4],
              [0, 34]])

# Compute the transpose of B
B_T = B.T

# Compute the product B_T * D
E = np.dot(B_T, D)

# Display the result
print('Result of B^T * D:')
print(E)
```

### c)

$$tr(B) $$
```{python}
# Compute the trace of matrix B
trace_B = np.trace(B)

# Display the result
print('Trace of B:')
print(trace_B)
```
