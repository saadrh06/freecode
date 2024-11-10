import re
s = 'A message from csev@newton.edu to cwen@pytha.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)