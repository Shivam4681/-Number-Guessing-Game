import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it.")

    while True:
        guess = input("\nEnter your guess (or 'q' to quit): ")

        # Check if the user wants to quit
        if guess.lower() == 'q':
            print("Thanks for playing. Goodbye!")
            break

        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

# Run the game
guess_number()