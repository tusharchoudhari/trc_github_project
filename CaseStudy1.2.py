# This is a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# words is variable holds the input strings
# list_srt list holds the sorted words

words=str(input("Enter the sequence of words:"))
print(words)
list_srt=sorted(words.split(' '))
print("The sorted words are:{}".format(list_srt))