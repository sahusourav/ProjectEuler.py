"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(n):
    sum, temp = 0, n
    while n > 0:
        r = n % 10
        sum = (sum * 10) + r
        n //= 10
    return sum == temp


max, a = 0, 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        a = i * j
        if palindrome(a):
            if max < a:
                max = a
            break

print(max)

# OUTPUT - 906609
