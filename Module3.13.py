#13.Write a program which accepts a sequence of comma separated 4 digit binary
#numbers as its input and then check whether they are divisible by 5 or not. The
#numbers that are divisible by 5 are to be printed in a comma separated sequence.
input_num=input("Enter sequence of comma separated 4 digit binary numbers:")
list=input_num.split(",")
result_list=[num for num in list if int(num)%5==0]
print(",".join(result_list))
