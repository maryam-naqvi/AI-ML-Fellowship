import time

def execution_time(func):
    """
    A decorator that measures how long a function takes to run.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start timer
        result = func(*args, **kwargs) 
        end_time = time.time()    # End timer
        
        print(f"Execution time for '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper


@execution_time
def complex_calculation():
    print("Running a heavy task...")
    time.sleep(1.5)
    print("Task complete.")

if __name__ == "__main__":
    complex_calculation()