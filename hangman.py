import random
import sys

def prompt_to_play_again():
    while True:
        option = input('Do you want to play again (Y/N)? ')
        if option == 'Y' or option == 'y':
            play_game()
            break
        elif option == 'N' or option == 'n':
            sys.exit()
            break
        else:
            print('Invalid answer; please enter \'Y\' or \'N\'')
            continue

def play_game():
# Generate a random word
    wordlist = 'Hangman.txt'
    rand_words = []
    with open(wordlist, 'r') as f:
        for word in f:
            word = word.strip().lower()
            rand_words.append(word)
            
    word = random.choice(rand_words)
    word_as_list = list(word)

    guessed_letters = []
    attempts = 0
    encrypted_word = []
    for i in word:
        encrypted_word.append('*')

    attempts_left = 5
    while attempts_left > 0:
        enc_word_as_string = ''.join(encrypted_word)
        print(str(enc_word_as_string))

        if attempts_left == 1:
            print('You have 1 guess left.')
        else:
            print('You have %i guesses left.' % attempts_left)    
        
        guess = input('Guess a letter: ').lower()

        if not guess.isalpha():
            print('Invalid guess: Input is not a letter; please try again')
            continue
        elif len(guess) > 1:
            print('Invalid guess: Your guess must only be one character')
            continue
        elif guess == '':
            print('Invalid guess: Please enter something')
            continue
        
        if guess in guessed_letters:
            print('Invalid guess: You already guessed this letter; try again')
            continue
        else:
            if guess not in word:
                print('Incorrect guess; please try again')
                guessed_letters.append(guess)
                attempts_left = attempts_left - 1
                continue
            else:
                print('Good guess!')
                for i in range(0, len(word)):
                    if word[i] == guess:
                        encrypted_word[i] = guess
                guessed_letters.append(guess)
                if encrypted_word == word_as_list:
                    print(word)
                    print('You win!')
                    break

    if attempts_left == 0:
        print('You lose! The correct word is %s.' % word)

    prompt_to_play_again()

play_game()
