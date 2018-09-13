import pandas as pd
import chardet
import re
import monthdelta
import datetime

class FileMod:
 

    def AddColumnsToFile(self, filename, namedelimiter):       
        
        fileCountry=''
        fileyear=''
        firstmonth=''
        secondmonth=''

        countries = ("france", "germany", "italy", "spain")
        countrymatch = next((x for x in countries if x in filename.lower()), False)
        if(countrymatch!=False):
            fileCountry=countrymatch



        #sort out year
        match = re.match(r'.*([1-3][0-9]{3})', filename)
        if match is not None:
            fileyear= int(match.group(1))


        #sort out dates

        months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
        monthmatch = next((x for x in months if x in filename.lower()), False)
        if(monthmatch!=False):
            firstmonth=monthmatch


        monthmatch = next((x for x in months if x in filename.lower().replace(firstmonth, '')), False)
        if(monthmatch!=False):
            secondmonth=monthmatch


        tempmonth = firstmonth
        if filename.lower().find(firstmonth) > filename.lower().find(secondmonth):
          firstmonth=secondmonth
          secondmonth=tempmonth

        
        firstdate = datetime.date(fileyear, months.index(firstmonth)+1,1)
       
        monthdifference =  months.index(secondmonth)- months.index(firstmonth)

        if monthdifference<0:
            monthdifference+=12

        seconddate = firstdate + monthdelta.monthdelta(monthdifference)

       
        with open(filename+ '.csv', 'rb') as f:
            indexofnamedelimiter =filename.find(namedelimiter)
            result = chardet.detect(f.read())
            csv_input =pd.read_csv(filename +'.csv',encoding=result['encoding'])         #reading my csv file
            csv_input['filename'] = filename        #this would also copy the cell value 
            if indexofnamedelimiter>=0:
              csv_input['worksheet'] = filename[indexofnamedelimiter+len(namedelimiter):]
            else:
              csv_input['worksheet'] =''
            csv_input['country'] =fileCountry
            csv_input['year'] =fileyear
            csv_input['firstdate'] =firstdate
            csv_input['seconddate'] =seconddate
            csv_input.to_csv(filename +'.csv', index=False) 