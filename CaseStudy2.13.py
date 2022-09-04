import random

list=[num for num in range(1,1001) if num%5==0 or num%7==0]
print(random.sample(list,5))