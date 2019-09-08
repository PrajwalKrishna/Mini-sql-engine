def printRow(row):
    width=15
    print('|',end='')
    for i in row:
        i=str(i)
        i=i.center(width)
        print(i,end='|')
    print()
    border = '-' * width + ' '
    border = ' ' + border * len(row)
    print(border)

def printTable(table):
    if not len(table):
        print(None)
        return
    printRow(table[0])
    for record in table:
        printRow([record[element] for element in record.keys()])
