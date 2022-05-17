posibble = {"strong":set("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()"),
            "week":set("abcdefghijklmnopqrstuvwxyz"),
            "number":set("1234567890")
            }

def get_password(n,level):
    password = ""
    for _ in range(1,n+1):
        password += posibble[level].pop()
    return password
    
num = int(input("Enter the Password Length :"))
print(get_password(num,'strong'))
