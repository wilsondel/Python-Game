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
    'elli',
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
    hidde_word = ['°']*len(word)
    tries=0

    while True:
        display_board(hidde_word, tries)
        current_letter= str(input('Choose a letter: '))

        letter_index_user = []
        for idx in range(len(word)): #Recorre word mirando si alguno es igual a la letra del usuario
            if word[idx] == current_letter:
                letter_index_user.append(idx) 
            
        if len(letter_index_user)==0: #Codigo pregunta una vez y repite
            tries+=1
            if(tries==7):
                display_board(hidde_word, tries)
                print('')
                print('I am sorry, you fail :c')
                print(f'The correct word was {word}')
                break
        else:
            for idx in letter_index_user:
                hidde_word[idx]= current_letter # Realiza intercambio por letra del usurario
            
            letter_index_user = [] # Repite ciclo por eso se inicializa en cero
        try:
            hidde_word.index('°')
        except ValueError:
            print(f'Hey! you Win. Congratulations!! you guess {word}')
            break


if __name__ == '__main__':
    print('-------------------------------')
    print('         W E L C O M E         ')
    print('-------------------------------')
    run()