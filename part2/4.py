random = "1036"
guesses = []
cow = 0
bull = 0

while True:
    num = input("Enter the 4 digit value :")
    
    guesses.append(num)

    if random == num:
        print(f"Total chances : {len(guesses)}")
        break

    for index_i,value_i in list(enumerate(num)):
        for index_j,value_j in list(enumerate(random)):
            if random[index_i] == num[index_j] and index_i == index_j :
                cow+=1
            elif num[index_j] == random[index_i]:
                bull+=1

    
    print(f"{cow} cows, {bull} bulls")
    cow = bull = 0

    
