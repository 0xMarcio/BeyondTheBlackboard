import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FactorAnalysis


# Generating a synthetic dataset
np.random.seed(2)
num_items = 10  # Number of test items
num_factors = 2  # We assume there are 2 underlying personality traits
num_responses = 100  # Number of respondents

# Simulate responses to the personality assessment
responses = np.random.normal(size=(num_responses, num_items))

# Applying Factor Analysis
fa = FactorAnalysis(n_components=num_factors, random_state=0)
fa.fit(responses)

# Factor loadings
factor_loadings = fa.components_.T

# Visualizing factor loadings
plt.figure(figsize=(10, 6))
sns.heatmap(factor_loadings, annot=True, cmap='coolwarm', center=0)
plt.title('Factor Loadings - Personality Assessment')
plt.xlabel('Factor')
plt.ylabel('Test Item')
plt.show()

factor_loadings

