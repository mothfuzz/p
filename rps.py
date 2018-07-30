from random import randint

cont = 'memes'
pscore = 0
cscore = 0

print('ROCK PAPER SCISSORS')
print('enter \'stop\' to end the game')

while cont == 'memes':

    player = input('rock, paper, or scissors? ')

    while player != 'rock' and player != 'paper' and player != 'scissors' and player != 'stop':
        player = input('you must enter a valid choice! ')

    if player == 'stop':
        cont = 'stop'

    num = randint(1,3)
    if num == 1:
        comp = 'rock'
    elif num == 2:
        comp = 'paper'
    else:
        comp = 'scissors'

    if player != 'stop':
        print(player, 'vs', comp)

    if player == 'rock':
        if comp == 'paper':
            print('computer wins!')
            cscore = cscore + 1
        elif comp == 'scissors':
            print('you win!')
            pscore = pscore + 1


    if player == 'paper':
        if comp == 'scissors':
            print('computer wins!')
            cscore = cscore + 1
        elif comp == 'rock':
            print('you win!')
            pscore = pscore + 1


    if player == 'scissors':
        if comp == 'rock':
            print('computer wins!')
            cscore = cscore + 1
        elif comp == 'paper':
            print('you win!')
            pscore = pscore + 1

    if player == comp:
        print('it\'s a draw!')
        
print('FINAL SCORES')
print('you:', pscore, 'computer:', cscore)
print('goodbye :)')
