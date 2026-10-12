# Number Guessing Game

A simple command-line number guessing game written in Python. Pick a difficulty, then try to find the secret number before you run out of attempts.

## How to play

1. Choose a difficulty level.
2. The computer picks a secret number in that range.
3. Enter your guesses. After each one you'll be told whether it was too low or too high.
4. Find the number before your attempts run out.

## Difficulty levels

| Level  | Number range | Attempts |
|--------|--------------|----------|
| Easy   | 1 - 10       | 4        |
| Medium | 1 - 50       | 6        |
| Hard   | 1 - 100      | 8        |

If you enter anything other than 1, 2 or 3, the game defaults to Medium.

## Requirements

- Python 3.6 or newer
- No external libraries (it only uses the built-in `random` module)

## Example

```
========================================
   WELCOME TO THE NUMBER GUESSING GAME
========================================

Choose a difficulty:
1. Easy   (1-10,  4 attempts)
2. Medium (1-50,  6 attempts)
3. Hard   (1-100, 8 attempts)
Enter 1, 2, or 3: 1

I'm thinking of a number between 1 and 10.
You have 4 attempts. Good luck!

Attempts left: 4. Your guess: 5
Too low!

Attempts left: 3. Your guess: 8
🎉 Correct! The number was 8.
You guessed it in 2 attempt(s).

Play again? (y/n): n
Thanks for playing! Goodbye.
```

## Features

- Three difficulty levels
- Input validation: invalid entries (letters, blanks, decimals) don't use up an attempt
- Play again option after each round

## Ideas for improvement

- Track a high score or best attempt count
- Add hints (for example, "within 5 of the number")
- Add a custom range or custom attempt count

## License

This project is open source. Add a license of your choice, such as MIT.
