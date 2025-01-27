import random

number = random.randint(0,10)

guess = int(input("I'm thinking about a number 0~10 , Enter an integer : "))

while True:
    if guess == number:
        print('Congratulations, you guessed it.')
        break
    else:
        guess = int(input("Nope, try again : "))
print('Done, number is :', number)