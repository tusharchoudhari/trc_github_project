# T program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number.
# The numbers obtained should be printed in a comma separated sequence on a single line.
lower_bound_num=1000
upper_bound_num=3000
list=[]
for num in range(lower_bound_num,upper_bound_num+1):
        num_orig=num
        while(num>=1):
             digit=int(num%10)
             #print("digit"+str(digit))
             if(digit%2==0):
                    num=int(num/10)
                    #print("updated num" + str(num))
                    flag='Pass'
             else:
                     flag='Fail'
                     break
        if(flag=='Pass'):
           list.append(num_orig)
if(len(list)>0):
    print("All the numbers between {} and {} (both included) such that each digit of a number is an even number:\n{}".format(lower_bound_num,upper_bound_num,list))
else:
    print("No number exists in the range {} to {} (both included) such that each digit of a number is an even number".format(lower_bound_num,upper_bound_num))

