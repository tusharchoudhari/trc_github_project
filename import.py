import math
import sys
import os
import random
from math import sqrt
print("This is import program")
a=sqrt(4)
print(a)
import sys
print(sys.argv)
print(sys.winver)
print(sys.prefix)
#print(sys.exit())
print(sys.flags)
print(os.getcwd())
#print(os.chdir('G:/Big_Data_Hadoop/Euderka/Python/test_dir'))
#print(os.mkdir('G:/Big_Data_Hadoop/Euderka/Python/test_dir'))
print(os.name)
print(os.environ)
print(os.getlogin())
print(os.getppid())
print(os.path.join(sys.prefix,'/Users/addd'))
print(os.path.abspath("test.py"))
print(os.path.normpath("G:\Big_Data_Hadoop\Euderka\Python\import.py"))
print(os.path.split("G:\Big_Data_Hadoop\Euderka\Python\est.py"))
print(os.path.isdir("G:\Big_Data_Hadoop\Euderka\Python"))
print(os.path.exists("G:\Big_Data_Hadoop\Euderka\Python\est.py"))
# for ob in os.walk("G:\\Big_Data_Hadoop\\Euderka\\Python\\PythonProject\\venv\\Lib\\site-packages\\pip"):
#     print(ob)
print(random.randrange(100))
