import matplotlib.pyplot as plt
from math import sqrt
# Sample data



#deepmind flops 270 * 79 * 20

# DM, alpha

x = [426600, 64 * 27.6 * 20, 160 * 64, 160 * 64 * 20]  # X-coordinates (FLOPS (b))
y = [40, 18, 50, 71] # Y-coordinates
sizes = [270, 27.6, 160, 160]  # Bubble sizes

sizes = [sqrt(sz) * 10 for sz in sizes]  # Adjust the sizes
x = [x_ / 1e3 for x_ in x]  # Convert mflops to gflops

labels = ['GC-270M', 'AlphaZero value', 'BT4 policy', 'BT4 value']  # Labels for each point
colors = ['blue', 'blue', 'red', 'red']

# Create the scatter plot
plt.figure(figsize=(10, 6))  # Set figure size
scatter = plt.scatter(x, y, s=sizes, alpha=0.5, c=colors, edgecolors='w', linewidth=0.5)

# Add titles and labels
plt.title('Scatter Plot with Different Sized Bubbles and Labels')
plt.xlabel('FLOPS (B) ')
plt.ylabel('Elo')

# Add labels to the points
for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, fontsize=12, ha='right', va='bottom')

# Show grid
plt.grid(True)

# Display the plot
plt.show()