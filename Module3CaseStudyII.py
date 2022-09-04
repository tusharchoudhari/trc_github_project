i_file=open("G:/Big_Data_Hadoop/Euderka/PySpark/PythonScripting_Module3_Dataset/777_m3_datasets_v1.0/bank-data.csv","r")
job_list=[]
age_list=[]
age_criteria={}
header=True
for line in i_file.readlines():
    if(header==True):
         header=False
         continue
    else:
        job=line.split(",")[1].replace(".","")
        age=line.split(",")[0]
        if(job not in job_list):
            job_list.append(job)
        if(age not in age_list):
            age_list.append(int(age))
print(job_list)
i_file.close()
while True :
    prof=input("Enter Profession:")
    if(prof.upper()=="END"):
        break
    if(prof.lower() in job_list):
        print("Client is eligible for loan".format(prof))
    else:
        print("Client is not eligible for loan".format(prof))
    age_criteria['min']=min(age_list)
    age_criteria['max']=max(age_list)
    print("Loan eligibility age_criteria",age_criteria)



