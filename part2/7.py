def name_count():
    try:
        f1 = open('prime.txt','r',encoding='utf-8')
        f2 = open('happy.txt','r',encoding='utf-8')
        prime = f1.read().split("\n")
        happy = f2.read().split("\n")

        return [x for x in prime if x in happy]
    except:
        raise Exception("Something went wrong")
    finally:
        f1.close()
        f2.close()

print(f'Total no. of names : {name_count()}')