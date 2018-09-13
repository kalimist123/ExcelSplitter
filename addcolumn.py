import pandas as pd
import chardet


with open('addcolumnsame.csv', 'rb') as f:
    result = chardet.detect(f.read())

csv_input =pd.read_csv('addcolumn.csv',encoding=result['encoding'])         #reading my csv file
csv_input['Phone1'] = ''         #this would also copy the cell value 
csv_input['Phone2'] = csv_input['Disease']
csv_input['Phone3'] = csv_input['Disease']
csv_input['Phone4'] = csv_input['Disease']
csv_input['Phone5'] = csv_input['Disease']
csv_input['Country'] = csv_input['Disease']
csv_input['Website'] = csv_input['Disease']
csv_input.to_csv('addcolumnsame.csv', index=False) 