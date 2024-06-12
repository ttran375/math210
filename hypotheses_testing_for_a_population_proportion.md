# Hypotheses testing for a population proportion

## Example

In a study of air-bags effectiveness, it was found that in 821 crashes of
midsize cars equipped with air bags, 46 of the crashes resulted in
hospitalization of the drivers. Use a 0.01 significance level to test the
claim that the air bag hospitalization rate is lower than 7.8% rate for
crashes of midsize cars equipped with automatic safety belts but no air
bags.

- $n = 821$
- $x = 46$
- $\alpha = 0.01$
- $p = 0.078$


### Step 1

- $H_0: p = 0.078$
- $H_1: p < 0.078$

### Step 2

$Z_{0.01} = -2.33$

### Step 3

$$ \hat{p} = \frac{46}{821} \approx 0.056 $$

$$ \text{SE} = \sqrt{\frac{p (1 - p)}{n}} = \sqrt{\frac{0.078 \times (1 - 0.078)}{821}} \approx 0.0092 $$

$$ Z = \frac{\hat{p} - p}{\text{SE}} = \frac{0.056 - 0.078}{0.0092} \approx -2.35 $$

### Step 4

Since the P-value (0.0084) is less than the significance level (0.01), we reject the null hypothesis.

### Step 5: Compare the P-value with the Significance Level

At the 0.01 significance level, there is sufficient evidence to support the claim that the hospitalization rate for crashes of midsize cars equipped with air bags is lower than the 7.8% rate for crashes of midsize cars equipped with automatic safety belts but no air bags.


## Question 1

According to a study, 84% of U.S. children ages 8 to 18 had Internet
access at home as of August 2009. Researchers wonder if this number
has increased since then. The original sample consisted of 500 children,
and 86% of them had Internet access at home. Test the researchers’
claim at 5 % level of significance.

- $p = 0.84$
- $\hat{p} = 0.86$
- $x = 500$
- $\alpha = 0.05$, right tail test

### Step 1: State the Hypotheses

- $H_0: p = 0.84$
- $H_1: p > 0.84$

Here, $p$ is the proportion of children with Internet access at home in the current year.

### Step 2: Determine the Critical Value

Since the significance level \(\alpha\) is 0.05 and this is a one-tailed test, we look up the critical value for a right-tailed test in the Z-table.

- $Z_{\alpha} = Z_{0.05} \approx 1.645$

### Step 3: Calculate the Test Statistic

First, we need to calculate the sample proportion:

$$ \hat{p} = \frac{0.86 \times 500}{500} = 0.86 $$

Next, calculate the standard error (SE) using the null hypothesis proportion:

$$ \text{SE} = \sqrt{\frac{p_0 (1 - p_0)}{n}} = \sqrt{\frac{0.84 \times (1 - 0.84)}{500}} = \sqrt{\frac{0.84 \times 0.16}{500}} \approx 0.016 $$

Now, calculate the Z-score:

$$ Z = \frac{\hat{p} - p_0}{\text{SE}} = \frac{0.86 - 0.84}{0.016} \approx 1.25 $$

### Step 4: Make a Decision

Compare the calculated Z-score with the critical value:

- If $Z \geq Z_{0.05}$, reject the null hypothesis.
- If $Z < Z_{0.05}$, fail to reject the null hypothesis.

Here, $1.25 < 1.645$, so we fail to reject the null hypothesis.

### Step 5: State the Conclusion

At the 5% significance level, there is insufficient evidence to support the claim that the proportion of U.S. children ages 8 to 18 with Internet access at home has increased since 2009.
