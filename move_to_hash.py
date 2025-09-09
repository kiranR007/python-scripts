def move_to_hash(s):
    count = 0
    res = []
    for ele in s:
        if ele == "#":
            count+=1
        else:
            res.append(ele)
    return "#"*count+"".join(res)
print(move_to_hash("abc##d#e#"))