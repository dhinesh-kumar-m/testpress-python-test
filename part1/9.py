# 9 
import random

rand = random.Random().randint(1,10)

play = True

while True:
    guess = int(input("Guess the number : "))
    
    if guess < rand:
        print("too low")
    elif guess > rand:
        print("too high")
    else:
        print("You guesed it Right!!!")
        restart = input("press y to play again : ")
        if restart != "y":
            play = False
        


