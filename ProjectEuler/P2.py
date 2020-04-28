"""
Find the sum of all the even-valued terms in the Fibonacci sequence
which do not exceed four million.
"""
limit = 4000000

sum, a, b = 0, 1, 1
c = a+b

while c < limit:
    sum += c
    a = b+c
    b = c+a
    c = a+b

print(sum)

# OUTPUT - 4613732
