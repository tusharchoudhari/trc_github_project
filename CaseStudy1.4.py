# Program that accepts a sentence and calculate the number of letters and digits

str=input("Enter the string:")
letter_counter=0
digit_counter=0
for char in str:
    if (char.isnumeric()):
        digit_counter+=1
    elif(char.isalpha()):
        letter_counter+=1
    elif(char.isspace()):
        continue
    else:
        print("{} Char is of different category than letter/digits. Please investigate".format(char))

print("Letters:{} \nDigits:{}".format(letter_counter,digit_counter))
