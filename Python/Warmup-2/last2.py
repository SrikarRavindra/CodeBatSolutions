def last2(x):
    x_end = x[len(x)-2:len(x)]
    count = 0
    for i in range(len(x)-2):
        str = x[i:i+2]
        if(str == x_end):
            count += 1
    return count
