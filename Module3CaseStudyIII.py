import re
class Customer:
        title=""
        first=""
        last=""
        isblacklisted=0
        def setAttribute(self,title,first,last,isblacklisted):
            self.title=title
            self.first=first
            self.last=last
            self.isblacklisted=isblacklisted
        def display(self):
            print("Title:{}\nFirst:{}\nlast:{}\nisblacklisted:{}".format(self.title,self.first,self.last,self.isblacklisted))
class Order:
        produt_name=""
        product_code=""
        title=""
        first=""
        last=""
        isblacklisted=0
        def setProductName(self,produt_name):
             self.product_name=produt_name
        def setProductCode(self,produt_code):
             self.product_code=produt_code
        def getProductName(self):
            return self.product_name
        def getroductCode(self):
            return self.product_code
        def createOrder(self,cust):
            self.tilte = cust.title
            self.first = cust.first
            self.last = cust.last
            self.isblacklisted = cust.isblacklisted
            try:
                if(int(cust.isblacklisted)==1):
                    raise CustomerNotAllowedException
                else:
                    return self
            except CustomerNotAllowedException:
                print("Customer is not allowed as blacklisted flag is {}".format(cust.isblacklisted))
                return self
class CustomerNotAllowedException(Exception):
    pass

i_file=open("G:/Big_Data_Hadoop/Euderka/PySpark/PythonScripting_Module3_Dataset/777_m3_datasets_v1.0/FairDealCustomerData.csv")
custs=[]
lines=i_file.readlines()
for line in lines:
    cust=Customer()
    ord=Order()
    full_name=line.split(",")[1].lstrip()
    title=re.split("\s",full_name)[0]
    first=re.split("\s",full_name)[1]
    last=re.split("\s",full_name)[2]
    isblacklisted=line.split(",")[2]
    cust.setAttribute(title,first,last,isblacklisted)
    print("-------------------")
    cust.display()
    product_details=input("Enter ProductName and ProductCode(Separted by Space):")
    ord.setProductName(product_details.split(" ")[0])
    ord.setProductCode(product_details.split(" ")[1])
    cust_ord_details=ord.createOrder(cust)
    print("The customer order details are:\nTitle:{}\nFirst:{}\nLast:{}\nProduct Name:{}\nProduct Code:{}".format(
        cust_ord_details.title, cust_ord_details.first, cust_ord_details.last, cust_ord_details.getProductName(), cust_ord_details.getroductCode()))
