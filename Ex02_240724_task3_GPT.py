import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt

def numeric_derivative(f, x0, order, dx=1e-5):
    """
    Compute the numerical derivative of a function f at point x0 using finite differences.
    
    Parameters:
    f : function
        The function whose derivative is to be computed.
    x0 : float
        The point at which to compute the derivative.
    order : int
        The order of the derivative to compute.
    dx : float
        The finite difference step size.
        
    Returns:
    float
        The numerical derivative of the function at x0.
    """
    return derivative(f, x0, n=order, dx=dx)

def taylor_series_approximation(f, x0, x, N):
    """
    Compute the Taylor series expansion of the function f(x) around the point x0
    up to the N-th order using numerical derivatives.
    
    Parameters:
    f : function
        The function to be approximated.
    x0 : float
        The point around which the Taylor series is expanded.
    x : numpy array
        Array of x values.
    N : int
        The order of the Taylor series.
    
    Returns:
    numpy array
        The Taylor series expansion evaluated at the given x values.
    """
    # Initialize the Taylor series approximation
    taylor_approx = np.zeros_like(x)
    
    for n in range(N + 1):
        # Compute the n-th derivative at x0
        f_n_x0 = numeric_derivative(f, x0, n)
        # Construct the n-th term of the Taylor series
        taylor_approx += f_n_x0 * (x - x0)**n / np.math.factorial(n)
    
    return taylor_approx

# Define the function to be approximated
def reference_function(x):
    return np.exp(-2 * x - 1)

# Parameters for the Taylor series expansion
x0 = -0.5
N = 4

# Define the range of x
x_vals = np.linspace(-1, 4, 400)

# Compute the Taylor series approximation
taylor_vals = taylor_series_approximation(reference_function, x0, x_vals, N)
f_vals = reference_function(x_vals)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label='Reference function f(x)')
plt.plot(x_vals, taylor_vals, label='Taylor Series Approximation', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Reference Function vs. Taylor Series Approximation')
plt.legend()
plt.grid(True)
plt.show()
