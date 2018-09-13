def missing_number(x):
    y=[]
    for i in range(1,10):
        if i not in x:
            y.append(i)
    return y
print(missing_number([1,3,6,7,8,9]))            