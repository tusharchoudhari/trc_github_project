def binary_search(list,l,last_index,search):
    if(last_index>=0):
        mid=int(l+(last_index-1)/2)
    if(list[mid]==search):
        return mid
    elif(search<list[mid]):
        return binary_search(list,0,mid-1,search)
    elif(search>list[mid]):
        return binary_search(list, mid+1, last_index, search)
    else:
        return -1


#list=["A","B","C","X","Y","Z"]
list=[1,2,3,4,5,6,7,8]
print("Info for XYZ org",list)
search=int(input("Enter the value to search:"))
ans=binary_search(list,0,len(list)-1,search)
if ans!=-1:
    print("{} found at index {}".format(search,ans))
else :
    print("{} not found in {}".format(search,list))