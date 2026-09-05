import random

test_words = [
    'that',
    'fair',
    'bark',
    'blue',
    'body',
    'make',
    'fate',
    'bone',
    'book',
    'mark',
]


def get_random_word():
    random_word = random.choice(test_words)
    print(f'\nRandom word is {random_word}')
    return random_word


def is_valid_input(user_input: str, random_word: str):
    if any(char.isdigit() for char in user_input):
        print('\nYour answer can only contain letters')
        return False

    if len(user_input) != len(random_word):
        print(f'\nYou must enter a word that is {len(random_word)} characters long')
        return False

    return True


def get_new_clue(user_input: str, random_word: str):
    new_clue: list[str] = []

    for i, letter in enumerate(user_input):
        if letter == random_word[i]:
            new_clue.append(letter)
        else:
            new_clue.append('_')

    return new_clue


def is_correct_word(user_input: str, random_word: str):
    return user_input.upper() == random_word.upper()


def start_game():
    game_running = True
    random_word = get_random_word()

    while game_running:
        user_input = input('\nType your word: ')

        if not is_valid_input(user_input, random_word):
            continue

        if is_correct_word(user_input, random_word):
            print('\nYour guess is correct!')
            game_running = False
        else:
            print(f'\n11Current guess is {get_new_clue(user_input, random_word)}')