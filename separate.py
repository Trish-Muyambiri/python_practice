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

# using list comprehensions


def odd_even(l):
    if l:
        odd = [item for item in l if item % 2 != 0]
        even = [item for item in l if item % 2 == 0]

    return odd, even
