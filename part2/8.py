g = input("Enter roe x column (e.g., 2x2): ").split('x')
row = int(g[0])
column = int(g[-1])

for i in range(row+1):
    print(" --- " * column)
    if i == row:
        break
    for j in range(column+1):
        print("|", end = '    ')
        
    print()
    