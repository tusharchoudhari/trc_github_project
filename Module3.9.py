usr_input = input("Enter rows,columns for 2 dimentional array:")
x = int(usr_input.split(",")[0])
y = int(usr_input.split(",")[1])
final_list = []
for i in range(x):
        ele_list = []
        for j in range(y):
            ele_list.append(i*j)
        final_list.append(ele_list)
print(final_list)