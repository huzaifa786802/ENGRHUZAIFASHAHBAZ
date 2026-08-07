import numpy as np
import matplotlib.pyplot as plt
# Data
categories = ['Time Reduction', 'Accuracy', 'ROI Timeline', 'Scalability']
improvements = [80, 95, 15, 60]  # ROI Timeline visualized at ~15%
colors = ['#3399FF', '#66CC66', '#FFCC66', '#FF6666']
labels = ['Time Efficiency', 'Data Accuracy', 'ROI Timeline\n12–18 Months', 'Enterprise Scalability']
percent_labels = ['80 %', '95 %', '12–18 Months', '60 %']
# Plot
fig, ax = plt.subplots(figsize=(8, 5))
bars = plt.bar(categories, improvements, color=colors)
# Titles and labels
plt.title('Business Benefits of Industrial OMR Scanner', fontsize=14, weight='bold')
plt.ylabel('Improvement (%)')
plt.ylim(0, 100)
# Adding percentage labels above bars
for bar, label in zip(bars, percent_labels):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             label, ha='center', va='bottom', fontsize=10)
# Legend
plt.legend(labels, loc='upper right')
# Style and layout
plt.grid(False)
plt.tight_layout()
plt.show()