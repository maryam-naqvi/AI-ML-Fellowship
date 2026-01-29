import math

def calculate_area():
    """Calculates the area of a circle based on user input."""
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative.")
        else:
            area = math.pi * (radius ** 2)
            print(f"The area of the circle is: {round(area, 2)}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    calculate_area()