import openpyxl


book = openpyxl.load_workbook("tags_for_bd.xlsx", read_only=True)
sheet = book.active
rez = sheet[2][0].value
rez = rez.replace('"', '').split(',')

print(rez)
