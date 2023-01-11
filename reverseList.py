# take a list as input and return the reverse


def reverse(elements):
    reversed_list = []
    i = len(elements)-1

    while i >= 0:
        reversed_list.append(elements[i])
        i -= 1

    return reversed_list


print(reverse([1, 2, 3, 4]))
