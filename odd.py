# retur the ONLY value that appears an odd number of times
def findOdd(l):
    if l:
        odd = []

        for item in l:
            if item not in odd:
                odd.append(item)

            else:
                odd.remove(item)

        return odd[0]
