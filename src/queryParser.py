def queryParser(query,schema):
    words = query.split()
    n = len(words)
    if words[0].upper() != "SELECT":
        pass
    distinct_flag = False
    flag = 0
    columns = []
    tables = []
    conditions = []
    for i in range(1,n):
        if words[i].upper() == "FROM":
            flag = 1
        elif words[i].upper() == "WHERE":
            flag = 2
        elif flag == 0:
            if words[i].upper() == "DISTINCT":
                distinct_flag = True
                continue
            temp = words[i].split(',')
            [columns.append(word) for word in temp if word]
        elif flag == 1:
            temp = words[i].split(',')
            [tables.append(word) for word in temp if word]
        elif flag == 2:
            temp = words[i].split(',')
            [conditions.append(word) for word in temp if word]

    for table in tables:
        if not table in schema.keys():
            print("ERROR")
            pass

    aggregate = None
    FUNCTIONS = ["max","min","sum","average"]
    for FUNCTION in FUNCTIONS:
        if columns[0].split('(')[0].lower() == FUNCTION:
            aggregate = FUNCTION
    if aggregate:
        if len(columns) == 1:
            columns = [columns[0].split('(')[1].split(')')[0]]
        else:
            print("ERROR:\t","Check aggregate query")

    column_prefixed = []
    if columns[0] == '*':
        if len(columns) != 1:
            print("ERROR:\t","Using * operator invalid query")
        for table in tables:
            for i in schema[table]:
                column_prefix = table+'.'+i
                column_prefixed.append(column_prefix)
    else:
        for column in columns:
            column_prefix = None
            for table in tables:
                for i in schema[table]:
                    if i == column or table+'.'+i == column:
                        if column_prefix:
                            print("ERROR","Column ",column, "unresolved")
                        column_prefix = table+'.'+i
            if not column_prefix:
                print("ERROR","Column ",column, "unresolved")
            column_prefixed.append(column_prefix)

    # print(column_prefixed)
    # print(tables)
    # print(aggregate)
    return column_prefixed, tables, conditions,aggregate, distinct_flag
