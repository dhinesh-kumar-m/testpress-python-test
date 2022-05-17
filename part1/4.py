#4

number = int(input("Enter the number :"))
l =[]
for i in range(1,number+1):
    if number % i ==0:
        l.append(i)
    
print(f"{l} is the divisors for {number}")