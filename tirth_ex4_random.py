import random

r = random.randint(1, 10)
guesses_left = 3
print(r)
while guesses_left > 0:
    guess = int(input("enter your guess: "))
    if guess == r:
        print("You Won!")
        break
    else:
        guesses_left -= 1
        print("Guesses left: ", guesses_left)

if guesses_left == 0:
    print("You Lose!")
