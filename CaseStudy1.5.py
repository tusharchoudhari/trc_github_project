#Program which will find the given number is Palindrome number or not.

num=input("Enter the number:")
print("Reversed num is {}".format(num[::-1]))
if(num==num[::-1]):
    print("{} is Palindrome".format(num))
else :
    print("{} is not Palindrome".format(num))