#5

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

new_list = [x for x in a if x in b ]
new_list = set(new_list)
print(list(new_list))