import random

words = ["python", "java", "computer", "program", "coding"]


word = random.choice(words)

hidden_word = ["_"] * len(word)

guessed_letters = []

# Store wrong letters
wrong_letters = []

# Count incorrect guesses
wrong_guesses = 0

print(" Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < 6:

    print("\nWord:", " ".join(hidden_word))
    print("Wrong letters:", " ".join(wrong_letters))
    print("Wrong guesses:", wrong_guesses, "/ 6")

    guess = input("Guess a letter: ").lower()

    # Check whether input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        print("Wrong guess!")

        # Add wrong letter to the list
        wrong_letters.append(guess)

        # Increase wrong guess count
        wrong_guesses += 1

    # Check if the player guessed the complete word
    if "_" not in hidden_word:
        print("\nWord:", " ".join(hidden_word))
        print(" Congratulations! You won!")
        break

else:
    print("\nGame Over!")
    print("The word was:", word)

print("Thanks for playing! ")
print("\nkeep participating in the game ")

