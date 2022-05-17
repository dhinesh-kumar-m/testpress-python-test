#12

def generete_feb(value):
    x=0
    y=1
    while x < value:
        print(x)
        x,y = y,x+y
        

generete_feb(10)
    