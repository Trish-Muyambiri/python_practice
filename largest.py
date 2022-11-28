# returns the largest value in a list

def largest(l):
    if l:
        max = l[0]

        for i in range(1, len(l)):
            if l[i] > max:
                max = l[i]

        return max

    else:
        return None
