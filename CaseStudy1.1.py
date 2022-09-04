# This is a program which will find factors of given number and find whether the factor is even or odd
# num is variable holds the input number
# factors list holds the factor of num
# dict_even_odd dictionary holds the odd/even classification of factors for num

num=10
factors=[]
dict_even_odd={}
i=0
for n in range(1, num+1):
    if(num%n==0):
        factors.append(n)
        if(factors[i]%2==0):
            dict_even_odd[factors[i]]="Even"
            i=i+1
        else:
            dict_even_odd[factors[i]] = "odd"
            i = i + 1
print("Factors of {} are :{}".format(num,factors))
print("Even/Odd factor classification of {} is : {}".format(num,dict_even_odd))