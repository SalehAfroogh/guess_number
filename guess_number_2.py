import random

# Get input numbers from the user
print("Welcome to the Guess the Number game!")
lower_bound = int(input("Enter the lower bound for the random number: "))
upper_bound = int(input("Enter the upper bound for the random number: "))

# Validate the bounds
if lower_bound >= upper_bound:
    print("Invalid range. The lower bound must be less than the upper bound. Please restart the game.")
    exit()

# Generate a random number between the provided bounds
r = random.randint(lower_bound, upper_bound)
print(f"A random number has been generated between {lower_bound} and {upper_bound}. Try to guess it!")
print(r)

# Number of allowed guesses
guess_count = 5

while guess_count > 0:
    try:
        # Prompt the user to input their guess
        new_guess_str = input(f"Remaining guesses: {guess_count} => Enter your next guess:\n")
        new_guess = int(new_guess_str)  # Convert the input to an integer

        # Check if the guess is correct, too high, or too low
        if r == new_guess:
            print("Great! Your guess is correct!")
            break  # Exit the loop if the guess is correct
        elif r > new_guess:
            print("Your guess is lower than the selected number")
        else:
            print("Your guess is higher than the selected number")
        
        # Decrement the guess count
        guess_count -= 1

    except ValueError:
        # Handle non-integer input
        print("Please enter a valid number")

# If all guesses are used and the number is not guessed
if guess_count == 0:
    print(f"Sorry, you've used all your guesses. The correct number was {r}.")
