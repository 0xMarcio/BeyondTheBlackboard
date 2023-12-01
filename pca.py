import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification

# Generate a synthetic dataset
np.random.seed(0)
X, _ = make_classification(n_samples=100, n_features=5, n_informative=3, n_redundant=2, 
                           n_clusters_per_class=1, random_state=42)

# Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 components for simplicity
X_pca = pca.fit_transform(X)

# Plotting the results
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', marker='o', edgecolor='k', s=70)
plt.title('PCA of Survey Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.show()

# Explained variance ratio
explained_variance = pca.explained_variance_ratio_

explained_variance

