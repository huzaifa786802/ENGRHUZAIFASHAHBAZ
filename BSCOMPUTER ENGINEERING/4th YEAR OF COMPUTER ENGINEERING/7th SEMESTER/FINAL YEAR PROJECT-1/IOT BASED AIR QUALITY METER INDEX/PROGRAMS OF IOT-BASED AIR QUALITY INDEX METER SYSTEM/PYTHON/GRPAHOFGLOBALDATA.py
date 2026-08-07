import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
# Example: Prepare sample data (Replace with API-collected data)
data = pd.DataFrame({
    'city': ['Los Angles', 'London', 'CapeTown', 'Tokyo', 'Sydney'],
    'latitude': [40.7128, 51.5074, 28.6139, 35.6895, -33.8688],
    'longitude': [-74.0060, -0.1278, 77.2090, 139.6917, 151.2093],
    'pm2_5': [12, 18, 45, 25, 10],
    'pm10': [20, 25, 60, 35, 15]
})
# Plot global air quality
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
fig, ax = plt.subplots(figsize=(12, 8))
world.plot(ax=ax, color='lightgrey')
# Plot PM data
scatter = ax.scatter(
    data['longitude'], data['latitude'], 
    c=data['pm2_5'], cmap='Reds', s=100, alpha=0.7
)
# Add color bar and labels
plt.colorbar(scatter, label='PM2.5 Concentration (µg/m³)')
plt.title("Global Air Quality (PM2.5)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()