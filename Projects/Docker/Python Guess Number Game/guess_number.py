import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    lower_bound = int(input("Enter the minimum number: "))
    upper_bound = int(input("Enter the maximum number: "))

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()