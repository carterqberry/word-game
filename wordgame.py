#carter quesenberry wordgame.py
import sys
import random
from itertools import permutations


#for command line argument:
def choose_word(length_range, base_word=None):
    if base_word:
        return base_word
    else:
        pass


#function to choose a random word from 'words.txt' within the specified length range:
def choose_word(length_range):
    with open('words.txt', 'r') as file:
        words = [word.strip() for word in file.readlines() if len(word.strip()) in length_range]
    if not words:
        print(f"No words found for the specified length range {length_range}.")
        return None
    return random.choice(words)

#function to scramble the given word:
def scramble_word(word):
    return ''.join(random.sample(word, len(word)))


#function to generate possible words from the scrambled word:
def generate_possible_words(scrambled_word, length_range):
    possible_words = []
    for length in range(length_range[0], length_range[1] + 1):
        words_of_length = set()
        for permuted_letters in permutations(scrambled_word, length):
            possible_word = ''.join(permuted_letters)
            if possible_word in words_set:
                words_of_length.add(possible_word)
        if words_of_length:
            possible_words.append(words_of_length)
    return possible_words


#function to display possible words as hidden dashes:
def display_hidden_words(possible_words, guessed_words):
    for words_of_length in possible_words:
        if not words_of_length:
            continue  # skip the empty rows
        print("[", end="")
        for i, word in enumerate(words_of_length):
            if word in guessed_words:
                print(f"'{word}'", end="")
            else:
                print(f"'{'-' * len(word)}'", end="")

            if i < len(words_of_length) - 1:
                print(", ", end="")
        print("]")


def main(base_word=None):
    global words_set
    length_range_input = input("Enter the range of word lengths (low, high): ")
    low, high = map(int, length_range_input.split(','))

    length_range = (low, high)

    chosen_word = choose_word(length_range)

    if chosen_word:
        with open('words.txt', 'r') as file:
            words_set = set(word.strip() for word in file.readlines())

        possible_words = generate_possible_words(chosen_word, length_range)

        guessed_words = []

        while True:
            scrambled_word = scramble_word(chosen_word)
            print(scrambled_word, "\n")
            display_hidden_words(possible_words, guessed_words)

            guess = input("\nEnter a guess: ").strip().lower()

            if guess == 'q':
                break

            found = False
            for words_of_length in possible_words:
                if guess in words_of_length:
                    guessed_words.append(guess)
                    found = True

            if not found:
                print("Sorry. Try again\n")
            else:
                print("Correct!\n")

            all_words_guessed = all(not words_of_length for words_of_length in possible_words)
            if all_words_guessed:
                print("Congratulations! You've guessed all the words :)")
                break
        print(guessed_words)


if __name__ == "__main__":
    #check if a command-line argument is provided
    if len(sys.argv) > 1:
        #use the provided argument as the base word
        base_word_from_argument = sys.argv[1].lower()
        main(base_word_from_argument)
    else:
        main()

