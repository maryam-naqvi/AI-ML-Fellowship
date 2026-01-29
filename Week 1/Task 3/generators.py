def fibonacci_generator(n):
    
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def custom_range(start, end, step=1):
    
    current = start
    while current < end:
        yield current
        current += step

if __name__ == "__main__":
    print("--- Fibonacci Sequence (First 7) ---")
    for num in fibonacci_generator(7):
        print(num, end=" -> ")
    print("End")

    print("\n--- Custom Range (10 to 30, step 5) ---")
    for num in custom_range(10, 30, 5):
        print(num)