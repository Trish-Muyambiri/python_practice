# given a value, return the sum of all natural numbers from the number to 1

def sum(n):
    sum = 0

    for i in range(n+1):
        sum += i

    return sum
