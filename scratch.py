from dateutil.parser import parse



import re


file = "France PD-L1 1999 clack string"

match = re.match(r'.*([1-3][0-9]{3})', file)
if match is not None:
    print (match.group(1))

"""""
file = "France PD-L1 clack string"

year1 = parse(file, fuzzy=True).year 
print(year1)


try:
    year1 = parse(file, fuzzy=True).year 
except ValueError as e:
    year1 =e

print(year1)

filenames = glob.glob('*worksheet*')
for filename in filenames:
    print(filename)

str1 = "jip_worksheet_France Nov-Jan 2017.csv";
str2 = "worksheet_";
print(str1.find(str2))

index1 =str1.find(str2) 

print(str1[index1+10:])
print(str1[index1+10:-4])

"""""