#14.Write a program that accepts a sentence and calculate the number of upper case
#letters and lower case letters
input_str=input("Enter string:")
upper=0
lower=0
for char in input_str:
    if(char.isupper()):
        upper+=1
    elif(char.islower()):
         lower+=1
    elif(char.isspace()):
        continue
    else:
        print("Invalid char reported",char)
print("UPPER CASE={} \nLOWER CASE={}".format(upper,lower))