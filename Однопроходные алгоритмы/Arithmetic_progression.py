from os import path
import sys

if sys.version_info[0] < 3:
    input = raw_input

directory = "."
filename = "Arithmetic_progression_2018-03-04.txt"
thepath = path.join(directory, filename)
file = open(thepath)
is_data = True
curr = ""
number_list = []

while is_data:
    content = file.read(1)
    if content:
        is_data = True
        if content == " ":
            number = float(curr)
            curr = ""
            number_list.append(number)
        else:
            curr += content
    else:
        is_data = False
print(content)

n = 1
prev = number_list[0]
curr = number_list[1]
diff = curr - prev
is_progression = True
while n < len(number_list)-1:
    n += 1
    prev = curr
    curr = number_list[n]
    if (curr - prev) != diff:
        is_progression = False
        break
file.flush()
file.close()

if is_progression == False:
    print("This sequence is not arithmetic progression")
else:
    print("This sequence is arithmetic progression")