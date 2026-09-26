import random

# ASCII art representing the hangman stages
HANGMAN_STAGES = [
    """
       +-------+
       |       |
       |       |
       |       |
       |       |
       |       |
    -----------------
    """,
    """
       +-------+
       |       |
       |       |
       |       |
       |       |
       |       |
       (       )
    -----------------
    """,
    """
       +-------+
       |       |
       |       |
       |       |
       |       |
       |       |
       (       )
       |       |
    -----------------
    """,
    """
       +-------+
       |       |
       |       |
       |       |
       |       |
       |       |
       (       )
       |       |
       |       |
    -----------------
    """,
    """
       +-------+
       |       |
       |       |
       |       |
       |       |
       |       |
       (       )
       |       |
       |       |
       |       |
    -----------------
    """,
    """
       +-------+
       |       |
       |
       |       |
       |       |
       |       |
       (       )
       |       |
       |       |
       |       |
       |       |
    -----------------
    """,
    """
       +-------+
       |       |
       |       |
       |       |
       |       |
       |       |
       (       )
       |       |
       |       |
       |       |
       |       |
       |       |
    -----------------
    """
]

# A list of words to play with
WORDS = [
    "python", "programming", "developer", "algorithm", "software",
    "engineer", "intelligence", "computer", "coding", "variable",
    "function", "interface", "database", "network", "protocol",
    "encryption", "cybersecurity", "automation", "architecture", "logic"
]

def display_game_state(word, guessed_letters, mistakes):
    """Displays the current state of the game."""
    print(HANGMAN_STAGES[mistakes])

    # Display the word with underscores for unguessed letters
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"Word: {display_word}")

    # Display guessed letters
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Mistakes: {mistakes}/6")
    print("-" * 20)

def play_hangman():
    """Main game loop."""
    word = random.choice(WORDS).lower()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(HANGMAN_STAGES) - 1

    print("Welcome to Hangman!")
    print("Try to guess the hidden word before the man is hanged.")

    while mistakes < max_mistakes:
        # Create a template for display
        guessed_template = guessed_letters

        display_game_state(word, guessed_letters, mistakes)

        # Check if the user has won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word!")
            print(f"The word was: {word.upper()}")
            return

        # Get user input
        guess = input("Guess a letter: ").strip().lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("\n[!] Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"\n[!] You've already guessed '{guess}'. Try again.")
            continue

        # Process the guess
        guessed_letters.add(guess)

        if guess in word:
            print(f"\n[+] Good job! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"\n[-] Sorry, '{guess}' is not in the word.")

    # If the loop ends, the user has lost
    print(HANGMAN_STAGES[mistakes])
    print("\nGAME OVER")
    print(f"The man has been hanged. The word was: {word.upper()}")

if __name__ == "__main__":
    play_hangman()
