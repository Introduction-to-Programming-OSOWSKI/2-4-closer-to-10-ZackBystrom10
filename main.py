from re import X


def close10(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return 0
print(close10(4,2))