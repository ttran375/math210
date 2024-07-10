# Math 210. Lab #2

## Solving linear systems with Scilab. Practice

Perform the indicated operations using Scilab.

Example 1.

Solve the following system:

3*x* − 2*y* = 8

*x* + 4*y*=  − 3

Solution:

A=\[3 -2 8;1 4 -3\]

A =

3\. - 2. 8.

1\. 4. - 3.

--\>rref(A)

ans =

1\. 0. 1.8571429

0\. 1. - 1.2142857

Example 2

Solve the system simultaneously:

3*x* − *y* + *z* = *b*<sub>1</sub>

−*x* + 2*y* + 3*z*= *b*<sub>2</sub>

*x*    − 4*z*= *b*<sub>3</sub>

a\)
*b*<sub>1</sub>= 1            *b*<sub>2</sub>=  − 1             *b*<sub>3</sub>=  7        

b\)
*b*<sub>1</sub>=  − 2            *b*<sub>2</sub>= 3             *b*<sub>3</sub>=  1        

Solution:

B=\[3 -1 1 1 -2;-1 2 3 -1 3;1 0 -4 7 1\]

B =

3\. - 1. 1. 1. - 2.

\- 1. 2. 3. - 1. 3.

1\. 0. - 4. 7. 1.

--\>rref(B)

ans =

1\. 0. 0. 1.56 0.04

0\. 1. 0. 2.32 1.88

0\. 0. 1. - 1.36 - 0.24

## Practic

1.  Solve the following systems of equations using the method from
    example 1.

<!-- -->

1.  3*x*<sub>1</sub> − 5*x*<sub>2</sub> = 7

*x*<sub>1</sub> + 9*x*<sub>2</sub> = 11

1.  3*x*<sub>1</sub> + 2*x*<sub>2</sub> − *x*<sub>3</sub> = 8

2*x*<sub>1</sub> − 5*x*<sub>2</sub> + *x*<sub>3</sub> = 3

6*x*<sub>1</sub> +*x*<sub>3</sub> = 2

1.  Solve the systems simultaneously by using the method from example 2.

3*x*<sub>1</sub> + 2*x*<sub>2</sub> − *x*<sub>3</sub> = *b*<sub>1</sub>

2*x*<sub>1</sub> − 5*x*<sub>2</sub> + *x*<sub>3</sub> = *b*<sub>2</sub>

6*x*<sub>1</sub> +*x*<sub>3</sub> = *b*<sub>3</sub>

1.  *b*<sub>1</sub> = 2, *b*<sub>2</sub> = 6, *b*<sub>3</sub> = 8

2.  *b*<sub>1</sub> = −2, *b*<sub>2</sub> = −6, *b*<sub>3</sub> = −8
