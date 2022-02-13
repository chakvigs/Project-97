#Import a random module into your file.
#Use random to generate a random number from 1-9.
#Give users 5 chances to guess the number.
#If the user guesses incorrectly, show a hint or message to the user if their guess was close or far.
#If the user guesses correctly show the congratulating message.
#Show the “you lose” msg and the number.
#Hints - Use the while loop to count the chances of the player
#Show the “You Win” msg when the player guesses correctly and end the program using break.

import random
print('Number Guessing Game')
guesses = 0
randomInt = random.randint(1,9)
if(guesses == 5):
        print('You have no more guesses left! Try again!')
while guesses < 5:
    user = int(input('Guess a number between 1 and 9:'))
    if (user == randomInt):
        print('Your guess is correct!')
        break
    
    elif(user < randomInt):
        print('Your guess is too low. Guess a number higher than ', user)
    else:
        print('Your guess is too high. Guess a number lower than ', user)
    guesses+=1
    
if(not guesses < 5):
    print('The number is ', randomInt)