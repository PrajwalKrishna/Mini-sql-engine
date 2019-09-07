def selectColumns(columns,table):
    parsed_records = []
    for record in table:
        parsed_record = {}
        for column in columns:
            parsed_record[column] = record[column]
        parsed_records.append(parsed_record)
    return parsed_records

def selectDistinct(columns,table):
    parsed_records = []
    seen_records = {}
    for record in table:
        test_record = []
        for column in columns:
            test_record.append(record[column])
        if not seen_records.get(tuple(test_record)):
            seen_records[tuple(test_record)] = 1
            parsed_records.append(record)
    return parsed_records
