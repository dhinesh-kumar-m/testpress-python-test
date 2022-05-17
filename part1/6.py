# 6
string = input("Enter the string :")

reversed = string[::-1]
if string == reversed:
    print(f"{string} is PANLINDROM")
else:
    print(f"{string} is not PANLINDROM")