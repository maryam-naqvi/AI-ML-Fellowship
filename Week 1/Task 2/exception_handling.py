from utils import log_message  # Importing from our own module!

def safe_calculator():
    print("--- Safe Calculator ---")
    print("Enter two numbers to divide.")
    
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        
        result = num1 / num2
        
    except ValueError:
        log_message("Invalid input! Please enter numeric values only.", level="ERROR")
    except ZeroDivisionError:
        log_message("Cannot divide by zero!", level="ERROR")
    else:
        # This runs only if NO exception occurs
        print(f"Result: {result}")
        log_message("Calculation successful", operation="division", value=result)
    finally:
        # This runs no matter what
        print("Calculation attempt finished.\n")

if __name__ == "__main__":
    safe_calculator()