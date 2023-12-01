import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Simulating data for 100 college students
np.random.seed(0)
data = {
    'Stress_Level': np.random.normal(50, 10, 100),  # Stress levels (mean = 50, std = 10)
    'Sleep_Quality': np.random.normal(70, 15, 100),  # Sleep quality index (mean = 70, std = 15)
    'Cognitive_Performance': np.random.normal(60, 12, 100)  # Cognitive test scores (mean = 60, std = 12)
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Performing Multivariate Regression Analysis
# Cognitive Performance is the dependent variable, and Stress and Sleep Quality are independent variables
X = df[['Stress_Level', 'Sleep_Quality']]
Y = df['Cognitive_Performance']

# Adding a constant to the model (intercept)
X = sm.add_constant(X)

# Fitting the model
model = sm.OLS(Y, X).fit()

# Summary of the regression
regression_summary = model.summary()

# Scatter plot for Stress Level vs Cognitive Performance
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(df['Stress_Level'], df['Cognitive_Performance'], color='blue')
plt.title('Stress Level vs Cognitive Performance')
plt.xlabel('Stress Level')
plt.ylabel('Cognitive Performance')

# Scatter plot for Sleep Quality vs Cognitive Performance
plt.subplot(1, 2, 2)
plt.scatter(df['Sleep_Quality'], df['Cognitive_Performance'], color='green')
plt.title('Sleep Quality vs Cognitive Performance')
plt.xlabel('Sleep Quality')
plt.ylabel('Cognitive Performance')

plt.tight_layout()
plt.show()
