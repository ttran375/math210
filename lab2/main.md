### Example 1

Solve the following system:

$$ \begin{cases}
3x - 2y = 8 \\
x + 4y = -3 \end{cases} $$

We will solve this system using matrix methods.

Step 1: Write the augmented matrix for the system.

$$ \begin{bmatrix}
3 & -2 & | & 8 \\
1 & 4 & | & -3
\end{bmatrix} $$

Step 2: Perform row operations to get the matrix in row-echelon form.

1. Multiply the second row by 3 to make the coefficient of \( x \) in the second row match the coefficient of \( x \) in the first row:

$$ \begin{bmatrix}
3 & -2 & | & 8 \\
3 & 12 & | & -9
\end{bmatrix} $$

2. Subtract the first row from the second row to eliminate \( x \):

$$ \begin{bmatrix}
3 & -2 & | & 8 \\
0 & 14 & | & -17
\end{bmatrix} $$

Step 3: Solve for \( y \) from the second row.

$$ 14y = -17 $$
$$ y = -\frac{17}{14} $$

Step 4: Substitute \( y = -\frac{17}{14} \) back into the first row to find \( x \).

$$ 3x - 2\left(-\frac{17}{14}\right) = 8 $$
$$ 3x + \frac{34}{14} = 8 $$
$$ 3x + \frac{17}{7} = 8 $$
$$ 3x = 8 - \frac{17}{7} $$
$$ 3x = \frac{56}{7} - \frac{17}{7} $$
$$ 3x = \frac{39}{7} $$
$$ x = \frac{39}{21} $$
$$ x = \frac{13}{7} $$

So, the solution to the system is:
$$ x = \frac{13}{7}, \quad y = -\frac{17}{14} $$

### Example 2

Solve the system simultaneously:

$$ \begin{cases}
3x - y + z = b_1 \\
-x + 2y + 3z = b_2 \\
x - 4z = b_3
\end{cases} $$

We will solve this system for both cases (a) and (b).

#### Case (a)

$$ \begin{cases}
b_1 = 1 \\
b_2 = -1 \\
b_3 = 7
\end{cases} $$

The system becomes:

$$ \begin{cases}
3x - y + z = 1 \\
-x + 2y + 3z = -1 \\
x - 4z = 7
\end{cases} $$

To solve this system, we can use matrix methods or substitution/elimination. Here we use matrix methods.

Write the augmented matrix:

$$ \begin{bmatrix}
3 & -1 & 1 & | & 1 \\
-1 & 2 & 3 & | & -1 \\
1 & 0 & -4 & | & 7
\end{bmatrix} $$

Perform row operations to get the matrix in row-echelon form:

1. Swap Row 1 and Row 3 to place a 1 in the top left corner:

$$ \begin{bmatrix}
1 & 0 & -4 & | & 7 \\
-1 & 2 & 3 & | & -1 \\
3 & -1 & 1 & | & 1
\end{bmatrix} $$

2. Add Row 1 to Row 2 and multiply Row 1 by 3 and subtract Row 3:

$$ \begin{bmatrix}
1 & 0 & -4 & | & 7 \\
0 & 2 & -1 & | & 6 \\
0 & -1 & 13 & | & -20
\end{bmatrix} $$

3. Add Row 2 to Row 3:

$$ \begin{bmatrix}
1 & 0 & -4 & | & 7 \\
0 & 2 & -1 & | & 6 \\
0 & 0 & 12 & | & -14
\end{bmatrix} $$

Back-substitution to find \( z \):

$$ 12z = -14 $$
$$ z = -\frac{14}{12} $$
$$ z = -\frac{7}{6} $$

Substitute \( z = -\frac{7}{6} \) into Row 2 to find \( y \):

$$ 2y - (-\frac{7}{6}) = 6 $$
$$ 2y + \frac{7}{6} = 6 $$
$$ 2y = 6 - \frac{7}{6} $$
$$ 2y = \frac{36}{6} - \frac{7}{6} $$
$$ 2y = \frac{29}{6} $$
$$ y = \frac{29}{12} $$

Substitute \( y = \frac{29}{12} \) and \( z = -\frac{7}{6} \) into Row 1 to find \( x \):

$$ x - 4(-\frac{7}{6}) = 7 $$
$$ x + \frac{28}{6} = 7 $$
$$ x + \frac{14}{3} = 7 $$
$$ x = 7 - \frac{14}{3} $$
$$ x = \frac{21}{3} - \frac{14}{3} $$
$$ x = \frac{7}{3} $$

So, the solution for case (a) is:
$$ x = \frac{7}{3}, \quad y = \frac{29}{12}, \quad z = -\frac{7}{6} $$

#### Case (b)

$$ \begin{cases}
b_1 = -2 \\
b_2 = 3 \\
b_3 = 1
\end{cases} $$

The system becomes:

$$ \begin{cases}
3x - y + z = -2 \\
-x + 2y + 3z = 3 \\
x - 4z = 1
\end{cases} $$

We follow the same matrix method:

Write the augmented matrix:

$$ \begin{bmatrix}
3 & -1 & 1 & | & -2 \\
-1 & 2 & 3 & | & 3 \\
1 & 0 & -4 & | & 1
\end{bmatrix} $$

Perform row operations to get the matrix in row-echelon form:

1. Swap Row 1 and Row 3:

$$ \begin{bmatrix}
1 & 0 & -4 & | & 1 \\
-1 & 2 & 3 & | & 3 \\
3 & -1 & 1 & | & -2
\end{bmatrix} $$

2. Add Row 1 to Row 2 and multiply Row 1 by 3 and subtract Row 3:

$$ \begin{bmatrix}
1 & 0 & -4 & | & 1 \\
0 & 2 & -1 & | & 4 \\
0 & -1 & 13 & | & -5
\end{bmatrix} $$

3. Add Row 2 to Row 3:

$$ \begin{bmatrix}
1 & 0 & -4 & | & 1 \\
0 & 2 & -1 & | & 4 \\
0 & 0 & 12 & | & -1
\end{bmatrix} $$

Back-substitution to find \( z \):

$$ 12z = -1 $$
$$ z = -\frac{1}{12} $$

Substitute \( z = -\frac{1}{12} \) into Row 2 to find \( y \):

$$ 2y - (-\frac{1}{12}) = 4 $$
$$ 2y + \frac{1}{12} = 4 $$
$$ 2y = 4 - \frac{1}{12} $$
$$ 2y = \frac{48}{12} - \frac{1}{12} $$
$$ 2y = \frac{47}{12} $$
$$ y = \frac{47}{24} $$

Substitute \( y = \frac{47}{24} \) and \( z = -\frac{1}{12} \) into Row 1 to find \( x \):

$$ x - 4(-\frac{1}{12}) = 1 $$
$$ x + \frac{4}{12} = 1 $$
$$ x + \frac{1}{3} = 1 $$
$$ x = 1 - \frac{1}{3} $$
$$ x = \frac{3}{3} - \frac{1}{3} $$
$$ x = \frac{2}{3} $$

So, the solution for case (b) is:
$$ x = \frac{2}{3}, \quad y = \frac{47}{24}, \quad z = -\frac{1}{12} $$
