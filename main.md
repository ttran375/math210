# Hypotheses Testing

## Steps for Hypotheses Testing

In a court of law, there are 2 possible errors: 1. Finding the defendant
guilty when he is innocent. 2. Finding the defendant innocent when he is
guilty.

In hypothesis testing, these 2 types of errors translate as follows:

1.  **Type I error**: The mistake of rejecting the null hypothesis when
    it is true. For instance, in the above example, rejecting the
    hypothesis of mean salary being \$45,000 when, in fact, it is true.
2.  **Type II error**: The mistake of failing to reject the null
    hypothesis when it is false. For instance, in the above example,
    failing to reject the hypothesis of mean salary being \$45,000 when,
    in reality, it is not true.

#### Type I and II Errors:

The size of $\alpha$, the rejection region, affects the risk of making
different types of incorrect decisions.

- **Type I Error**:
  - Rejecting a true null hypothesis when it should NOT be rejected.
  - Considered a serious type of error.
  - The probability of Type I Error is $\alpha$.
  - It is also called the level of significance of the test.
- **Type II Error**:
  - Failing to reject a false null hypothesis that should have been
    rejected.
  - The probability of Type II Error is $\beta$.

## Steps for Hypothesis Testing

### Identify the Null Hypothesis $H_0$ and the Alternate Hypothesis $H_1$

1.  Identify the null hypothesis $H_0$ and the alternate hypothesis
    $H_1$. As a rule, the null hypothesis will contain an equal sign,
    and the alternate hypothesis will contradict the null hypothesis
    (thus containing one of the inequality signs).

### Errors in Hypothesis Testing

In a court of law, there are 2 possible errors: - (a) Finding the
defendant guilty when he is innocent. - (b) Finding the defendant
innocent when he is guilty.

In hypothesis testing, these 2 types of errors translate as follows: -
**Type I Error**: The mistake of rejecting the null hypothesis when it
is true. For instance, in the above example, rejecting the hypothesis of
mean salary being \$45,000 when, in fact, it is true. - **Type II
Error**: The mistake of failing to reject the null hypothesis when it is
false. For instance, in the above example, failing to reject the
hypothesis of mean salary being \$45,000 when, in reality, it is not
true.

### Type I and II Errors

- **Type I Error**: Rejecting a true null hypothesis when it should NOT
  be rejected. This is considered a serious type of error. The
  probability of Type I Error is $\alpha$. It is also called the level
  of significance of the test.
- **Type II Error**: Failing to reject a false null hypothesis that
  should have been rejected. The probability of Type II Error is
  $\beta$.

### Steps - Continued

2.  Choose the level of significance $\alpha$. The value should be
    small, usually less than 10%. Consider the consequences of both
    types of errors. Determine the critical region by calculating the
    critical value(s). There are 3 possibilities for the acceptance
    region:
    - If the test statistic is situated inside the acceptance region, we
      fail to reject the null hypothesis.
    - If the test statistic is situated in the critical region, we
      reject the null hypothesis.
3.  Choose the test statistic and calculate its value. For known
    $\sigma$, calculate the z-score for the test statistic; for unknown
    $\sigma$, calculate the t-score.

### Test of Hypothesis for the Mean

- **When $\sigma$ is known**: The test statistic is
  $z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$.
- **When $\sigma$ is unknown**: The test statistic is
  $t = \frac{\bar{X} - \mu}{s / \sqrt{n}}$.

### Steps - Continued

4.  Compare the observed value of the statistic to the critical value
    obtained for the chosen level of significance and make a decision.
    Make a decision to reject/fail to reject the null hypothesis.
    Compare the z-score of the test statistic to the values of z that
    constructed the critical region. If the z-score of the test
    statistic falls in the critical region, we reject the null
    hypothesis. If it falls inside the acceptance zone, we fail to
    reject the null hypothesis.

5.  State a conclusion.

## Example

A sports biologist claims that female distance runners tend to be taller
on average than women in general, who have an average height of 64
inches. To study this, she obtained a sample of 55 female distance
runners and recorded their heights, obtaining a mean of $\bar{x}$. It is
known that the general population of female distance runners has a
standard deviation $\sigma$. Using these results, test the claim at the
5% level of significance ($\alpha = 0.05$).

### Step 1: Formulate the Hypotheses

The claim is that female distance runners are taller on average than
women in general. Therefore, our hypotheses will be:

- $H_0: \mu = 64$ inches (null hypothesis: the mean height of female
  distance runners is 64 inches)
- $H_a: \mu > 64$ inches (alternate hypothesis: the mean height of
  female distance runners is greater than 64 inches)

### Step 2: Set the Significance Level

The significance level (α) is given as 0.05.

### Step 3: Determine the Test Statistic

Since we know the standard deviation of the general population of female
distance runners (σ), we will use a z-test to determine the test
statistic. The formula for the z-test is:

$$ z = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}} $$

where: - $\bar{x}$ is the sample mean height of female distance
runners - $\mu$ is the population mean height of women in general (64
inches) - $\sigma$ is the population standard deviation of female
distance runners - $n$ is the sample size (55)

### Step 4: Calculate the Test Statistic

To proceed, we need the sample mean height ($\bar{x}$) and the
population standard deviation ($\sigma$).

For illustration, let’s assume $\bar{x} = 65$ inches and $\sigma = 3$
inches (these values need to be given or calculated from actual data):

$$ z = \frac{65 - 64}{\frac{3}{\sqrt{55}}} $$
$$ z = \frac{1}{\frac{3}{7.416}} $$

$$ z \approx \frac{1}{0.404} $$

$$ z \approx 2.48 $$

### Step 5: Determine the Critical Value and Make a Decision

For a one-tailed test at the 5% level of significance, we look up the
critical value in the z-table:

$$ z_{0.05} = 1.645 $$

Since our calculated $z$-value (2.48) is greater than the critical value
(1.645), we reject the null hypothesis.

### Conclusion

We have sufficient evidence at the 0.05 significance level to conclude
that female distance runners are, on average, taller than women in
general.

### Summary of Steps

1.  **Formulate the Hypotheses**:

    - $H_0: \mu = 64$ inches
    - $H_a: \mu > 64$ inches

2.  **Set the Significance Level**: $\alpha = 0.05$

3.  **Determine the Test Statistic**:
    $$ z = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}} $$

4.  **Calculate the Test Statistic**: Assuming $\bar{x} = 65$ inches and
    $\sigma = 3$ inches, $$ z \approx 2.48 $$

5.  **Determine the Critical Value and Make a Decision**:

    - Critical value $z_{0.05} = 1.645$
    - Since $z \approx 2.48$ \> 1.645, reject $H_0$

**Conclusion**: At the 5% level of significance, we found enough
evidence to support the claim that that female distance runners tend to
be taller on the average than women in general.
