# Reading an excel file using Python 
import xlrd 


result_file = open('result.txt', encoding='utf-8', mode='w')

# Give the location of the file 
loc = ("School.xlsx") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 

sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
value = sheet.cell_value(5, 0)

text = ""
for x in range(3,sheet.nrows):
    number = str( int( sheet.cell_value(x,0)))
    school_name =  str( sheet.cell_value(x,1))
    text = text + number + "\t" + school_name + "\n"
    
    
result_file.write( text.rstrip())    
