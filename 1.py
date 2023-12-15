def choose_word():
    # List of words to choose from
    words = ['apple', 'banana', 'orange', 'grape', 'watermelon', 'pineapple', 'strawberry', 'kiwi']
    # Randomly choose a word from the list
    import random
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with blanks for letters not guessed yet
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
        display += ' '
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed = []
    attempts = 6  # Number of attempts allowed

    while attempts > 0:
        print("\n" + display_word(secret_word, guessed))
        if '_' not in display_word(secret_word, guessed):
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess! You have", attempts, "attempts left.")

    if attempts == 0:
        print("\nSorry, you're out of attempts. The word was:", secret_word)

hangman()