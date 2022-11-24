def separate(l):
    if l:
        odd = []
        even = []

        for item in l:
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)

        return odd, even


print(separate([1, 2, 3, 4, 5]))
