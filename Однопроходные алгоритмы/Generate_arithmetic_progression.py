#Generating arithmetic progression with parameters

import sys
import datetime

if sys.version_info[0] < 3:
    input = raw_input

n = int(input("Input the length of progression"))
first_num = float(input("Input the first number of progression"))
diff = float(input("Input the difference of the progression"))
filename = str("Arithmetic_progreesion") + str(".txt")
file = open(filename, 'w')
num = first_num  #Wrinting in file the first number
file.write(str(num))
file.write(" ")

for i in range(n):  #In loop we calculate the value of new member in this progression and put it in the text file
    num += diff
    file.write(str(num))
    file.write(" ")

file.flush()
file.close()
