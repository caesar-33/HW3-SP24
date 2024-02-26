import numpy as np
from scipy.linalg import solve

# Define the coefficient matrices and the right-hand side vectors for both systems
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])
b1 = np.array([2, 12, 10])

A2 = np.array([[1, -10, 2, 4],
               [3, 1, 4, 12],
               [9, 2, 3, 4],
               [-1, 2, 7, 3]])
b2 = np.array([2, 12, 21, 37])

# Solve the systems of equations
solution_1 = solve(A1, b1)
solution_2 = solve(A2, b2)

# Display the solutions
def display_solution(solution, title):
    """
        Solve a system of linear equations given the coefficients and constants.

        Parameters:
        - coefficients: A numpy array of shape (n, n) representing the coefficients of the system.
        - constants: A numpy array of shape (n,) representing the constant terms of the system.

        Returns:
        - A numpy array containing the solution to the system of equations.

        The function uses scipy's 'solve' method to find the solution of the linear system
        represented by Ax = B, where A is the matrix of coefficients, and B is the vector
        of constants.

        Example:
        >>> A = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
        >>> B = np.array([2, 12, 10])
        >>> solve_linear_system(A, B)
        array([1., 2., 3.])
        """
    print(title)
    for i, x in enumerate(solution, start=1):
        print(f"x_{i} = {x:.2f}")
    print("\n")

display_solution(solution_1, "Solution for the first matrix problem:")
display_solution(solution_2, "Solution for the second matrix problem:")
