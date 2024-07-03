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

```scilab
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

Name the matrix using a letter. Use brackets. Use a semicolon after each row.

### Example

```scilab
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

```scilab
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

```scilab
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

Clean command will restore the matrix to the identity matrix (see below).

```scilab
--> clean(inv(A) * A)
ans =
1. 0. 0.
0. 1. 0.
0. 0. 1.
```

### Transpose of a Matrix

```scilab
--> A'
ans =
3. 0. -1.
4. 1. 2.
5. 2. 7.
```

### Trace of a Matrix

```scilab
--> trace(A)
ans =
11.
```

### Solving Systems of Linear Equations by Applying the Reduced Row Echelon Command to the Augmented Matrix Associated with the System

```scilab
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

The solution of the system can be found in the last column of the matrix above.

## Practice

1. Given the following matrices, perform the operation:

   $A = \begin{bmatrix} 1 & 2 & 0 \\ 8 & 1 & 2 \\ 0 & -2 & -43 \end{bmatrix}$, $B = \begin{bmatrix} 0 & 1 & 2 \\ -3 & 6 & 1 \\ 7 & -23 & 0 \end{bmatrix}$

   a) $A'$

   b) $\text{trace}(B)$

   c) $A \times B$

   d) $B \times A$

   e) $3A - B'$

   f) $\text{inv}(B)$

   g) $\text{rref}(A)$

   e) $A^3$

   f) $2B - 3I$
