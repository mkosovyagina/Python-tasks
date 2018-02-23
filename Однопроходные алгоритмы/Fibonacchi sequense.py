import sys
if sys.version_info[0] < 3:
    input = raw_input
s = 0
curr = 1
prev = 1
print("Enter the amount of first Fibonacci numbers you'd like to output")
n = int(input())
print prev
print curr
for i in range(1, n-2):
    s = prev + curr
    prev = curr
    curr = s
    print s


