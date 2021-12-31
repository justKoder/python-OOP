import random

num = random.randint(10, 100)

print("Guess a number between 10 and 100")
print('You get 3 guesses to guess the number')


def guessingGame(num):
    game_loop = True
    while game_loop:
        for i in range(3):
            guess = int(input("Enter your guess: "))
            i += 1
            if guess == num:
                print("You guessed it right YAY!!!!!")
                break
            elif guess < num:
                print("Your guess is too low!")
            elif guess > num:
                print("Your guess is too high!")
            else:
                print("Your number of guesses is over")
        game_loop = False


guessingGame(num)
