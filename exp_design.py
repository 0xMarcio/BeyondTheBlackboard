import scipy.stats as stats
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Simulating data for the control and treatment groups
np.random.seed(1)
control_group = np.random.normal(loc=50, scale=10, size=30)  # Control group with standard treatment
treatment_group = np.random.normal(loc=45, scale=10, size=30)  # Treatment group with new therapy

# Perform a t-test
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)

# Visualizing the data
plt.figure(figsize=(10, 6))
sns.histplot(control_group, color="skyblue", label="Control Group", kde=True)
sns.histplot(treatment_group, color="red", label="Treatment Group", kde=True)
plt.title("Control vs. Treatment Group Outcomes")
plt.xlabel("Anxiety Level")
plt.ylabel("Frequency")
plt.legend()
plt.show()

(t_stat, p_value)

