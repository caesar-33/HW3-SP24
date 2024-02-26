import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def func1(x):
    """
        Define the first function based on the given equation.

        Parameters:
        - x (float or array-like): The input value(s) for the function.

        Returns:
        - The output of the function x - 3*cos(x).
        """
    return x - 3 * np.cos(x)

def func2(x):
    """
        Define the second function based on the given equation.

        Parameters:
        - x (float or array-like): The input value(s) for the function.

        Returns:
        - The output of the function cos(2*x)*x**3.
        """
    return np.cos(2 * x) * x**3

def find_intersection(x):
    """
        Calculate the difference between the two defined functions to find intersection points.

        Parameters:
        - x (float): The input value for the functions.

        Returns:
        - The difference between func1(x) and func2(x).
        """
    return func1(x) - func2(x)

# Finding roots for the individual functions near 0
root_func1 = fsolve(func1, 0.0)
root_func2 = fsolve(func2, 0.0)

# Setting up a range of initial guesses to find intersection points
initial_guesses = np.linspace(-15, 15, 300)
intersection_points = []

for guess in initial_guesses:
    x, infodict, ier, mesg = fsolve(find_intersection, guess, full_output=True)
    # Check if the solution converged and the solution is not already in the list
    if ier == 1 and not x[0] in intersection_points:
        intersection_points.append(x[0])

# Filtering unique solutions by rounding and taking the set to remove near-duplicates
intersection_points = set(np.round(intersection_points, decimals=5))

# Plotting
x = np.linspace(-15, 15, 400)
y1 = func1(x)
y2 = func2(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='x - 3*cos(x)')
plt.plot(x, y2, label='cos(2*x)*x^3')
plt.scatter(list(intersection_points), [func1(x) for x in intersection_points], color='red', zorder=5)
plt.title('Graphs of func1 and func2 with Intersection Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Output the roots and intersection points
print("Root of func1 (x - 3*cos(x) = 0):", root_func1)
print("Root of func2 (cos(2*x)*x^3 = 0):", root_func2)
print("Intersection points:", intersection_points)
