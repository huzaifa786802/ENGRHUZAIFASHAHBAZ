import numpy as np
import matplotlib.pyplot as plt
# Time vector (in seconds)
time = np.arange(0, 50.1, 0.1)  # 0 to 50 seconds with 0.1-second intervals
# Simulated gas concentrations (ppm - parts per million)
# Replace these with real data if available
mq135_data = 200 + 50 * np.sin(0.2 * time) + np.random.randn(len(time)) * 5  # Simulated for CO2, NO2, etc.
mq5_data = 300 + 70 * np.cos(0.15 * time) + np.random.randn(len(time)) * 10  # Simulated for LPG, CH4, etc.
# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(time, mq135_data, 'b-', linewidth=1.5, label='MQ-135 (e.g., SO2, NO2, O3, CO)')
plt.plot(time, mq5_data, 'r--', linewidth=1.5, label='MQ-5 (e.g., SnO2, H2, LPG, CH4, CO, Alcohol)')
# Customize the plot
plt.title('Gas Concentrations from MQ-135 and MQ-5 Sensors')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (ppm)')
plt.legend()
plt.grid(True)
# Highlight thresholds (optional)
plt.axhline(y=400, color='k', linestyle='--', label='Threshold 1 (MQ-135)')
plt.axhline(y=500, color='k', linestyle=':', label='Threshold 2 (MQ-5)')
# Show the plot
plt.tight_layout()
plt.show()