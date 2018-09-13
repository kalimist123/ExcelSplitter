from dateutil.parser import parse
import datetime
import monthdelta


import re


filename = "France PDL1 Excel_worksheet_France Apr-May 2017"

secondmonth=firstmonth=""
months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
monthmatch = next((x for x in months if x in filename.lower()), False)
if(monthmatch!=False):
    firstmonth=monthmatch


monthmatch = next((x for x in months if x in filename.lower().replace(firstmonth, '')), False)
if(monthmatch!=False):
    secondmonth=monthmatch

tempmonth = firstmonth
if filename.find(firstmonth) > filename.find(secondmonth):
    firstmonth=secondmonth
    secondmonth=tempmonth

print(firstmonth)
print(secondmonth)


print(months.index(firstmonth)+1)
print(months.index(secondmonth)+1)

firstdate = datetime.date(1987, months.index(firstmonth)+1,1)
seconddate = datetime.date(1987, months.index(secondmonth)+1,1)

monthdifference =  months.index(secondmonth)- months.index(firstmonth)

if monthdifference<0:
    monthdifference+=12

print("monthdifference:"+ str(monthdifference))
print(firstdate)
enddate = firstdate + monthdelta.monthdelta(monthdifference)
print(enddate)
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