import random

# Define the range
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Generate a random number
random_number = random.randint(a, b)
print(f"A random number between {a} and {b} has been generated.")
print(random_number)
# Total allowed guesses
total_attempts = 5

for attempt in range(total_attempts):
    # Prompt the user for input
    guess = int(input(f"Attempt {attempt + 1}/{total_attempts}: Guess the number: "))

    # Check if the guess is correct
    if guess == random_number:
        print("True! Your guess is correct!")
        break
    else:
        print("False! Try again.")

# If the loop completes without breaking, the user has lost
else:
    print(f"You've used all {total_attempts} attempts. You lose! The correct number was {random_number}.")
