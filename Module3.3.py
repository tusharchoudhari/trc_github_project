import time
localtime=time.localtime()
print(localtime.tm_hour)
if(7<localtime.tm_hour<18):
    print("It is Day")
else:
    print("It is Dark")