import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd

# Years from 2020 to 2024
years = np.array([2020, 2021, 2022, 2023, 2024])
months = np.array(['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'])

# Energy consumption data (in kWh per 1000 operations) - realistic trends
# Traditional routing shows gradual improvement due to hardware advances
traditional_routing = np.array([850, 820, 795, 775, 760])

# Network coding shows more significant improvement due to algorithmic advances
network_coding = np.array([520, 475, 425, 380, 340])

# Energy reduction percentage over years
energy_reduction = ((traditional_routing - network_coding) / traditional_routing) * 100

# Quarterly data for 2024 (more detailed view)
quarters_2024 = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
traditional_2024 = np.array([770, 765, 762, 760])
network_coding_2024 = np.array([355, 348, 342, 340])

# Create comprehensive visualization
fig = plt.figure(figsize=(18, 12))

# Main comparison plot (2020-2024)
ax1 = plt.subplot(2, 3, (1, 2))
ax1.plot(years, traditional_routing, 'r-o', linewidth=3, markersize=8, 
         label='Traditional Routing', marker='o', markerfacecolor='red', markeredgecolor='darkred')
ax1.plot(years, network_coding, 'b-s', linewidth=3, markersize=8, 
         label='Network Coding', marker='s', markerfacecolor='blue', markeredgecolor='darkblue')

# Fill area showing energy savings
ax1.fill_between(years, traditional_routing, network_coding, 
                alpha=0.3, color='green', label='Energy Saved')

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Energy Consumption (kWh/1000 ops)', fontsize=12, fontweight='bold')
ax1.set_title('Network Coding vs Traditional Routing Energy Consumption (2020-2024)', 
              fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(2019.5, 2024.5)

# Add trend annotations
ax1.annotate('38.8% reduction', xy=(2020, 520), xytext=(2020.5, 600),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=10, fontweight='bold', color='green')
ax1.annotate('55.3% reduction', xy=(2024, 340), xytext=(2023.2, 450),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=10, fontweight='bold', color='green')

# Energy reduction percentage over time
ax2 = plt.subplot(2, 3, 3)
bars = ax2.bar(years, energy_reduction, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'], 
               edgecolor='black', linewidth=1.5)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Energy Reduction (%)', fontsize=12, fontweight='bold')
ax2.set_title('Energy Reduction Percentage', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

# Add percentage labels on bars
for bar, reduction in zip(bars, energy_reduction):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{reduction:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)

# 2024 Quarterly breakdown
ax3 = plt.subplot(2, 3, 4)
x_pos = np.arange(len(quarters_2024))
width = 0.35

bars1 = ax3.bar(x_pos - width/2, traditional_2024, width, label='Traditional Routing', 
                color='red', alpha=0.7)
bars2 = ax3.bar(x_pos + width/2, network_coding_2024, width, label='Network Coding', 
                color='blue', alpha=0.7)

ax3.set_xlabel('Quarter', fontsize=12, fontweight='bold')
ax3.set_ylabel('Energy (kWh/1000 ops)', fontsize=12, fontweight='bold')
ax3.set_title('2024 Quarterly Performance', fontsize=12, fontweight='bold')
ax3.set_xticks(x_pos)
ax3.set_xticklabels(quarters_2024, rotation=45)
ax3.legend()
ax3.grid(True, alpha=0.3, axis='y')

# Cumulative energy savings
ax4 = plt.subplot(2, 3, 5)
annual_savings = traditional_routing - network_coding
cumulative_savings = np.cumsum(annual_savings)

ax4.plot(years, cumulative_savings, 'g-o', linewidth=3, markersize=8, color='darkgreen')
ax4.fill_between(years, 0, cumulative_savings, alpha=0.3, color='lightgreen')
ax4.set_xlabel('Year', fontsize=12, fontweight='bold')
ax4.set_ylabel('Cumulative Savings (kWh/1000 ops)', fontsize=12, fontweight='bold')
ax4.set_title('Cumulative Energy Savings', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3)

# Technology advancement impact
ax5 = plt.subplot(2, 3, 6)
technologies = ['Linear NC\n(2020)', 'Random NC\n(2021)', 'Adaptive NC\n(2022)', 'AI-Enhanced\n(2023)', 'Quantum-Inspired\n(2024)']
efficiency_gains = [38.8, 42.1, 46.5, 51.0, 55.3]

bars = ax5.bar(range(len(technologies)), efficiency_gains, 
               color=['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6'])
ax5.set_xlabel('Technology Evolution', fontsize=12, fontweight='bold')
ax5.set_ylabel('Efficiency Gain (%)', fontsize=12, fontweight='bold')
ax5.set_title('Technology Impact on Efficiency', fontsize=12, fontweight='bold')
ax5.set_xticks(range(len(technologies)))
ax5.set_xticklabels(technologies, rotation=0, ha='center', fontsize=9)

# Add efficiency labels
for i, gain in enumerate(efficiency_gains):
    ax5.text(i, gain + 1, f'{gain}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()

# Print comprehensive statistics
print("=== NETWORK CODING ENERGY ANALYSIS (2020-2024) ===")
print(f"Energy Reduction Improvement: {energy_reduction[0]:.1f}% (2020) → {energy_reduction[-1]:.1f}% (2024)")
print(f"Total Improvement: +{energy_reduction[-1] - energy_reduction[0]:.1f} percentage points")
print(f"Average Annual Improvement: {(energy_reduction[-1] - energy_reduction[0])/4:.1f} percentage points/year")
print(f"2024 Energy Efficiency: {traditional_routing[-1]/network_coding[-1]:.2f}x better than traditional routing")

print(f"\nTotal Energy Saved (2020-2024): {np.sum(annual_savings):.0f} kWh per 1000 operations")
print(f"2024 Annual Savings: {annual_savings[-1]:.0f} kWh per 1000 operations")

# Detailed year-by-year breakdown
print("\n=== YEAR-BY-YEAR BREAKDOWN ===")
print("Year | Traditional | Network Coding | Savings | Reduction% | Tech Advancement")
print("-" * 85)
tech_names = ['Linear NC', 'Random NC', 'Adaptive NC', 'AI-Enhanced', 'Quantum-Inspired']
for i in range(len(years)):
    savings = traditional_routing[i] - network_coding[i]
    print(f"{years[i]} | {traditional_routing[i]:11.0f} | {network_coding[i]:14.0f} | {savings:7.0f} | {energy_reduction[i]:8.1f}% | {tech_names[i]}")

# Future projection
print(f"\n=== 2025 PROJECTION ===")
projected_traditional = 745  # Continued gradual improvement
projected_nc = 305  # Continued algorithmic advancement
projected_reduction = ((projected_traditional - projected_nc) / projected_traditional) * 100
print(f"Projected 2025: {projected_reduction:.1f}% energy reduction")
print(f"Projected improvement: +{projected_reduction - energy_reduction[-1]:.1f} percentage points")

plt.show()