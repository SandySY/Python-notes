from  openpyxl import Workbook

wb = Workbook()

sheet = wb.active
print(sheet.title)
sheet.title = 'sheet1'

sheet['B8'] = 'Hello'
sheet['c9'] = 'world!!'
# sheet['29'] = '29d!!'

sheet.append(['女孩', '177', '46'])

wb.save('demo.xlsx')