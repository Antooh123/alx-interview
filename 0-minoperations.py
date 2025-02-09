#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
