import random

while True:
    print("think of a number from 0 to 100")
    input('type done when you are ready:')
    guess = random.randint(0,100)
    print('is it ', guess, "?")
    user_input = input("type yes or no:")
    while user_input == 'no':
        guess = random.randint(0, 100)
        print('is it ', guess, "?")
        user_input = input("type yes or no:")
    if user_input == 'yes':
        playagain=input('do you want to play again type yes or no:')
        if playagain=='yes':
            continue
        else:
            break
