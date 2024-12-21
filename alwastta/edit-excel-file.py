from openpyxl import load_workbook

book = load_workbook('new.xlsx')
sheet = book.active

for row in sheet['E0':'E356']:
    for cell in row:
        cell_value = cell.value + ""
        c = cell_value.split('\n')
        print(c)

        link = ''
        for l in c: 
            link += l + ', '
        cell.value = link
        
for row in sheet['E0':'E356']:
    for cell in row:
        print(cell.value)

print('saving file ...')
book.save('new-file.xlsx')