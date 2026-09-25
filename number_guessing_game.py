import random

def play_game():
    print("=" * 40)
    print("   WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 40)

    # Difficulty settings: (range, attempts)
    levels = {
        "1": (10, 4),
        "2": (50, 6),
        "3": (100, 8),
    }

    print("\nChoose a difficulty:")
    print("1. Easy   (1-10,  4 attempts)")
    print("2. Medium (1-50,  6 attempts)")
    print("3. Hard   (1-100, 8 attempts)")

    choice = input("Enter 1, 2, or 3: ").strip()
    max_num, max_attempts = levels.get(choice, levels["2"])

    secret_number = random.randint(1, max_num)
    attempts_left = max_attempts

    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_left > 0:
        guess_input = input(f"Attempts left: {attempts_left}. Your guess: ").strip()

        if not guess_input.isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)
        attempts_left -= 1

        if guess == secret_number:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {max_attempts - attempts_left} attempt(s).")
            break
        elif guess < secret_number:
            print("Too low!\n")
        else:
            print("Too high!\n")

        if attempts_left == 0:
            print(f"\n💥 Out of attempts! The number was {secret_number}.")

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing! Goodbye.")


if __name__ == "__main__":
    play_game()
