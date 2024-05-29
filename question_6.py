import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = [2.1, 2.3, 4.7, 7.9, 5.5, 6.6, 6.4, 12.4, 6.8, 12.5, 9.3, 8.3, 12.7, 3.8, 11.2, 11.2, 11.5, 11.7, 14.3, 23.4]
df = pd.DataFrame(data, columns=['Minutes'])

mean = df['Minutes'].mean()
median = df['Minutes'].median()
mode = df['Minutes'].mode()[0]
std_dev = df['Minutes'].std()
variance = df['Minutes'].var()
quartiles = df['Minutes'].quantile([0.25, 0.5, 0.75])

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Quartiles:\n{quartiles}")

plt.hist(df['Minutes'], bins=10, edgecolor='black')
plt.title('Histogram of Minutes to Solve a Problem')
plt.xlabel('Minutes')
plt.ylabel('Frequency')
plt.show()
