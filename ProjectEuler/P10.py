"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import math as m

num, sum = 2000000, 0
prime = [True for i in range(num + 1)]
for i in range(2,int(m.sqrt(num))):
    j=i
    while j*i <= num:
        prime[i*j] = False
        j += 1
for i in range(2, num+1):
    if prime[i]:
        sum += i
print(sum)

# OUTPUT- 142913828922
