> **Lab 2: SYSTEMS OF EQUATIONS** *Example 1*. Consider the system of
> linear equations:\
> 2x1 + 2x2 + 3x3 =0\
> 3x1 + x2 + 4x3 =21\
> --x1 -- 3x2 + 7x3 =15\
> We can represent this system using matrices: **Ax** = **b**
>
> Where
>
> To solve this equation, we can left multiply both sides by A-1
> **A**-1**Ax** = **A**-1**b** **Ix** = **A**-1**b**\
> **x** = **A**-1**b**
>
> Using Scilab, we obtain a solution by multiplying the inverse of A
> with b.
>
> A= \[2 2 3; 3 1 4; -1 -3 7\];\
> b= \[0; 21; 15\];\
> inv(A)\*b\
> ans =\
> 11.333333\
> - 10.333333\
> - 0.6666667
>
> Solving Two Linear Systems at Once\
> *Example 2*. Consider the systems:
>
> a)\
> 2x1 + 2x2 + 3x3 =0
>
> 3x1 + x2 + 4x3 =21
>
> --x1 -- 3x2 + 7x3 =15
>
> b)\
> 2x1 + 2x2 + 3x3 = -3
>
> 3x1 + x2 + 4x3 = 3
>
> --x1 -- 3x2 + 7x3 = -6
>
> Since both systems have the same coefficient matrix, we represent both
> systems with the augmented matrix:
>
> We can do this in Scilab by:\
> b1=\[-3; 3; -6\];\
> A(:,4) = b; A(:,5)=b1\
> rref(A)\
> ans =
>
> 1\. 0. 0. 11.333333 4.3333333\
> 0. 1. 0. - 10.333333 - 3.3333333\
> 0. 0. 1. - 0.6666667 - 1.6666667
>
> Exercises:
>
> Solve the systems of questions 1 -- 3 using the method of
> Example 1. 1) x1 + 2x2 = 2\
> 5x1 + 6x2 = 9
>
> 2\) 5x1 + 3x2 + 2x3 =4\
> 3x1 +3x2 + 2x3 =2\
> x2 + x3 =5
>
> 3\) Solve the systems in all parts simultaneously using the method of
> Example 2 -x1 + 4x2 + x3 = b1\
> x1 + 9x2 -- 2x3 = b2\
> 6x1 + 4x2 -- 8x3 = b3
>
> \(a\) b1 = 0, b2 = 1, b3 = 0
>
> \(b\) b1 = - 3, b2 = 4, b3 = - 5
