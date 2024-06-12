# Hypotheses testing for a population proportion

## Question 1

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


### Step 1: Define the left tail Hypotheses

- $H_0: p = 0.078$
- $H_1: p < 0.078$

### Step 2: Calculate the Test Statistic

$$ \hat{p} = \frac{46}{821} \approx 0.056 $$

$$ \text{SE} = \sqrt{\frac{p (1 - p)}{n}} = \sqrt{\frac{0.078 \times (1 - 0.078)}{821}} \approx 0.0092 $$

$$ Z = \frac{\hat{p} - p}{\text{SE}} = \frac{0.056 - 0.078}{0.0092} \approx -2.39 $$

### Step 3: Determine the P-value

We use the Z-test statistic to find the P-value. Since this is a one-tailed test (we are testing if the rate is less than 7.8%), we find the area to the left of the Z-test statistic in the standard normal distribution.

Using a Z-table or standard normal distribution calculator, we find the P-value for $ Z = -2.39 $:

\[ \text{P-value} \approx 0.0084 \]

### Step 4: Compare the P-value with the Significance Level

- Significance level ($\alpha$): 0.01

Since the P-value (0.0084) is less than the significance level (0.01), we reject the null hypothesis.

### Conclusion

At the 0.01 significance level, there is sufficient evidence to support the claim that the hospitalization rate for crashes of midsize cars equipped with air bags is lower than the 7.8% rate for crashes of midsize cars equipped with automatic safety belts but no air bags.
