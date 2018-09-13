import pandas as pd
import chardet
import re

class FileMod:
 

    def AddColumnsToFile(self, filename, namedelimiter):       
        
        fileCountry=''
        fileyear=''
        countries = ("france", "germany", "italy", "spain")
        countrymatch = next((x for x in countries if x in filename.lower()), False)
        if(countrymatch!=False):
            fileCountry=countrymatch

        match = re.match(r'.*([1-3][0-9]{3})', filename)
        if match is not None:
            fileyear= match.group(1)

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
            csv_input.to_csv(filename +'.csv', index=False) 