"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""

import math as m

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(m.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

limit = 10001

ctr, num = 0, 1
while ctr < limit:
    num += 1
    if isPrime(num):
        ctr += 1
print(num)

# OUTPUT - 104743

