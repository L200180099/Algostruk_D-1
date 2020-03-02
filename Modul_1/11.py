def apakahKabisat(x):
    x = int(x)
    if x%100 == 0 and x%400 != 0:
        return False
    elif x%4 == 0 or x%400 == 0:
        return True
    else:
        return False
    
