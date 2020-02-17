import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']
WORDS = [
    'spiderman',
    'link',
    'dante',
    'kratos',
    'nathan',
    'lara',
    'Elli',
    'snake',
    'computer',
]

def random_word():
    index = random.randint(0, len(IMAGES)-1)
    return WORDS[index]

def display_board(hidde_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidde_word)
    print('♦♦♦♦♦♦♦ ☼ ♦♦♦♦♦♦♦ ☼ ♦♦♦♦♦♦♦ ☼ ♦♦♦♦♦♦♦ ')


def run():
    word = random_word()
    hidde_word = ['=']*len(word)
    tries=0

    while True:
        display_board(hidde_word, tries)
        current_letter= str(input('Choose a letter: '))

if __name__ == '__main__':
    print('-------------------------------')
    print('         W E L C O M E         ')
    print('-------------------------------')
    run()