import re

file1=open("category_stats").read()

print(re.findall('"kind":[0-9]+|"wound":[0-9]+',file1))
