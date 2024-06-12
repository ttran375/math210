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

$$ \text{SE} = \sqrt{\frac{p (1 - p)}{n}} = \sqrt{\frac{0.078 \times (1 - 0.078)}{821}} \approx 0.0094 $$

$$ Z = \frac{\hat{p} - p}{\text{SE}} = \frac{0.056 - 0.078}{0.0092} \approx -2.35 $$

### Step 4

Since the P-value (0.0084) is less than the significance level (0.01), we reject the null hypothesis.

### Step 5: Compare the P-value with the Significance Level

At 1% level of significance, there is enough evidence to support the claim.

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

### Step 2: Determine the Critical Value

- $\alpha = 0.05$
- $Z_{\alpha} = Z_{0.05} \approx 1.645$

### Step 3: Calculate the Test Statistic

$$ \hat{p} = \frac{0.86 \times 500}{500} = 0.86 $$

$$ \text{SE} = \sqrt{\frac{p_0 (1 - p_0)}{n}} = \sqrt{\frac{0.84 \times (1 - 0.84)}{500}} = \sqrt{\frac{0.84 \times 0.16}{500}} \approx 0.016 $$

$$ Z = \frac{\hat{p} - p_0}{\text{SE}} = \frac{0.86 - 0.84}{0.016} \approx 1.22 $$

### Step 4: Make a Decision

Fail to reject $H_0$ (Do not reject $H_0$)

### Step 5: State the Conclusion

At 5% level of significance, there is not enough evidence to support the claim.

## Question 2

Data from the Center for Disease Control estimates that about 30.4%
of American teenagers were overweight in 2008.

- A professor in public health at a major university wants to determine
whether the proportion has decreased since 2008. He samples 800
randomly selected incoming freshman at universities around the
country. Using the BMI measurements, he finds that 210 of them are
overweight.
- If the professor uses a significance level of 0.10, what conclusion can he
draw?

### Given Data

- $p_0 = 0.304$
- $n = 800$
- $x = 210$
- $\alpha = 0.10$
- $ \hat{p} = \frac{x}{n} = \frac{210}{800} = 0.2625 $

### Step 1: State the Hypotheses

- $H_0: p = 0.304$
- $H_1: p < 0.304$

### Step 2: Determine the Critical Value

- $\alpha = 0.10$
- $Z_{\alpha} = Z_{0.10} \approx -1.28$

### Step 3: Calculate the Test Statistic

$$ \text{SE} = \sqrt{\frac{p_0 (1 - p_0)}{n}} = \sqrt{\frac{0.304 \times (1 - 0.304)}{800}} \approx 0.0163 $$

$$ Z = \frac{\hat{p} - p_0}{\text{SE}} = \frac{0.2625 - 0.304}{0.0163} \approx -2.55 $$

### Step 4: Make a Decision

Reject the null hypothesis $H_0$.

### Step 5: State the Conclusion

At the 10% level of significance, there is enough evidence to support the claim.

## Question 3

The NCHS report indicated that in 2002, 75% of children aged 2 to 17
saw a dentist in the past year. An investigator wants to assess whether
use of dental services is similar in children living in a certain city. A
sample of 125 children aged 2 to 17 living in that city are surveyed and
64 reported seeing a dentist over the past 12 months. Is there a
significant difference in use of dental services between children living in
that particular city and the national data?

## Hypotheses Testing for Population Proportion

### Given Data

- $p_0 = 0.75$
- $n = 125$
- $x = 64$
- $\alpha = 0.05$
- $\hat{p} = \frac{64}{125} \approx 0.512$

### Step 1: Two-tail test

- $H_0: p = 0.75$
- $H_1: p \neq 0.75$

### Step 2: Determine the Critical Value

- $\alpha = 0.05$
- $Z_{\alpha/2} \approx \pm 1.96$

### Step 3: Calculate the Test Statistic

1. Calculate the standard error (SE):

$$ \text{SE} = \sqrt{\frac{p_0 (1 - p_0)}{n}} = \sqrt{\frac{0.75 \times (1 - 0.75)}{125}} = \sqrt{\frac{0.75 \times 0.25}{125}} = \sqrt{\frac{0.1875}{125}} \approx 0.0387 $$

2. Calculate the Z-score:

$$ Z = \frac{\hat{p} - p_0}{\text{SE}} = \frac{0.512 - 0.75}{0.0387} \approx -6.15 $$

### Step 4: Make a Decision

- Compare the calculated Z-score with the critical values.
- Since $-6.15$ is much less than $-1.96$, we reject the null hypothesis $H_0$.

### Step 5: State the Conclusion

- At the 5% level of significance, there is enough evidence to conclude that there is a significant difference in the use of dental services between children living in the city and the national data from 2002.
