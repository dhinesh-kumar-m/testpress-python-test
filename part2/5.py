def find_number(list,number):
    
    if number in list:
        print(f'{number} is in list')
    else:
        print(f'{number} is not in list')

number = int(input("enter the number :"))
find_number([1,2,3,4],number)