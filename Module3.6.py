lower_bound=2000
upper_bound=3200
list=[str(num) for num in range(lower_bound,upper_bound+1) if num%7==0 and num%5!=0]
comm_sep_list=",".join(list)
print(comm_sep_list)