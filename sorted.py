# check if a list is sorted

def isSorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False

        i = i + 1

    return True
