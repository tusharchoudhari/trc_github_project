#write a program which count and print the numbers of each character in a string input by console.
str=input("Enter string:")
dict={}
for char in str:
    if char in dict:
        dict[char]=dict[char]+1
    else:
        dict[char]=1
for key in dict:
  print("\n{},{}".format(key,dict[key]))