import numpy as np
import matplotlib.pyplot as plt

# Number of data points
num_points = 100

# Generate synthetic PM2.5 and PM10 data (for example purposes)
PM2_5_data = np.random.rand(num_points) * 150  # PM2.5 values between 0 and 150 µg/m³
PM10_data = np.random.rand(num_points) * 200  # PM10 values between 0 and 200 µg/m³

# Create a time vector (for example purposes, using 1-second intervals)
time = np.arange(1, num_points + 1)

# Plotting the data
plt.plot(time, PM2_5_data, 'b-', linewidth=2, label='PM2.5')  # PM2.5 plot (blue)
plt.plot(time, PM10_data, 'r-', linewidth=2, label='PM10')  # PM10 plot (red)

# Adding labels and title
plt.xlabel('Time (seconds)')
plt.ylabel('Concentration (µg/m³)')
plt.title('PM2.5 and PM10 Concentration Over Time')
plt.legend()

# Display grid
plt.grid(True)

# Show the plot
plt.show()
