def run_length_encode(s):
    if not s:
        return ""
    count = 1
    prev =s[0]
    result =[]
    for ch in s[1:]:
        if ch == prev:
            count+=1
        else:
            result.append(prev+(str(count) if count>1 else ""))
            prev =ch
            count= 1
    result.append(prev+(str(count) if count>1 else ""))
    return "".join(result)

print(run_length_encode("aabbbbeeeeffggg")) 
print(run_length_encode("abbccccc"))