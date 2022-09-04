#Build a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID with fingerprint
#Give the option for decryption to use
#refid="123456789012"
#refid="abcdefghij12"
refid=input("Enter the Reference ID:")
encryp_refid_list=[]
encryp_refid=""
valid='N'
is_decrypt='N'
len_refid=len(refid)
cnt1=0
if(len_refid==12 and refid.isalnum() and not refid.isnumeric() and not refid.isalpha()):
        while(cnt1<12):
            encryp_char=ord(refid[cnt1])
            encryp_refid_list.append(encryp_char)
            encryp_refid+=str(encryp_char)
            cnt1+=1
        valid = 'Y'
else:
        print("Invalid Reference ID. It should be length 12 and Alphanumeric")

if(valid == 'Y'):
    print("Encrypted Reference ID:{}".format(encryp_refid))
    is_decrypt=input("Do you w1234566701ant to decrypt the password:")


if(is_decrypt.lower()=="y"):
    decrypt_refid=""
    cnt2=0
    while (cnt2<len(encryp_refid_list)):
        dencryp_char=chr(int(encryp_refid_list[cnt2]))
        decrypt_refid+=dencryp_char
        cnt2+=1
    if(valid == 'Y'):
        print("Decrypted Reference ID :{}".format(decrypt_refid))

