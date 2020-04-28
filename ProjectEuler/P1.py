#  Find the sum of all the multiples of 3 or 5 below 1000.
num = 1000
temp = (num-1)//3
sumof3 = 3*(temp*(temp+1))//2

temp = (num-1)//5
sumof5 = 5*(temp*(temp+1))//2

temp = (num-1)//15
sumof15 = 15*(temp*(temp+1))//2

print(sumof3+sumof5-sumof15)

# OUTPUT - 233168
