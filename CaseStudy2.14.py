n=5
list=[]
sum=0
for num in range(1,n+2):
    list.append(num)
sum=0
i=0
while i<len(list)-1:
    sum=sum+(list[i]/list[i+1])
    i=i+1

print(sum)
