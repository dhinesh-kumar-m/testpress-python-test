def name_count():
    try:
        f = open('names.txt','r',encoding='utf-8')
        name = f.read().split("\n")
        dic = {i:name.count(i) for i in name}   #
        # return len(name) 
        return dic # 
    except:
        raise Exception("Something went wrong")
    finally:
        f.close()

print(f'Total no. of names : {name_count()}')