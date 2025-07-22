import random
import re

print('''
    Bagels, a deductive logic game.

    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
    Pico           One digit is correct but in the wrong position.
    Fermi          One digit is correct and in the right position.
    Bagels         No digit is correct.
      
    I have thought up a number...''')

print('''
    Choose the dificult:
    Print - 1 (BEGINNER)
    Print - 2 (EASY)
    Print - 3 (NORMAL)
    Print - 4 (MEDIUM)
    Print - 5 (HARD)
    Print - 6 (IMPOSSIBLE)
    Print - 7 (GOD)
      ''')

class Game:
    diffs = {1: 100_000, 2: 100, 3: 50, 4: 25, 5: 10, 6: 3, 7: 1}

    def __init__(self, num):
        self.difficult = self.diffs[num]
        self.result = self.random_number()

        if self.difficult == '1':
            print('You have UNLIMITED guesses to get it.')
            print()
        else:
            print(f'You have {self.difficult} guesses to get it. Good luck!')
            print()

        self.play()

    def random_number(self):
        return str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    
    def check(self):
        flag = True

        while flag:
            word = input('Your guess --> ')

            if not re.match('\d{3}', word):
                print('''ERROR! Your number should consist of 3 digits. Examples: 123, 100, 023, 003, 000, etc.
    Try again!
                    ''')
            else:
                flag = False

        return word

    def play(self):
        if self.difficult != 1:
            while self.difficult:
                guess = self.check()

                if guess == self.result:
                    print('CORRECT! YOU WIN')
                    return
                else:
                    print('WRONG. TRY AGAIN')
                    print()

                self.difficult -= 1
        else:
            guess = self.check()

            if guess == self.result:
                print('CORRECT! YOU WIN')
                return

        print('YOU LOST! GAME OVER')
        return
    
def level():
    flag = True
        
    while flag:
        n = input('Choose difficulty ---> ')
    
        if n.isdigit() and int(n) in list(range(1, 8)):
            flag = False
        else:
            print('''ERROR! Difficulty level should be a digit in range 1 to 7.
Try again!
                    ''')
    return int(n)

l = level()
Game(l)