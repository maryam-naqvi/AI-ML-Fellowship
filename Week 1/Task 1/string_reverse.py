def reverse_string():
    """Reverses a string provided by the user."""
    text = input("Enter a string to reverse: ")
    reversed_text = text[::-1]
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")

if __name__ == "__main__":
    reverse_string()