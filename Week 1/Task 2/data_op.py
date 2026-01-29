def process_data():
    raw_data = [10, 20, 10, 5, 40, 5, 30, 20]
    
    print(f"Raw Data: {raw_data}")

    #  Remove duplicates using a Set
    unique_data = list(set(raw_data))
    print(f"Unique Data: {unique_data}")

    # Find Min, Max, Sum
    print(f"Max: {max(unique_data)}")
    print(f"Min: {min(unique_data)}")
    print(f"Sum: {sum(unique_data)}")

    # List Comprehension: Square all numbers
    squared = [x**2 for x in unique_data]
    print(f"Squared Data: {squared}")

if __name__ == "__main__":
    process_data()