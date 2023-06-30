import random


randomNumber=random.randint(1,5)
# randomNumber=int(random.random()*6) #Another Way
for i in range(6):
    guessNumber=int(input('Enter your guess number between 1 to 5 : '))

    if(guessNumber==randomNumber):
        print('win')
        break
    else:
        print('Loss')