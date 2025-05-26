charcher = "absabfrgeuadnz45A"
val = ["a" ,"b" , "f", "n"]

# dic = {}

# for c in charcher:
#     dic[c] = dic.get(c,0) + 1


# for v in val:
#     print(dic.get(v))



hashlist = [0] * 128

for ch in charcher:
    ascvalue = ord(ch)

    index = ascvalue

    hashlist[index] += 1

for v in val:
     asc = ord(v)
     index = asc 

     print(hashlist[index])
    
