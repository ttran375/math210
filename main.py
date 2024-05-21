import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

X = np.array([3, 9, 12, 13, 17, 21])
Y = np.array([15, 21, 30, 33, 42, 56])

plt.scatter(X, Y, color='blue', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

model_summary = model.summary()
intercept, slope = model.params
intercept_rounded = round(intercept, 1)
slope_rounded = round(slope, 1)

print(f'The equation of the line of best fit: y = {slope_rounded}x + {intercept_rounded}')
