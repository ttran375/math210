# Review Statistics

## Question 1

Consider the following stem and leaf plot. Find:

a) The 35th percentile

b) The median

| Stem | Leaf |
|------|------|
| 1    | 4 4 6 |
| 2    | 3 8 |
| 3    | 2    |
| 4    | 0 1 |

### a) The 35th percentile

Sort: 14, 14, 16, 23, 28, 32, 40, 41

$$ \text{Loc. } P_{35} = \left(\frac{K}{100}\right) \times u = \left(\frac{35}{100}\right) \times 8 = 2.8 \rightarrow 3 $$
$$ P_{35} = 16 \text{ days} $$

### b) The 35th percentile

$$ \text{Loc. } \tilde{x} = \frac{n+1}{2} = \frac{8+1}{2} = 4.5 $$
$$ \tilde{x} = \frac{23 + 28}{2} = 25.5 \text{ days} $$

## Question 2

The following dot plot represents number of books college students read over a semester.

![](dot-plot.png)

Find the following:
a) The mean

b) The standard deviation

c) The interquartile range

### a) The mean

Data: 2,3,3,5,5,7,7,7,10,10,11

$$ \bar{x} = \frac{\sum{x}}{n} = \frac{2+3+3+5+5+7+7+7+10+10+11}{11} \approx 6.4 $$

### b) The standard deviation

$$
\begin{align}
s &= \sqrt{\dfrac{\sum\limits_{i=1}^{n} (x_i - \bar{x})^2}{n-1}} \\
&= \sqrt{\dfrac{(2 - 6.4)^2 + (3 - 6.4)^2 + (3 - 6.4)^2 + (5 - 6.4)^2 + (5 - 6.4)^2 + (7 - 6.4)^2 + (7 - 6.4)^2 + (7 - 6.4)^2 + (10 - 6.4)^2 + (10 - 6.4)^2 + (11 - 6.4)^2}{11-1}} \\
&\approx 3.1
\end{align}
$$

### c) The interquartile range

$$
\frac{25}{100} \times 11 = 2.75 \rightarrow \text{Loc} P_{25} = 3 \rightarrow P_{25} = 3 \rightarrow Q_1 = 3
$$

$$
\frac{75}{100} \times 14 = 8.25 \rightarrow \text{Loc} P_{75} = 9 \rightarrow P_{75} = 10 \rightarrow Q_3 = 10
$$

$$ IQR = Q_3 - Q_1 = 10−3=7$$

## Question 3

A survey found that 20% of people believe that they have seen a UFO. Choose a sample of 10 people at random. Find the probability of the following. Round intermediate calculations and final answers to at least three decimal places.

(a) At least 3 people believe that they have seen a UFO
(b) Exactly 2 people think they have seen an UFO
(c) At most 2 people believe that they have seen a UFO

### (a) At least 3 people believe that they have seen a UFO

$$
\begin{align}
P(x \geq 3) &= 1 - [P(0) + P(1) + P(2)] \\
&= 1 - [C_{10}^0 \times 0.20^0 \times 0.80^{10} + C_{10}^1 \times 0.20^1 \times 0.80^9 + C_{10}^2 \times 0.20^2 \times 0.80^8] \\
&\approx 0.3222
\end{align}
$$

### (b) Exactly 2 people think they have seen an UFO

$$ P(x = 2) = C_{10}^2 \times 0.20^2 \times 0.80^8 \approx 0.3020 $$

### (c) At most 2 people believe that they have seen a UFO

$$
\begin{align}
P(x \leq 2) &= P(0) + P(1) + P(2) \\
&= C_{10}^0 \times 0.20^0 \times 0.80^{10} + C_{10}^1 \times 0.20^1 \times 0.80^9 + C_{10}^2 \times 0.20^2 \times 0.80^8 \\
&\approx 0.6778
\end{align}
$$

## Question 4

a) In the standard normal distribution, find the z value that
corresponds to the 78th percentile. Use Cumulative Normal
Distribution Table and enter the answer to 2 decimal places.

b) In order for a student to be accepted to a postgraduate
program, she needs to achieve an entrance exam mark that is
at least at the 40% level of all marks. If the mean of marks for
the entrance exam is known to be 82, with a standard
deviation of 8, what is the minimum mark that she needs to
acquire?
