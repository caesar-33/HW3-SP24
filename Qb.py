import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#ChatGPT was used to help solve this problem


def equation1(x):
    """
    Compute the value of the first equation: x - 3 * cos(x).

    Parameters:
    x (float or array_like): Input values.

    Returns:
    float or array_like: Value of the equation at the given input.
    """
    return x - 3 * np.cos(x)

def equation2(x):
    """
    Compute the value of the second equation: cos(2x) * x^3.

    Parameters:
    x (float or array_like): Input values.

    Returns:
    float or array_like: Value of the equation at the given input.
    """
    return np.cos(2*x) * x**3

# Define the range of x values for plotting
x_values = np.linspace(-10, 10, 400)

# Compute the y values for each equation
y_values_eq1 = equation1(x_values)
y_values_eq2 = equation2(x_values)

# Find the roots of equation 1
initial_guess_eq1 = np.array([-3.-2, -1, 0, 1, 2])
roots_eq1 = fsolve(equation1, initial_guess_eq1)

# Find the roots of equation 2
initial_guess_eq2 = np.array([-2, -1, 0, 1, 2])
roots_eq2 = fsolve(equation2, initial_guess_eq2)

# Plotting
plt.figure(figsize=(12, 6))  # Adjust figure size

# Plot equation 1
plt.plot(x_values, y_values_eq1, label='x - 3 * cos(x)')

# Plot equation 2
plt.plot(x_values, y_values_eq2, label='cos(2x) * x^3')

# Mark the roots of equation 1
plt.scatter(roots_eq1, equation1(roots_eq1), color='red', label='Roots of Equation 1')

# Mark the roots of equation 2
plt.scatter(roots_eq2, equation2(roots_eq2), color='blue', label='Roots of Equation 2')

plt.axhline(y=0, color='black', linewidth=0.5)  # Add x-axis for reference

plt.title('Intersection of Two Equations')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Set x-axis limits
plt.xlim(-10, 10)  # Adjust to make it easier to view intersections by making the x-axis smaller
plt.ylim(-500, 500)  # Adjust to make it easier to view intersections by making the y-axis smaller


plt.show()
