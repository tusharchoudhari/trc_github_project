import math
user_input=input("Enter 3 values for D separated by comma:")
result_list=[]
C=50
H=30
#Q=math.sqrt(2*(C*D)/H)
#Q=math.sqrt(2*(C*D)/H)
for val in user_input.split(","):
    D=int(val)
    Q = math.sqrt(2 * (C * D) / H)
    result_list.append(str(int(Q)))
print(",".join(result_list))
