import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate y values for sine, cosine, and tangent functions
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot sine function
plt.plot(x, y_sin, label='sin(x)', color='b')

# Plot cosine function
plt.plot(x, y_cos, label='cos(x)', color='r')

# Plot tangent function with limited y-values to avoid extreme values
plt.plot(x, y_tan, label='tan(x)', color='g')
plt.ylim(-10, 10)  # Limit y-axis for better visibility

# Add titles and labels
plt.title('Trigonometric Functions')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()

