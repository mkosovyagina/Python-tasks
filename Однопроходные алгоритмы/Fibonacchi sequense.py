import sys
if sys.version_info[0] < 3:
    input = raw_input
s = 0 #Variable for calculating number
curr = 1 #First number of sequence
prev = 1 #Second number of aequence
print("Enter the amount of first Fibonacci numbers you'd like to output")
n = int(input())  #Length of Fibonacchi sequence
print prev
print curr
for i in range(1, n-2): #Loop where we calculate the next number
    s = prev + curr
    prev = curr
    curr = s
    print s


