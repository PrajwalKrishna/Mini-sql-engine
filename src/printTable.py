def printTable(table):
    if not len(table):
        print(None)
        return
    for key in table[0].keys():
        print(key,'\t', end='')
    print()
    for record in table:
        [print(record[key],'\t',end='') for key in record.keys()]
        print()
