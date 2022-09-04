#12.Write a program that accepts a sequence of whitespace separated words as input
#and prints the words after removing all duplicate words and sorting them
#alphanumerically.
input_str=input("Enter space separated string:")
print(" ".join(sorted(set(input_str.split(" ")))))
