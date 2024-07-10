# Math 210: Lab #2

## Solving Linear Systems with Scilab: Practice

Perform the indicated operations using Scilab.

### Example 1

Solve the following system:

$$ 3x - 2y = 8 $$
$$ x + 4y = -3 $$

**Solution:**

```scilab
A = [3 -2 8; 1 4 -3]

A =
   3.  -2.  8.
   1.   4. -3.
   
-->rref(A)

ans =
   1.  0.  1.8571429
   0.  1. -1.2142857
```

### Example 2

Solve the system simultaneously:

$$ 3x - y + z = b_1 $$
$$ -x + 2y + 3z = b_2 $$
$$ x - 4z = b_3 $$

#### Case (a)

$$ b_1 = 1 $$
$$ b_2 = -1 $$
$$ b_3 = 7 $$

#### Case (b)

$$ b_1 = -2 $$
$$ b_2 = 3 $$
$$ b_3 = 1 $$

**Solution:**

```scilab
B = [3 -1 1 1 -2; -1 2 3 -1 3; 1 0 -4 7 1]

B =
   3.  -1.  1.  1.  -2.
  -1.   2.  3. -1.   3.
   1.   0. -4.  7.   1.

-->rref(B)

ans =
   1.  0.  0.  1.56  0.04
   0.  1.  0.  2.32  1.88
   0.  0.  1. -1.36 -0.24
```

## Practice

1. Solve the following systems of equations using the method from Example 1.

   1. $$
      3x_1 - 5x_2 = 7 \\
      x_1 + 9x_2 = 11
      $$

   2. $$
      3x_1 + 2x_2 - x_3 = 8 \\
      2x_1 - 5x_2 + x_3 = 3 \\
      6x_1 + x_3 = 2
      $$

2. Solve the systems simultaneously using the method from Example 2.

   $$
   3x_1 + 2x_2 - x_3 = b_1 \\
   2x_1 - 5x_2 + x_3 = b_2 \\
   6x_1 + x_3 = b_3
   $$

   1. For \( b_1 = 2 \), \( b_2 = 6 \), \( b_3 = 8 \)
   2. For \( b_1 = -2 \), \( b_2 = -6 \), \( b_3 = -8 \)
