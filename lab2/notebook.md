### Example 1

Solve the following system:

$$
\begin{cases}
3x - 2y = 8 \\
x + 4y = -3
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
x1, y1 = solution1
print(f"Example 1 Solution: x = {x1}, y = {y1}")
```

    ## Example 1 Solution: x = 1.857142857142857, y = -1.2142857142857142

### Example 2

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

``` python
# Constants vector for a)
B2a = np.array([1, -1, 7])

# Solving the system
solution2a = np.linalg.solve(A2, B2a)
x2a, y2a, z2a = solution2a
print(f"Example 2a Solution: x = {x2a}, y = {y2a}, z = {z2a}")
```

    ## Example 2a Solution: x = 1.5600000000000003, y = 2.3200000000000003, z = -1.36

2)  

$$ \begin{cases}
b_1 = -2 \\
b_2 = 3 \\
b_3 = 1
\end{cases} $$

``` python
# Constants vector for b)
B2b = np.array([-2, 3, 1])

# Solving the system
solution2b = np.linalg.solve(A2, B2b)
x2b, y2b, z2b = solution2b
print(f"Example 2b Solution: x = {x2b}, y = {y2b}, z = {z2b}")
```

    ## Example 2b Solution: x = 0.03999999999999996, y = 1.88, z = -0.23999999999999994