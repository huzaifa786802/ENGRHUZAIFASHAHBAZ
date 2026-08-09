import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(12, 16))
ax.set_xlim(0, 10)
ax.set_ylim(0, 16)
ax.axis('off')

# Background
bg = Rectangle((0, 0), 10, 16, facecolor='#f5f5f0', edgecolor='none')
ax.add_patch(bg)

# Fiverr badge (top right corner)
fiverr_triangle = plt.Polygon([[8, 16], [10, 16], [10, 14.5]], 
                               facecolor='#1d7a54', edgecolor='none')
ax.add_patch(fiverr_triangle)
ax.text(9.3, 15.2, 'fiverr', fontsize=12, color='white', 
        weight='bold', rotation=-45, ha='center')

# Header: "I WILL TEACH"
ax.text(5, 15, 'I WILL TEACH', fontsize=32, weight='bold', 
        ha='center', va='top', color='#2c3e50')

# Green banner: "MECHANICAL ENGINEERING ONLINE"
banner = FancyBboxPatch((1.5, 13.8), 7, 0.8, boxstyle="round,pad=0.1",
                         facecolor='#1d7a54', edgecolor='none')
ax.add_patch(banner)
ax.text(5, 14.2, 'MECHANICAL ENGINEERING ONLINE', fontsize=16, 
        weight='bold', ha='center', va='center', color='white')

# Chapter 1
ax.text(0.8, 12.8, 'CHAPTER 1', fontsize=14, color='#555555')

# IC ENGINES title
ax.text(0.8, 12.2, 'IC ENGINES', fontsize=48, weight='bold', 
        color='#1d7a54', va='top')

# Yellow "INTRODUCTION" badge
intro_box = FancyBboxPatch((0.8, 11), 2.5, 0.5, boxstyle="round,pad=0.05",
                           facecolor='#fbbf24', edgecolor='none')
ax.add_patch(intro_box)
ax.text(2.05, 11.25, 'INTRODUCTION', fontsize=14, weight='bold', 
        ha='center', va='center', color='#000000')

# Left side - Engine illustration placeholder
engine_box = FancyBboxPatch((0.8, 6.5), 4, 4, boxstyle="round,pad=0.1",
                            facecolor='white', edgecolor='#cccccc', linewidth=2)
ax.add_patch(engine_box)
ax.text(2.8, 8.5, '⚙️', fontsize=80, ha='center', va='center')
ax.text(2.8, 7.3, 'IC ENGINE', fontsize=12, ha='center', 
        va='center', color='#555555', style='italic')

# Right side - Information box
info_box = FancyBboxPatch((5.2, 9), 4.2, 4, boxstyle="round,pad=0.1",
                          facecolor='white', edgecolor='#cccccc', linewidth=2)
ax.add_patch(info_box)

# Info box header
info_header = Rectangle((5.3, 12.5), 4, 0.4, facecolor='#1d7a54', edgecolor='none')
ax.add_patch(info_header)
ax.text(7.3, 12.7, 'What is an Internal Combustion Engine?', 
        fontsize=10, weight='bold', ha='center', va='center', color='white')

# Info box text
info_text = ('An internal combustion engine is a heat engine\n'
             'that converts chemical energy of a fuel into\n'
             'mechanical energy, usually made available on\n'
             'a rotating output shaft.')
ax.text(7.3, 11.2, info_text, fontsize=9, ha='center', va='top', 
        color='#333333', linespacing=1.5)

# Energy conversion icons
ax.text(6.2, 9.8, '⚡', fontsize=30, ha='center')
ax.text(6.2, 9.3, 'Chemical\nEnergy', fontsize=8, ha='center', color='#555555')

ax.text(7.3, 9.8, '→', fontsize=30, ha='center', color='#1d7a54')

ax.text(8.4, 9.8, '⚙️', fontsize=30, ha='center')
ax.text(8.4, 9.3, 'Mechanical\nEnergy', fontsize=8, ha='center', color='#555555')

# Instructor photo placeholder
photo_box = FancyBboxPatch((5.2, 6.5), 4.2, 2.2, boxstyle="round,pad=0.1",
                           facecolor='white', edgecolor='#cccccc', linewidth=2)
ax.add_patch(photo_box)
ax.text(7.3, 7.6, '👨‍🏫', fontsize=60, ha='center', va='center')
ax.text(7.3, 6.8, 'Instructor', fontsize=10, ha='center', 
        va='center', color='#555555', style='italic')

# Feature boxes
features = [
    ('✓', 'Clear Conceptual Teaching', 0.8),
    ('✓', 'Exam Preparation & Guidance', 3.7),  # Fixed spelling: "Exam"
    ('✓', 'PowerPoint Slides + Notes', 6.6)
]

for icon, text, x_pos in features:
    feature_box = FancyBboxPatch((x_pos, 5.2), 2.6, 0.6, 
                                 boxstyle="round,pad=0.05",
                                 facecolor='white', edgecolor='#cccccc', 
                                 linewidth=1.5)
    ax.add_patch(feature_box)
    ax.text(x_pos + 0.3, 5.5, icon, fontsize=20, color='#1d7a54', 
            weight='bold', va='center')
    ax.text(x_pos + 1.4, 5.5, text, fontsize=9, weight='bold', 
            ha='center', va='center', color='#333333')

# "BOOK A LECTURE NOW" button
button = FancyBboxPatch((0.8, 3.5), 4, 0.8, boxstyle="round,pad=0.1",
                        facecolor='#1d7a54', edgecolor='none')
ax.add_patch(button)
ax.text(2.8, 3.9, 'BOOK A LECTURE NOW', fontsize=16, weight='bold', 
        ha='center', va='center', color='white')

# Live lectures box
lecture_box = FancyBboxPatch((5.2, 2.5), 4.2, 2.5, boxstyle="round,pad=0.1",
                             facecolor='white', edgecolor='#cccccc', linewidth=2)
ax.add_patch(lecture_box)

# Video camera icon and text
ax.text(5.6, 4.6, '🎥', fontsize=20, va='center')
ax.text(7.3, 4.6, 'LIVE LECTURES ON ZOOM', fontsize=10, weight='bold', 
        ha='center', va='center', color='#333333')

# Star rating
stars_x = 6.0
for i in range(5):
    ax.text(stars_x + i*0.3, 4.1, '⭐', fontsize=16, va='center')

ax.text(7.8, 4.1, '5.0', fontsize=18, weight='bold', va='center', color='#333333')
ax.text(8.6, 4.1, 'GOOGLE MEET', fontsize=9, va='center', color='#666666')

# Instructor details
instructor_text = 'Engr. Shahbaz Ghani, BS, MS in Mechanical Engineering'
ax.text(7.3, 3.4, instructor_text, fontsize=9, ha='center', 
        va='center', color='#333333')

# Decorative line
ax.plot([0.8, 9.2], [2.2, 2.2], color='#1d7a54', linewidth=2, alpha=0.3)

# Additional decorative elements
ax.text(5, 1.5, 'Professional Online Mechanical Engineering Tutoring', 
        fontsize=11, ha='center', va='center', color='#555555', style='italic')

# Set tight layout
plt.tight_layout()

# Save the figure
plt.savefig('ic_engines_poster.png', dpi=300, bbox_inches='tight', 
            facecolor='#f5f5f0')
print("Poster saved as 'ic_engines_poster.png'")

# Display the plot
plt.show()