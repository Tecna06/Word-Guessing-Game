# Word guessing game

# The word to guess
target_word = "python"

# Number of attempts allowed
guess_limit = 5

# List to store correctly guessed letters
correct_guesses = []

print(">>> Welcome to the Word Guessing Game! <<<")
print(f"The word has {len(target_word)} letters. Try to guess it.")
print("Enter one letter at a time. You have", guess_limit, "chances.")

# Loop: until the user runs out of guesses
while guess_limit > 0:
    guess = input("Guess a letter: ").lower()

    # Condition: input must be one alphabet character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the guessed letter is in the word
    if guess in target_word:
        if guess not in correct_guesses:
            correct_guesses.append(guess)
            print("Correct guess!")
        else:
            print("You've already guessed that letter.")
    else:
        guess_limit -= 1
        print("Wrong guess! Remaining chances:", guess_limit)

    # Show the current word status
    current_display = ""
    for letter in target_word:
        if letter in correct_guesses:
            current_display += letter + " "
        else:
            current_display += "_ "
    print("Word:", current_display.strip())

    # Check if all letters have been guessed
    if all(letter in correct_guesses for letter in target_word):
        print("\nCongratulations! You guessed the word:", target_word)
        break
else:
    print("\nGame over! The correct word was:", target_word)
