def add(a,b):
    return a+b
    print("This will not execute")

a=10
b=20
items =[1,2,3,4]
square=list(map(lambda x:x*2,items))
print(square)
from functools import reduce
product=reduce(lambda x,y:x*y,items)
print("Reduce={}".format(product))
fib=reduce(lambda x,y:x+y,items)
print("fib={}".format(fib))
sum=(lambda a,b:a+b)
number_list=range(-5,5)
less_than_zero=list(filter(lambda x:x<0,number_list))
print(less_than_zero)
print("Sum={}".format(add(a,b)))
print("Sum={}".format(sum(a,b)))
