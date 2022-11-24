def mean(lst):
    if lst:
        sum = 0
        for item in lst:
            sum += item

        average = sum / len(lst)

        return average


def average(lst):
    if lst:
        return sum(lst)/len(lst)
