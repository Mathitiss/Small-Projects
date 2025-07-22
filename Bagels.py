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

difficult = int(input('---> '))
difs = {1: 100_000, 2: 100, 3: 50, 4: 25, 5: 10, 6: 3, 7: 1}
if difficult == 1:
    print('You have UNLIMITED guesses to get it.')
else:
    print(f'You have {difs[difficult]} guesses to get it.')
