import random

def number_guessing_game():
    """A simple number guessing game where the user guesses a random number between 1 and 100."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                return
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print(f"\n😔 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")

if __name__ == "__main__":
    number_guessing_game()