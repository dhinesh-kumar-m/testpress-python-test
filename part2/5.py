def find_number(list,number):
    
    if number in list:
        print(f'{number} is in list')
    else:
        print(f'{number} is not in list')

list = list(input("enter the list :"))
number = int(input("enter the number :"))
find_number(list,number)