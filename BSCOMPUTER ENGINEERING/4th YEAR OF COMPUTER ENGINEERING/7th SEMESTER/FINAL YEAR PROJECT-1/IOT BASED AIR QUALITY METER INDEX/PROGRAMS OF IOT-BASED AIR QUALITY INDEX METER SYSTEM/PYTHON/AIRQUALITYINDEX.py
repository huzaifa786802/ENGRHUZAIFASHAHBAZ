import matplotlib.pyplot as plt
import numpy as np
# Define the locations of the cities on the map with placeholder sensor data
cities = {
    "London": (51.5074, 0.1278, 10, 20, {"SO2": 1, "NO2": 5, "O3": 10, "CO": 2}),
    "Paris": (48.8566, 2.3522, 12, 25, {"SO2": 2, "NO2": 3, "O3": 9, "CO": 3}),
    "Tokyo": (35.6895, 139.6917, 8, 18, {"SO2": 1, "NO2": 4, "O3": 7, "CO": 1}),
    "Sydney": (-33.8688, 151.2093, 5, 15, {"SO2": 0, "NO2": 2, "O3": 8, "CO": 0}),
    "Rio de Janeiro": (-22.9068, -43.1729, 15, 30, {"SO2": 3, "NO2": 6, "O3": 12, "CO": 4}),
    "Moscow": (55.7558, 37.6173, 20, 40, {"SO2": 4, "NO2": 7, "O3": 10, "CO": 6}),
    "Beijing": (39.9042, 116.4074, 35, 60, {"SO2": 5, "NO2": 10, "O3": 15, "CO": 8}),
    "Delhi": (28.6139, 77.2090, 40, 70, {"SO2": 6, "NO2": 12, "O3": 20, "CO": 10}),
    "Cairo": (30.0444, 31.2357, 25, 50, {"SO2": 3, "NO2": 8, "O3": 13, "CO": 7}),
    "Karachi": (24.8607, 67.0011, 30, 55, {"SO2": 4, "NO2": 9, "O3": 16, "CO": 9}),
    "Lahore": (31.5497, 74.3436, 32, 58, {"SO2": 5, "NO2": 10, "O3": 18, "CO": 7}),
    "Islamabad": (33.6844, 73.0479, 20, 40, {"SO2": 2, "NO2": 5, "O3": 10, "CO": 3}),
    "Peshawar": (34.0151, 71.5249, 28, 50, {"SO2": 3, "NO2": 6, "O3": 12, "CO": 5}),
    "Quetta": (30.1798, 66.9750, 22, 45, {"SO2": 3, "NO2": 7, "O3": 11, "CO": 6}),
}
# Create a scatter plot of the cities with sensor data
plt.figure(figsize=(12, 8))
for city, (lat, lon, pm25, pm10, gases) in cities.items():
    # Scatter the city locations with PM2.5 and PM10 values
    plt.scatter(lon, lat, label=f"{city} (PM2.5: {pm25}, PM10: {pm10})")
    # Optionally, you can print the gas sensor data in the labels
    gas_info = ", ".join([f"{key}: {value}" for key, value in gases.items()])
    print(f"{city}: PM2.5: {pm25}, PM10: {pm10}, Gases: {gas_info}")
# Add labels and title
plt.title("City Locations with Air Quality Sensor Data")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid()
# Show the plot
plt.show()