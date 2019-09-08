import operator
OPERATORS = {
"<":operator.lt,
"<=":operator.le,
"=":operator.eq,
"<>":operator.ne,
">=":operator.ge,
">":operator.gt,
"AND":operator.and_,
"OR":operator.or_
}

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

def selectRecords(columns, table, conditions):
    parsed_records = []
    if not conditions['conjuction']:
        for record in table:
                a = conditions['condition_1'][0]
                if not isinstance(a, int):
                    a = record[a]
                b = conditions['condition_1'][1]
                if not isinstance(b, int):
                    b = record[b]
                if OPERATORS[conditions['operator_1']](a, b):
                    parsed_records.append(record)
    else:
        for record in table:
                a = conditions['condition_1'][0]
                if not isinstance(a, int):
                    a = record[a]
                b = conditions['condition_1'][1]
                if not isinstance(b, int):
                    b = record[b]
                c = conditions['condition_2'][0]
                if not isinstance(c, int):
                    c = record[c]
                d = conditions['condition_2'][1]
                if not isinstance(d, int):
                    d = record[d]
                if OPERATORS[conditions['conjuction']](OPERATORS[conditions['operator_1']](a, b),OPERATORS[conditions['operator_2']](c, d)):
                    parsed_records.append(record)
    return parsed_records
