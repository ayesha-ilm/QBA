import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class QuantitativeBiasAnalysis:
    def __init__(self, true_value, measured_value, bias_factor):
        self.true_value = true_value
        self.measured_value = measured_value
        self.bias_factor = bias_factor
    
    def adjusted_value(self):
        return self.measured_value / self.bias_factor
    
    def bias_correction(self):
        return self.true_value - self.adjusted_value()

np.random.seed(42)
true_returns = np.random.normal(0.05, 0.02, 100)
observed_returns = true_returns * np.random.uniform(0.9, 1.1, 100)
bias_factors = np.random.uniform(0.9, 1.1, 100)

adjusted_returns = [QuantitativeBiasAnalysis(t, o, b).adjusted_value() for t, o, b in zip(true_returns, observed_returns, bias_factors)]
corrections = [QuantitativeBiasAnalysis(t, o, b).bias_correction() for t, o, b in zip(true_returns, observed_returns, bias_factors)]

plt.figure(figsize=(10,5))
plt.plot(true_returns, label='True Returns', alpha=0.7)
plt.plot(observed_returns, label='Observed Returns', alpha=0.7)
plt.plot(adjusted_returns, label='Bias Adjusted Returns', linestyle='dashed')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Returns')
plt.title('Quantitative Bias Analysis in Financial Returns')
plt.show()

results_df = pd.DataFrame({
    'True Returns': true_returns,
    'Observed Returns': observed_returns,
    'Bias Adjusted Returns': adjusted_returns,
    'Correction Magnitude': corrections
})
print(results_df.describe())
