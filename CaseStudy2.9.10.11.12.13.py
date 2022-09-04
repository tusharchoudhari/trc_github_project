list=[12,24,35,24,88,120,155,88,120,155]
uniq_list=[]
print(list)
for num in list :
    if num not in uniq_list:
        uniq_list.append(num)
print(uniq_list)

list_removed_24=[ num for num in list if num!=24]
print(list_removed_24)

list_removed_0th_4th_5th=[ list[i] for i in range(0,len(list)) if i not in(0,4,5)]
print(list_removed_0th_4th_5th)

list_removed_div_by_5_7=[num for num in list if num%5!=0 or num%7!=0]
print(list_removed_div_by_5_7)

import random

list_div_by_5_7=[num for num in range(1,1001) if num%5==0 or num%7==0]
print(random.sample(list_div_by_5_7,5))