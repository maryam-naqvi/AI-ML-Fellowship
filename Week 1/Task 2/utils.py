def log_message(message, level="INFO", **kwargs):
   
    print(f"[{level}] {message}")
    if kwargs:
        print(f"   Details: {kwargs}")

def calculate_stats(*args):
    
    if not args:
        return 0, 0
    total = sum(args)
    average = total / len(args)
    return total, average