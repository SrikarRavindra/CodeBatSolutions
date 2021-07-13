def string_match(s1,s2):
    big_len = 0
    count = 0
    if(len(s1) > len(s2)):
        big_len = len(s1)
    else:
        big_len = len(s2)
    for i in range(big_len-1):
        a = s1[i:i+2]
        b = s2[i:i+2]
        if(a == b):
            count+=1
    return count
