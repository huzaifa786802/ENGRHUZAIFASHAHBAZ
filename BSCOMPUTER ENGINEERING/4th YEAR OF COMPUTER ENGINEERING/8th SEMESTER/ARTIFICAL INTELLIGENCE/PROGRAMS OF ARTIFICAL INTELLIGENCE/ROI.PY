import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

# Set the style
plt.style.use('default')
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'sans-serif'

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [1, 1.2]})
fig.suptitle('Project Cost and ROI Projection', fontsize=16, fontweight='bold')

# Data for pie chart
labels = ['R&D Prototyping', 'Marketing & Distribution', 'Manufacturing Setup', 'Interest Rate Costs']
sizes = [16.9, 10.09, 23.04, 10.09]  # Values in PKR millions
colors = ['#007bff', '#dc3545', '#28a745', '#ffc107']  # Blue, Red, Green, Yellow
total_cost = sum(sizes)

# Create donut chart
wedges, texts, autotexts = ax1.pie(sizes, labels=None, colors=colors, autopct='', 
                                   startangle=90, wedgeprops={'width': 0.5})

# Add a white circle at the center
centre_circle = plt.Circle((0, 0), 0.25, fc='white')
ax1.add_artist(centre_circle)

# Add center text
ax1.text(0, 0, f'Total\n{total_cost:.2f}M PKR', ha='center', va='center', fontsize=12, fontweight='bold')

# Create custom legend
ax1.legend(wedges, [f'{labels[i]} ({sizes[i]}M PKR)' for i in range(len(labels))], 
          loc='center left', bbox_to_anchor=(-0.3, 0))

# ROI projection data (months vs revenue in PKR millions)
months = np.arange(0, 37, 1)
# Creating an S-curve for revenue growth
revenue = np.zeros_like(months, dtype=float)
for i, month in enumerate(months):
    if month < 6:
        revenue[i] = month * 5  # Initial slow growth
    elif month < 18:
        revenue[i] = 30 + (month - 6) * 15  # Accelerated growth phase
    else:
        revenue[i] = 210 + (month - 18) * 5 * np.exp(-0.1 * (month - 18))  # Plateau phase

# Plot revenue projection
ax2.plot(months, revenue, color='#28a745', linewidth=3)
ax2.set_xlabel('Months After Launch')
ax2.set_ylabel('Revenue (PKR Millions)')
ax2.grid(True, linestyle='--', alpha=0.7)

# Add break-even point
break_even_month = 16  # Based on the image
break_even_value = revenue[break_even_month]

# Add horizontal line for total cost
ax2.axhline(y=total_cost, color='#dc3545', linestyle='--', alpha=0.8)

# Mark break-even point
ax2.scatter(break_even_month, break_even_value, s=80, facecolors='#ff7f0e', edgecolors='black', zorder=5)
ax2.annotate(f'Break-even ({break_even_month} months)', 
             xy=(break_even_month, break_even_value),
             xytext=(break_even_month + 2, break_even_value - 10),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=10)

# Add vertical line from break-even point
ax2.plot([break_even_month, break_even_month], [0, break_even_value], color='#ff7f0e', linestyle='--')

# Set limits
ax2.set_xlim(0, 36)
ax2.set_ylim(0, 300)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.9)

plt.show()

# For saving the figure
# plt.savefig('project_cost_roi_projection.png', dpi=300, bbox_inches='tight')