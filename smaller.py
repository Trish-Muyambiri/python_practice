# given a list and a value x, return a list of elements smaller than x in the list
def smaller(l, x):
    less = []
    if l:
        for item in l:
            if item < x:
                less.append(item)

    return less


print(smaller([1, 2, 3, 4, 5], 2))
