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

### (b) $C^T$

### (c) $g(B)$ where $g(x) = 3 - 2x^2$

### (d) $B + 3E^T$

## 4. Use SCILAB to solve the following system of equations and attach SCILAB output.

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

### b)

$$a_1 = 5, \quad a_2 = 1, \quad a_3 = -2 $$

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

### a)

### b)

### c)
