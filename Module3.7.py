num=int(input("Enter number to find factorial:"))
def fact(num):
    if(num==0):
        return 1
    elif(num==1):
        return 1
    else:
      return num*fact(num-1)
print("Factorial=",fact(num))