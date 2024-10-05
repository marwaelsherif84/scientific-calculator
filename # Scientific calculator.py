# Scientific calculator

import math
import statistics
import numpy as np

class ScientificCalculator:
    def __init__(self):
        self.memory = 0
    
    # Basic Arithmetic Operations
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    # Advanced Mathematical Functions
    def power(self, base, exp):
        return base ** exp
    
    def sqrt(self, x):
        if x < 0:
            return "Error: Negative root"
        return math.sqrt(x)
    
    def cbrt(self, x):
        return x ** (1/3)
    
    # Trigonometric Functions
    def sin(self, angle):
        return math.sin(math.radians(angle))
    
    def cos(self, angle):
        return math.cos(math.radians(angle))
    
    def tan(self, angle):
        return math.tan(math.radians(angle))
    
    # Hyperbolic Functions
    def sinh(self, x):
        return math.sinh(x)
    
    def cosh(self, x):
        return math.cosh(x)
    
    def tanh(self, x):
        return math.tanh(x)
    
    # Logarithmic Functions
    def ln(self, x):
        if x <= 0:
            return "Error: Logarithm of non-positive number"
        return math.log(x)
    
    def log10(self, x):
        if x <= 0:
            return "Error: Logarithm of non-positive number"
        return math.log10(x)
    
    def log2(self, x):
        if x <= 0:
            return "Error: Logarithm of non-positive number"
        return math.log2(x)
    
    def exp(self, x):
        return math.exp(x)
    
    # Statistical Functions
    def mean(self, data):
        return statistics.mean(data)
    
    def stddev(self, data):
        return statistics.stdev(data)
    
    def variance(self, data):
        return statistics.variance(data)
    
    def linear_regression(self, x, y):
        slope, intercept = np.polyfit(x, y, 1)
        return slope, intercept
    
    # Fractional and Integer Functions
    def factorial(self, n):
        if n < 0:
            return "Error: Factorial of negative number"
        return math.factorial(n)
    
    def nCr(self, n, r):
        if r > n or n < 0 or r < 0:
            return "Error: Invalid inputs"
        return math.comb(n, r)
    
    def nPr(self, n, r):
        if r > n or n < 0 or r < 0:
            return "Error: Invalid inputs"
        return math.perm(n, r)
    
    # Memory Functions
    def memory_store(self, value):
        self.memory = value
    
    def memory_recall(self):
        return self.memory
    
    def memory_add(self, value):
        self.memory += value
    
    def memory_subtract(self, value):
        self.memory -= value
    
    def memory_clear(self):
        self.memory = 0
    
    # Equation Solving
    def solve_linear(self, a, b):
        if a == 0:
            return "Error: No solution or infinite solutions"
        return -b / a
    
    def solve_quadratic(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "Error: No real roots"
        elif discriminant == 0:
            return -b / (2 * a)
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2
    
    # Matrix Operations
    def matrix_add(self, A, B):
        return np.add(A, B)
    
    def matrix_subtract(self, A, B):
        return np.subtract(A, B)
    
    def matrix_multiply(self, A, B):
        return np.dot(A, B)
    
    def matrix_determinant(self, A):
        return np.linalg.det(A)
    
    def matrix_inverse(self, A):
        try:
            return np.linalg.inv(A)
        except np.linalg.LinAlgError:
            return "Error: Singular matrix"
    
    # Unit Conversions (example: length)
    def convert_units(self, value, from_unit, to_unit):
        conversion_factors = {
            'meters_to_feet': 3.28084,
            'feet_to_meters': 0.3048,
            'kg_to_pounds': 2.20462,
            'pounds_to_kg': 0.453592
        }
        key = f'{from_unit}_to_{to_unit}'
        if key in conversion_factors:
            return value * conversion_factors[key]
        else:
            return "Error: Conversion not supported"
    
    # Constants
    def pi(self):
        return math.pi
    
    def e(self):
        return math.e


# Example usage
calc = ScientificCalculator()

# Basic operations
print(calc.add(5, 3))
print(calc.subtract(10, 4))
print(calc.multiply(7, 6))
print(calc.divide(8, 2))

# Advanced functions
print(calc.power(2, 3))
print(calc.sqrt(16))
print(calc.cbrt(27))

# Trigonometric functions
print(calc.sin(30))
print(calc.cos(60))
print(calc.tan(45))

# Hyperbolic functions
print(calc.sinh(1))
print(calc.cosh(1))
print(calc.tanh(1))

# Logarithmic functions
print(calc.ln(10))
print(calc.log10(100))
print(calc.log2(8))
print(calc.exp(1))

# Statistical functions
data = [1, 2, 3, 4, 5]
print(calc.mean(data))
print(calc.stddev(data))
print(calc.variance(data))

# Linear regression
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
print(calc.linear_regression(x, y))

# Fractional and integer functions
print(calc.factorial(5))
print(calc.nCr(5, 2))
print(calc.nPr(5, 2))

# Memory functions
calc.memory_store(10)
print(calc.memory_recall())
calc.memory_add(5)
print(calc.memory_recall())
calc.memory_subtract(2)
print(calc.memory_recall())
calc.memory_clear()
print(calc.memory_recall())

# Equation solving
print(calc.solve_linear(2, -4))
print(calc.solve_quadratic(1, -3, 2))

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(calc.matrix_add(A, B))
print(calc.matrix_subtract(A, B))
print(calc.matrix_multiply(A, B))
print(calc.matrix_determinant(A))
print(calc.matrix_inverse(A))

# Unit conversions
print(calc.convert_units(1, 'meters', 'feet'))
print(calc.convert_units(100, 'kg', 'pounds'))

# Constants
print(calc.pi())
print(calc.e())


#How to Use the Calculator
#You can use the provided methods for different operations. For example:
#	Basic Arithmetic: calc.add(5, 3) returns 8.
#	Advanced Functions: calc.power(2, 3) returns 8.
#	Statistical Functions: calc.mean([1, 2, 3]) returns 2.
# The calculator supports a wide range of mathematical, statistical, and unit conversion operations. Each method is documented with examples of how to use it, making the code easy to understand and extend if necessary.

