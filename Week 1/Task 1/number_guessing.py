import random

def guessing_game():
    """A simple number guessing game."""
    target_number = random.randint(1, 10)
    attempts = 0
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guessing_game()