# Fibonacci generator

again = 'yes'

while again == 'yes':
    num = int(input('How many Fibonacci numbers would you like? '))

    if num == 0:
        print('Then why are you even using this?')
    elif num == 1:
        fib = [1]
        print(fib)
    elif num != 1:
        fib = [1,1]
        for x in range(num-2):
            fib.append( fib[-2] + fib[-1] )
        print(fib)

    again = input('Again? yes/no ')
    while again != 'yes' and again != 'no':
        again = input('Yes or no? ')

print('Goodbye :)')
