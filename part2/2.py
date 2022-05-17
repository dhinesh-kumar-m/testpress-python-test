def reverse_string(string):
    string = string.split(' ')
    return ' '.join(string[::-1])

string = input("Enter the string :")
print(reverse_string(string))
