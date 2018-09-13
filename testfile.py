from FileMod import FileMod
import glob

filemod = FileMod()

"""
filemod.AddColumnsToFile('jip_worksheet_France Apr-May 2017','worksheet_')
"""

filenames = glob.glob('*worksheet*')
for filename in filenames:
    print(filename[:-4])
    filemod.AddColumnsToFile(filename[:-4],'worksheet_')