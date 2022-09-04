#10.Write a program that accepts a comma separated sequence of words as input and
#prints the words in a comma-separated sequence after sorting them alphabetically.
input_str=input("Enter comma separated string:")
print(",".join(sorted(input_str.split(","))))

