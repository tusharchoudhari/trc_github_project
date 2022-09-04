#write a program which accepts a string from console and print the characters that have even indexes.
str=input("Enter string:")
extracted_str=""
i=0
while(i<=len(str)):
    if(i%2==0):
        extracted_str=extracted_str+str[i]
        i+=1
    else:
        i+=1
        continue
print("The final extracted string is:{}".format(extracted_str))

