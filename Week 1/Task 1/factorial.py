def calculate_factorial():
    """Calculates factorial using a loop."""
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial does not exist for negative numbers.")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i
            print(f"The factorial of {num} is: {factorial}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    calculate_factorial()