from random import randint

playAgain = 'yes'

while playAgain == 'yes':

    comp = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))

    print('Welcome to Bulls and Cows!')

    user = input('Enter your 4-digit guess: (i.e. 1234) ')

    bulls = 0

    while bulls < 4:

        bulls = 0
        cows = 0

        while len(user) != 4:
            user = input('You must enter a 4-digit number: ')
        
        if id(comp[0]) == id(user[0]):
            bulls = bulls + 1
        elif id(comp[0]) == id(user[1]):
            cows = cows + 1
        elif id(comp[0]) == id(user[2]):
            cows = cows + 1
        elif id(comp[0]) == id(user[3]):
            cows = cows + 1
        else:
            cows = cows + 0

        if id(comp[1]) == id(user[1]):
            bulls = bulls + 1
        elif id(comp[1]) == id(user[0]):
            cows = cows + 1
        elif id(comp[1]) == id(user[2]):
            cows = cows + 1
        elif id(comp[1]) == id(user[3]):
            cows = cows + 1
        else:
            cows = cows + 0

        if id(comp[2]) == id(user[2]):
            bulls = bulls + 1
        elif id(comp[2]) == id(user[1]):
            cows = cows + 1
        elif id(comp[2]) == id(user[0]):
            cows = cows + 1
        elif id(comp[2]) == id(user[3]):
            cows = cows + 1
        else:
            cows = cows + 0

        if id(comp[3]) == id(user[3]):
            bulls = bulls + 1
        elif id(comp[3]) == id(user[1]):
            cows = cows + 1
        elif id(comp[3]) == id(user[2]):
            cows = cows + 1
        elif id(comp[3]) == id(user[0]):
            cows = cows + 1
        else:
            cows = cows + 0

        print('Bulls: ' + str(bulls) + ' Cows: ' + str(cows))

        if bulls != 4:    
            user = input('Enter another guess: ')
        

    print('You win!')
    playAgain = input('Play again? (yes/no) ')
    while playAgain != 'yes' and playAgain !='no':
        playAgain = input('Please enter yes or no: ')

print('Goodbye :)')
        
