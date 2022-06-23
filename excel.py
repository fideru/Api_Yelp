import openpyxl as opx



wb = opx.load_workbook("transactions.xlsx")
print(wb.sheetnames)

sheet = wb["Sheet1"]
cell = sheet["a1"]
print(cell.row)
print(cell.column)
print(cell.value)
column = sheet["a:c"]

