"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math as m

n= 600851475143
lastFactor, factor = 0, 0

if n % 2 == 0:
    lastFactor = 2
    n //= 2
    while n % 2 == 0:
        n //= 2
else:
    lastFactor=1

factor = 3
maxFactor = int(m.sqrt(n))

while n > 1 and factor <= maxFactor:
    if n % factor == 0:
        n //= factor
    lastFactor = factor
    while n % factor == 0:
        n //= factor
    maxFactor = int(m.sqrt(n))
    factor += 2

if n == 1:
    print(lastFactor)
else:
    print(n)

# OUTPUT - 6857
