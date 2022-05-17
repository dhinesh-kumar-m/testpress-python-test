chance = 0
min=0
max=100
guess = None

while True:
    guess = round((min+max)/2)
    print(f"I guess you have {guess}")
    clue = input("Reply : ")
    
    if clue == 'low':
        min = guess
        max = max
    elif clue == 'high':
        min = min
        max = guess
    else:
        break
    chance += 1
        
print(f"I found it in {chance} chances")