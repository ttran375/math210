# Confidence intervals

## Question 2

Average score obtained by 25 students in a test is 75. It is known that
the standard deviation of the population of scores is 8. Find the
confidence interval at 95% confidence level, assuming the scores are
normally distributed.

- $\bar{x} = 75$
- $\sigma = 8$
- $n = 25$
- $1-\alpha= 95\\%$

$$ \text{ME} = Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$
$$ \text{ME} = 1.96 \left( \frac{8}{\sqrt{25}} \right) $$

$$ \text{ME} = 3.136 $$

$$ \text{CI} = \bar{x} \pm Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$
$$ \text{CI} = 75 \pm 3.136 $$

$$ \text{CI} = (71.864, 78.136) $$

## Question 2 – modified

Average score obtained by 25 students in a test is 75. The standard
deviation for the sample of scores is 8. Find the confidence interval at
95% confidence level, assuming the scores are normally distributed.

- $\bar{x} = 75$
- $s = 8$
- $n = 25$
- $1-\alpha = 95%$

$$ \text{ME} = t_{\alpha/2} \left( \frac{s}{\sqrt{n}} \right) $$
$$ \text{ME} = 2.064 \left( \frac{8}{\sqrt{25}} \right) $$
$$ \text{ME} = 3.3024 $$

$$ \text{CI} = \bar{x} \pm t_{\alpha/2} \left( \frac{s}{\sqrt{n}} \right) $$
$$ \text{CI} = 75 \pm 3.3024 $$ $$ \text{CI} = (71.6976, 78.3024) $$

## Question 3

21 employees from a certain company travel to work an average of 14.3
miles. The standard deviation of their travel time was 2 miles. Find the
95% confidence interval of the true mean of the population, considering
the data is normally distributed.

To find the 95% confidence interval for the true mean of the
population’s travel distance, given that the data is normally
distributed and the standard deviation is for the sample, we will use
the t-distribution.

The formula for the confidence interval of the mean when the sample
standard deviation is known is:

$$ \text{CI} = \bar{x} \pm t_{\alpha/2} \left( \frac{s}{\sqrt{n}} \right) $$

Where:

- $\bar{x}$ is the sample mean
- $t_{\alpha/2}$ is the t-score corresponding to the desired confidence
  level and degrees of freedom
- $s$ is the sample standard deviation
- $n$ is the sample size

Given:

- $\bar{x} = 14.3$ miles
- $s = 2$ miles
- $n = 21$
- Confidence level = 95%

For a 95% confidence level and $n - 1 = 20$ degrees of freedom,
$t_{\alpha/2}$ is approximately 2.086 (from t-distribution tables or
using a t-distribution calculator).

Now, we can calculate the margin of error (ME):

$$ \text{ME} = t_{\alpha/2} \left( \frac{s}{\sqrt{n}} \right) $$
$$ \text{ME} = 2.086 \left( \frac{2}{\sqrt{21}} \right) $$
$$ \text{ME} = 2.086 \left( \frac{2}{4.5826} \right) $$
$$ \text{ME} = 2.086 \times 0.436 $$

$$ \text{ME} = 0.910 $$

Therefore, the confidence interval is:

$$ \text{CI} = 14.3 \pm 0.910 $$
$$ \text{CI} = (14.3 - 0.910, 14.3 + 0.910) $$
$$ \text{CI} = (13.39, 15.21) $$

So, the 95% confidence interval for the average travel distance is
$(13.39, 15.21)$ miles.

## Question 4

The average yearly income for 17 engineering graduates in 2008 was
\$56,718. The standard deviation for the population of incomes is known
to be \$650. Find the 90% confidence interval for the population mean,
considering the population is normally distributed.

To find the 90% confidence interval for the population mean, you can use
the formula for the confidence interval when the population standard
deviation is known. The formula is:

$$ \bar{x} \pm Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$

Where:

- $\bar{x}$ is the sample mean.
- $Z_{\alpha/2}$ is the critical value from the standard normal
  distribution for the desired confidence level.
- $\sigma$ is the population standard deviation.
- $n$ is the sample size.

Given:

- Sample mean ($\bar{x}$) = \$56,718
- Population standard deviation ($\sigma$) = \$650
- Sample size ($n$) = 17
- Confidence level = 90%

First, find the critical value $Z_{\alpha/2}$ for a 90% confidence
level. For a 90% confidence level, $\alpha = 0.10$, so
$\alpha/2 = 0.05$. The critical value $Z_{\alpha/2}$ corresponding to
0.05 in the standard normal distribution is approximately 1.645.

Now, calculate the margin of error:

$$ \text{Margin of error} = Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$

$$ \text{Margin of error} = 1.645 \left( \frac{650}{\sqrt{17}} \right) $$

$$ \text{Margin of error} = 1.645 \left( \frac{650}{4.123} \right) $$

$$ \text{Margin of error} = 1.645 \left( 157.59 \right) $$

$$ \text{Margin of error} \approx 259.98 $$

Now, calculate the confidence interval:

$$ \text{Lower limit} = \bar{x} - \text{Margin of error} $$

$$ \text{Lower limit} = 56,718 - 259.98 $$

$$ \text{Lower limit} \approx 56,458 $$

$$ \text{Upper limit} = \bar{x} + \text{Margin of error} $$

$$ \text{Upper limit} = 56,718 + 259.98 $$

$$ \text{Upper limit} \approx 56,978 $$

Therefore, the 90% confidence interval for the population mean is
approximately:

$$ (56,458, 56,978) $$

## Question 6

1.  An automotive engineer wants to estimate the cost of repairing a car
    that experiences a head-on collision. He crashes 36 cars, and the
    average repair is \$11,000. The standard deviation of the population
    of repair costs is known to be \$2,500. A)Provide a 90% confidence
    interval for the true mean cost of repairs. B)Provide a 98%
    confidence interval for the true mean cost of repair.

To calculate the confidence intervals, we use the formula for the
confidence interval when the population standard deviation is known:

$$ \bar{x} \pm Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$

Where:

- $\bar{x}$ is the sample mean.
- $Z_{\alpha/2}$ is the critical value from the standard normal
  distribution for the desired confidence level.
- $\sigma$ is the population standard deviation.
- $n$ is the sample size.

Given:

- Sample mean ($\bar{x}$) = \$11,000
- Population standard deviation ($\sigma$) = \$2,500
- Sample size ($n$) = 36

### Part A: 90% Confidence Interval

For a 90% confidence level, $\alpha = 0.10$, so $\alpha/2 = 0.05$. The
critical value $Z_{\alpha/2}$ corresponding to 0.05 in the standard
normal distribution is approximately 1.645.

Calculate the margin of error:

$$ \text{Margin of error} = Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$

$$ \text{Margin of error} = 1.645 \left( \frac{2,500}{\sqrt{36}} \right) $$

$$ \text{Margin of error} = 1.645 \left( \frac{2,500}{6} \right) $$

$$ \text{Margin of error} = 1.645 \left( 416.67 \right) $$

$$ \text{Margin of error} \approx 685.42 $$

Now, calculate the confidence interval:

$$ \text{Lower limit} = \bar{x} - \text{Margin of error} $$

$$ \text{Lower limit} = 11,000 - 685.42 $$

$$ \text{Lower limit} \approx 10,314.58 $$

$$ \text{Upper limit} = \bar{x} + \text{Margin of error} $$

$$ \text{Upper limit} = 11,000 + 685.42 $$

$$ \text{Upper limit} \approx 11,685.42 $$

Therefore, the 90% confidence interval for the true mean cost of repairs
is approximately:

$$ (10,314.58, 11,685.42) $$

### Part B: 98% Confidence Interval

For a 98% confidence level, $\alpha = 0.02$, so $\alpha/2 = 0.01$. The
critical value $Z_{\alpha/2}$ corresponding to 0.01 in the standard
normal distribution is approximately 2.33.

Calculate the margin of error:

$$ \text{Margin of error} = Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$

$$ \text{Margin of error} = 2.33 \left( \frac{2,500}{\sqrt{36}} \right) $$

$$ \text{Margin of error} = 2.33 \left( \frac{2,500}{6} \right) $$

$$ \text{Margin of error} = 2.33 \left( 416.67 \right) $$

$$ \text{Margin of error} \approx 970.84 $$

Now, calculate the confidence interval:

$$ \text{Lower limit} = \bar{x} - \text{Margin of error} $$

$$ \text{Lower limit} = 11,000 - 970.84 $$

$$ \text{Lower limit} \approx 10,029.16 $$

$$ \text{Upper limit} = \bar{x} + \text{Margin of error} $$

$$ \text{Upper limit} = 11,000 + 970.84 $$

$$ \text{Upper limit} \approx 11,970.84 $$

Therefore, the 98% confidence interval for the true mean cost of repairs
is approximately:

$$ (10,029.16, 11,970.84) $$
