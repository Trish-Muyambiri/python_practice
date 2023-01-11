# return the second largest VALUE
def getSecMax(l):
    if len(l) <= 1:
        return None

    largest = l[0]
    slargest = None
    for x in l[1:]:
        if x > largest:
            slargest = largest
            largest = x

        elif x != largest:
            if slargest == None or slargest < x:
                slargest = x

    return slargest
