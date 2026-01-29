import math

def calculate_circle_area(radius):
    
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

def factorial(n):
    
    if n == 0:
        return 1
    return n * factorial(n - 1)