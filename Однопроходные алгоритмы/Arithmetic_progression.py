from os import path
import sys

if sys.version_info[0] < 3:
    input = raw_input

directory = "."
filename = input("Enter filename")
thepath = path.join(directory, filename)
file = open(thepath)
content = file.read()
print(content)



