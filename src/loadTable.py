import csv

def tableLoader(tableName, columns, TABLE_DIR):
    FILE_NAME = TABLE_DIR + '/' + tableName + '.csv'
    records = []
    n = len(columns)
    with open(FILE_NAME, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            record = {}
            for i in range(n):
                record[tableName + '.' + columns[i]] = int(line[i])
            records.append(record)
    return records
