#8
play = True
#rule
rule = {"rock":"scissor","scissor":"paper","paper":"rock"}

while play:
    p1 = input("Player 1 Choose (rock/paper/scissor) ")
    p2 = input("Player 2 Choose (rock/paper/scissor) ")
    
    if p1 == p2:
        print("Draw!!!")
    elif rule[p1] == p2:
        print(f'{rule[p1]} beats {rule[p2]} Player 1 won!')
    else :
        print(f'{rule[p2]} beats {rule[p1]} Player 2 won!')
    
    p = input("press y to continue :")
    if p != 'y':
        play = False
    