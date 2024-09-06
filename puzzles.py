import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ['Lc0-BT4\nPolicy\n196M params\n12.5B FLOPS', 'Lc0-BT4\nValue\n196M params\n251B FLOPS', 'DeepMind-270M\n Action-value \n 270M params\n427B FLOPS', 'AlphaZero\n27.6M params\n35.3B FLOP']

accuracy_2200_2400 = [70] * 4 # grey
accuracy_2400_2600 = [70] * 4  # orange
accuracy_2600_2800 = [70] * 4 # blue

# Position of bars on the x-axis
x = np.arange(len(categories))

# Bar width
width = 0.25

# Create a figure and axis
plt.xticks(rotation=0, ha='center')
fig, ax = plt.subplots(figsize=(1, len(categories)))

# Plotting the bars
bar1 = ax.bar(x - width, accuracy_2200_2400, width, label='2200-2400 elo', color='grey')
bar2 = ax.bar(x, accuracy_2400_2600, width, label='2400-2600 elo', color='orange')
bar3 = ax.bar(x + width, accuracy_2600_2800, width, label='2600-2800 elo', color='blue')



# Adding labels and title
ax.set_xlabel('Models')
ax.set_ylabel('Accuracy (%)')
ax.set_title('Lichess Puzzles - 1K Policy Head Tests')

# Adding the category labels to x-axis
ax.set_xticks(x)
ax.set_xticklabels(categories)

# Ensure x-axis labels are not slanted
plt.xticks(rotation=0, ha='center')

# Add a legend
ax.legend()

# Display the chart
plt.show()