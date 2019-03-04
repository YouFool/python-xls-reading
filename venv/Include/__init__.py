import os
import xlrd

# Gets the Workbook URL based on the env variable 'XLS_PATH'
workbook = xlrd.open_workbook(os.getenv('XLS_PATH'))

# Gets sheet by name in the env variable 'SHEET_NAME'
sheet = workbook.sheet_by_name(os.getenv('SHEET_NAME'))

#Get the sheet number of rows and columns
num_rows = sheet.nrows
print("Number of rows: "+ str(num_rows))
num_columns = sheet.ncols
print("Number of columns: "+ str(num_columns))

# Gets the row i need to read
current_row = sheet.row(15)

data = []
for i in range(num_columns):
    data.append(current_row[i].value)
print(data)


