# Program to find factorial of number
num=5
fact=1
for n in range(1,num):
    fact=fact*n
print("Using For Factorial of {} = {}".format(num,fact))
fact=1
while n>1:
    fact=fact*n
    n=n-1
print("Using while Factorial of {} = {}".format(num,fact))