file=open("G:/Big_Data_Hadoop/Euderka/PySpark/PythonScripting_Module3_Dataset/777_m3_datasets_v1.0/bank-data.csv","r")
print(file.readline())
f=open("G:/Big_Data_Hadoop/Euderka/PySpark/PythonScripting_Module3_Dataset/777_m3_datasets_v1.0/bank-data_output_test.csv","w")
for line in file.read():
    f.write(line)