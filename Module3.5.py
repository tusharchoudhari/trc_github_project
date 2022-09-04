#Bank System
balance=100
def showBalance(bal):
    print("Updated balance is:",bal)
while True:
    banking_option = input("Enter Input:")
    if(banking_option==""):
        break
    banking_option = banking_option.split(" ")
    banking_option_0 = banking_option[0]
    banking_option1 = banking_option[1]
    if(banking_option==""):
        break
    if(banking_option_0=="CASH_WITHDRAW"):
        balance=balance-int(banking_option1)
        showBalance(balance)
    elif(banking_option_0=="CASH_CREDIT"):
        balance=balance+int(banking_option1)
        showBalance(balance)
    elif(banking_option_0=="CHANGE_PASSWORD"):
        pass_dict={'pass':'','new_pass':'','confim_pass':''}
        new_pass = banking_option1
        pass_dict['new_pass'] = new_pass
        confim_pass = input("Confirm new password:")
        pass_dict['confirm_pass'] = confim_pass
        if (pass_dict["new_pass"] == pass_dict['confirm_pass']):
            passwd = new_pass
            pass_dict['pass'] = passwd
            print("Password changed successfully")
        else:
            print("new and confirmed password not matching")
    else:
        print("Invali Choice")

#passwd=input("Enter current password:")
