# Review for Quiz – Statistics Math 210

## Question 1

Given the following frequency histogram, find:

<img src="main/media/image2.png" style="width:6.25in;height:4.6875in" />

- A\) The sample size that was analyzed
- B\) What is the cumulative frequency of class 2?
- C\) What is the midpoint of class 3?
- D\) What is the class width?

Let’s analyze the histogram to answer the given questions.

### A) The sample size that was analyzed

- The sample size of Class 1: 4
- The sample size of Class 2: 11
- The sample size of Class 3: 2
- The sample size of Class 4: 3
- The sample size of Class 5: 1

$$ \text{The sample size} = 4 + 11 + 2 + 3 + 1 = 21$$

### B) What is the cumulative frequency of class 2?

- The sample size of Class 1: 4
- The sample size of Class 2: 11

$$ \text{Cumulative frequency of class 2} = 4 + 11 = 15 $$

### C) What is the midpoint of class 3?

- Lower boundary of class 3: 45.5
- Upper boundary of class 3: 58.5

$$ \text{Midpoint of class 3} = \frac{45.5 + 58.5}{2} = 52 $$

### D) What is the class width?

- Class boundaries of Class 1: 19.5 to 32.5

$$ \text{Class width} = 32.5 - 19.5 = 13 $$

## Question 2

1.  It is estimated that 36% of the students are bored in their
    Statistics class. If a random sample of 15 students from this
    population is examined, find the probability that:

- a\) 3 students will say they are bored in class.
- b\) Fewer than 2 will say they are bored in class.
- c\) What is the expected value of students bored in their Statistics
  class?
- d\) What is the standard deviation for the number of students bored in
  their Statistics class?
- e\) At least 3 students will say they are bored in class.

$$ P(X = x) = \binom{n}{x} p^x (1-p)^{n-x} $$

- $n = 15$
- $p = 0.36$

### a) 3 students will say they are bored in class

$$ P(X = 3) = \binom{15}{3} \times 0.36^3 \times (1-0.36)^{15-3} \approx 0.10 $$

### b) Fewer than 2 will say they are bored in class

$$
\begin{align}
P(X < 2) &= P(X = 0) + P(X = 1) \\
&= \binom{15}{0} \times 0.36^0 \times (1-0.36)^{15-0} + \binom{15}{1} \times 0.36^1 \times (1-0.36)^{15-1} \\
&\approx 0.01
\end{align}
$$

### c) What is the expected value of students bored in their Statistics class?

$$ \mu = E[X] = np = 15 \times 0.36 = 5.40$$

### d) What is the standard deviation for the number of students bored in their Statistics class?

$$ \sigma = \sqrt{V[X]} = \sqrt{np(1-p)} = \sqrt{15 \times 0.36 \times(1-0.36)} = 1.86$$

### e) At least 3 students will say they are bored in class

$$
\begin{align}
P(X \geq 3) &= 1 - P(X < 3)\\
&= 1 - [P(X = 0) + P(X = 1) + P(X = 2)]\\
&= 1 - \left[\binom{15}{0} \times 0.36^0 \times (1-0.36)^{15-0} + \binom{15}{1} \times 0.36^1 \times (1-0.36)^{15-1} + \binom{15}{2} \times 0.36^2 \times (1-0.36)^{15-2} \right] \\
&\approx 0.95
\end{align}
$$

## Question 3

2.  At a city high school, past records indicate that the literacy test
    scores for students are normally distributed with a mean of 67% and
    a standard deviation of 12%. If one student is randomly selected,
    what is the probability that their score will be more than 70%?

### If one student is randomly selected, what is the probability that their score will be more than 70%

- $\mu = 67\\%$
- $\sigma = 12\\%%$

$$ z = \frac{X - \mu}{\sigma} = \frac{70\\% - 67\\%}{12\\%} = 0.25 $$

$$ P(Z > 0.25) = 1 - P(Z \leq 0.25) = 1 - 0.5987 = 0.4013 $$

## Question 4

For the following sample data below representing the amount of time (in
hours) groups of students spent in completing a Statistics project,
find: 5, 7, 12, 8, 8, 12

- a\) The mean;
- b\) The median;
- c\) The midrange;
- d\) The standard deviation;
- e\) The 58th percentile;

### a) The mean

$$
\bar{x} = \frac{5 + 7 + 12 + 8 + 8 + 12}{6} \approx 8.67
$$

### b) The median

Sort: 5, 7, 8, 8, 12, 12

$$
\text{Median} = \frac{8 + 8}{2} = 8
$$

### c) The midrange

Sort: 5, 7, 8, 8, 12, 12

$$
\text{Midrange} = \frac{5 + 12}{2} = \frac{17}{2} = 8.5
$$

### d) The standard deviation

$$
\begin{align}
s &= \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \mu)^2} \\
&= \sqrt{\frac{1}{6-1} \times [(5 - 8.67)^2 + (7 - 8.67)^2 + (12 - 8.67)^2 + (8 - 8.67)^2 + (8 - 8.67)^2 + (12 - 8.67)^2]} \\
&= 2.80
\end{align}
$$

### e) The 58th percentile

Sort: 5, 7, 8, 8, 12, 12

$$
\frac{58}{100} \times 6 = 3.48 \rightarrow \text{Loc} P_{58} = 4 \rightarrow P_{58} = 8
$$

## Question 5

For the data in the stem and leaf graph below, find:

- A\) First quartile;
- B\) Third quartile;
- C\) The interquartile range;

Key: 2\|3 means 23 lbs.
<img src="main/media/image1.png" style="width:2.91667in;height:4.71875in" />

- Stem 1: 15, 17, 18
- Stem 2: 23, 23, 24, 25, 26
- Stem 3: 35, 36, 37
- Stem 4: 40, 42
- Stem 5: 56
- Stem 6: 63

Sort: 15, 17, 18, 23, 23, 24, 25, 26, 35, 36, 37, 40, 42, 56, 63

### A) First quartile

The first quartile ($Q_1$) is the median of the first half of the data,
the 4th value of the first 7 value: 23

### B) Third quartile

The third quartile ($Q_3$) is the median of the last half of the data,
the 4th value of the last 7 value: 40

### C) The interquartile range

The interquartile range (IQR) is the difference between the third
quartile and the first quartile.

$$ \text{IQR} = Q_3 - Q_1 = 40 - 23 = 17 $$

## Question 6

7.  The height of trees in a nursery is normally distributed with a mean
    of 45 cm and a standard deviation of 15 cm. Find:

- a\) The probability that a tree will have a height above 40 cm
- b\) The probability that a tree will have a height below 40 cm
- c\) The height that separates the top 10% of the heights from the rest
- d\) The height that separates the bottom 15% from the rest
- e\) The 87<sup>th</sup> percentile

### a) The probability that a tree will have a height above 40 cm

- $\mu$: 45 cm
- $\sigma$: 15 cm

$$ z = \frac{X - \mu}{\sigma} = \frac{40 - 45}{15} \approx-0.333 $$

$$ P(X > 40) = P(Z > -0.333) = 1 - P(Z < -0.333) \approx 1 - 0.3694 \approx 0.6306 $$

### b) The probability that a tree will have a height below 40 cm

$$ P(X < 40) = P(Z < -0.333) = 0.3694 $$

### c) The height that separates the top 10% of the heights from the rest

$$  X = \mu + Z_{0.90}\sigma \approx 45 + 1.2816 \times 15  = 64.224 $$

### d) The height that separates the bottom 15% from the rest

$$  X = \mu + Z_{0.15}\sigma \approx 45 + (-1.036) \times 15 = 29.46 $$

### e) The 87<sup>th</sup> percentile

$$ X = \mu + Z_{0.87}\sigma \approx 45 + 1.126 \times 15= 61.89 $$

## Question 7

8.  For the following bivariate data, find the regression line:
    $y = b_0 + b_1x$

| **x** | **y** |
|-------|-------|
| 21    | 12    |
| 34    | 11    |
| 35    | 9     |
| 46    | 9     |
| 47    | 6     |
| 73    | 4     |

- a\) ∑x
- b\) ∑y
- c\) ∑x<sup>2</sup>
- d\) ∑y<sup>2</sup>
- e\) ∑xy
- f\) $b_1$ (round to 2 decimal places)
- g\) $b_0$ (write your answer to one decimal place)
- h\) Coefficient of correlation

### a) ∑x

### b) ∑y

### c) ∑x<sup>2</sup>

### d) ∑y<sup>2</sup>

### e) ∑xy

$$
\begin{array}{|c|c|c|c|c|}
\hline
X & Y & XY & X^2 & Y^2 \\
\hline
21 & 12 & 252 & 441 & 144 \\
34 & 11 & 374 & 1156 & 121 \\
35 & 9 & 315 & 1225 & 81 \\
46 & 9 & 414 & 2116 & 81 \\
47 & 6 & 282 & 2209 & 36 \\
73 & 4 & 292 & 5329 & 16 \\
\hline
256 & 51 & 1929 & 12476 & 479 \\
\hline
\end{array}
$$

### f) $b_1$ (round to 2 decimal places)

$$
\begin{align}
b_1 &= \frac{(\sum Y)(\sum X^2) - (\sum X)(\sum XY)}{n(\sum X^2) - (\sum X)^2} = \frac{(51)(12476) - (256)(1929)}{6(12476) - (256)^2} = \frac{4726}{1173} \approx 15.28
\end{align}
$$

### g) $b_0$ (write your answer to one decimal place)

$$
\begin{align}
b_0 &= \frac{n(\sum XY) - (\sum X)(\sum Y)}{n(\sum X^2) - (\sum X)^2} = \frac{6(1929) - (256)(51)}{6(12476) - (256)^2} = \frac{2703}{1173} \approx -0.16 \\
\end{align}
$$

### h) Coefficient of correlation

$$
\begin{align}
r &= \frac{n \sum XY - \sum X \sum Y}{\sqrt{[n \sum X^2 - (\sum X)^2][n \sum Y^2 - (\sum Y)^2]}} \\
&= \frac{6 \times 1929 - 256 \times 51}{\sqrt{[6 \times 12476 - 256^2][6 \times 479 - 51^2]}} \\
&= -0.93
\end{align}
$$
