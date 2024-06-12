# Hypotheses testing for a population proportion

## Question 1

In a study of air-bags effectiveness, it was found that in 821 crashes of
midsize cars equipped with air bags, 46 of the crashes resulted in
hospitalization of the drivers. Use a 0.01 significance level to test the
claim that the air bag hospitalization rate is lower than 7.8% rate for
crashes of midsize cars equipped with automatic safety belts but no air
bags.

### Step 1: Define the Hypotheses

- Null Hypothesis ($H_0$): The hospitalization rate for crashes with air bags is equal to 7.8%, $ p = 0.078 $.
- Alternative Hypothesis ($H_a$): The hospitalization rate for crashes with air bags is less than 7.8%, $ p < 0.078 $.

### Step 2: Calculate the Test Statistic

- Sample size ($n$): 821
- Number of hospitalizations ($x$): 46
- Hypothesized population proportion ($p_0$): 0.078

$$ \hat{p} = \frac{46}{821} \approx 0.056 $$

$$ \text{SE} = \sqrt{\frac{p_0 (1 - p_0)}{n}} = \sqrt{\frac{0.078 \times (1 - 0.078)}{821}} \approx 0.0092 $$

$$ Z = \frac{\hat{p} - p_0}{\text{SE}} = \frac{0.056 - 0.078}{0.0092} \approx -2.39 $$

### Step 3: Determine the P-value

We use the Z-test statistic to find the P-value. Since this is a one-tailed test (we are testing if the rate is less than 7.8%), we find the area to the left of the Z-test statistic in the standard normal distribution.

Using a Z-table or standard normal distribution calculator, we find the P-value for $ Z = -2.39 $:

\[ \text{P-value} \approx 0.0084 \]

### Step 4: Compare the P-value with the Significance Level

- Significance level ($\alpha$): 0.01

Since the P-value (0.0084) is less than the significance level (0.01), we reject the null hypothesis.

### Conclusion

At the 0.01 significance level, there is sufficient evidence to support the claim that the hospitalization rate for crashes of midsize cars equipped with air bags is lower than the 7.8% rate for crashes of midsize cars equipped with automatic safety belts but no air bags.
