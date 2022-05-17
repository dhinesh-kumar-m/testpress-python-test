#10

number = int(input("Enter the number :"))

for i in range(2,number+1):
    if number % i == 0 and number != i:
        print(f"{number} is Prime")
        break
else:
    print(f"{number} is not a Prime")
    