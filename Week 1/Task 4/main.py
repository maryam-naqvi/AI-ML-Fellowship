
from modules import math_utils
from mypackage import transformer

def run():
    print("--- Modular Programming Test ---")
    
    # Using the math module
    area = math_utils.calculate_circle_area(5)
    print(f"Area of circle (r=5): {area:.2f}")

    # Using the custom package
    text = "hello AI fellowship"
    reversed_text = transformer.reverse_string(text)
    capped_text = transformer.capitalize_string(text)
    
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")
    print(f"Capitalized: {capped_text}")

if __name__ == "__main__":
    run()