"""
A website requires a user to input username and password to register.
Write a program to check the validity of password given by user.
Following are the criteria for checking password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12
"""
passwd=input("Enter Password:")
passwd_len=len(passwd)
passwd_criteria_dict={'islower':'N','isupper':'N','isdigit':'N','$#@':'N'}   # criteria initiated with value  default value of N as not satisfied
if(passwd_len>=6 and passwd_len<=12):
    for char in passwd:
                if ('N' in passwd_criteria_dict.values()):   # The program should check each criteria only once
                    if(char.islower()):
                       passwd_criteria_dict['islower']='Y'   # set the value to 'Y' once the criteria is satisfied
                    elif(char.isupper()):
                        passwd_criteria_dict['isupper']='Y'
                    elif (char.isnumeric()):
                        passwd_criteria_dict['isdigit']='Y'
                    elif("$" in passwd or "#" in passwd or '@' in passwd):
                        passwd_criteria_dict['$#@']='Y'
                    elif(not (char.islower() or char.isupper() or char.isnumeric() or ("$" in passwd or "#" in passwd or '@' in passwd))):
                        print("{} Invalid character entered for password".format(char))
                        break
                    else:
                        continue
                else:
                    break
else:
    passwd_criteria_dict['len'] = 'N'
print("The password criteria satisfied/unsatisfied:{}".format(passwd_criteria_dict))
if('N' in passwd_criteria_dict.values()):     # if any of the criteria is not satisfied then invalid else valid
    print("{} password is invalid".format(passwd))
    print("The Password should satisfy following criteria:"
          "\n1. At least 1 letter between [a-z]"
          "\n2. At least 1 number between [0-9]"
          "\n 3. At least 1 letter between [A-Z]"
          "\n4. At least 1 character from [$#@]\n"
          "5.Minimum length of transaction password: 6"
          "\n6. Maximum length of transaction password: 12")
else:
    print("{} password is valid".format(passwd))