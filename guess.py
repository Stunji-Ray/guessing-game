import random
num=random.randint(0,100)
guesses=0
print("Hi,what's your name?")
name=input()
print ('Hi '+name+'!')
while True:
    print('Guess a number between 0 and 100.')
    guess=input()
    guess=int(guess)
    guesses+=1
    if guess>num:
        print('Too high')
    if guess<num:
        print('Too low')
    if guess==num:
        print('Correct!!! You got it in '+str(guesses)+' guesses!')
        break
