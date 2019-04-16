import os, sys, xlrd

workbookdir = ""
sheetname = ""
if (sys.argv[1]):
    workbookdir = sys.argv[1]
    sheetname = sys.argv[2]
else :
    workbookdir = os.getenv('XLS_PATH')
    sheetname = os.getenv('SHEET_NAME')

while(True):
	# Gets the Workbook URL based on the env variable 'XLS_PATH' or ARGV
	workbook = xlrd.open_workbook(workbookdir)

	# Gets sheet by name 
	sheet = workbook.sheet_by_name(sheetname)

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
	


