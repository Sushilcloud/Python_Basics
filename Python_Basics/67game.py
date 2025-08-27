# MODIFY NUMBER GUESSING GAME
winning_number=43
guess=1
number=int(input("Guess a number between 1 and 100:  "))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"You win!, and you guessed this number in {guess} times")
        game_over=True
        #WIN
    else:
            if number < winning_number:
                print("Too Low")
                guess += 1
                number= int(input("guess again:  "))
            # GUESS WRONG
            else:
                print("too high")
                guess += 1
            number= int(input("guess again:  "))


import random
while_number=random.randint(1,100)