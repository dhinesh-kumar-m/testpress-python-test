chance = 0
min=0
max=100
guess = None
play = True

while play:
    if min == max:
        print("You are cheating me!!!")
        break

    guess = round((min+max)/2)

    chance += 1
    
    print(f"I guess you have {guess}")
    clue = input("Reply : ")
    
    if clue == 'low':
        min = guess
        max = max
    elif clue == 'high':
        min = min
        max = guess
    else:
        play = False
else:
    print(f"I found it in {chance} chances")