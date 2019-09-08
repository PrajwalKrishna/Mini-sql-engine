def isInt(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True

def queryParser(query,schema):
    words = query.split()
    n = len(words)
    if words[0].upper() != "SELECT":
        print("ERROR: CANNOT PARSE QUERY NO SELECT FOUND")
        exit(-1)
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
            print("ERROR: CANNOT FIND THE REFERED TABLE",table)
            exit(-1)

    aggregate = None
    FUNCTIONS = ["max","min","sum","average"]
    for FUNCTION in FUNCTIONS:
        if columns[0].split('(')[0].lower() == FUNCTION:
            aggregate = FUNCTION
    if aggregate:
        if len(columns) == 1:
            columns = [columns[0].split('(')[1].split(')')[0]]
            if columns[0] == '*':
                print("ERROR: CHECK AGGREGATE QUERY")
                print("USAGE: SELECT <aggregate>(<column>) FROM <table> WHERE <condition>")
                exit(-1)
        else:
            print("ERROR: CHECK AGGREGATE QUERY")
            print("USAGE: SELECT <aggregate>(<column>) FROM <table> WHERE <condition>")
            exit(-1)
    column_prefixed = []
    if columns[0] == '*':
        if len(columns) != 1:
            print("ERROR:\t","Using * operator invalid query")
            exit(-1)
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
                            print("ERROR","Column",column, "unresolved, may refer to multiple columns")
                            exit(-1)
                        column_prefix = table+'.'+i
            if not column_prefix:
                print("ERROR","Column ",column, "unresolved, column not found")
                exit(-1)
            column_prefixed.append(column_prefix)

    dict_conditions = {}
    if flag == 2 and not conditions:
        print("ERROR:","WHERE clause used but not conditions passed")
        exit(-1)
    if conditions:
        conjuction = None
        flag = -1
        for i in range(len(conditions)):
            if conditions[i].upper() == 'AND':
                conjuction = 'AND'
                flag = i
            elif conditions[i].upper() == 'OR':
                conjuction = 'OR'
                flag = i

        OPERATORS = ['<=','>=','<>','<','>','=']
        if conjuction:
            condition_1 = conditions[:flag]
            condition_2 = conditions[flag+1:]
            operator_1 = None
            parsed_condition_1 = []
            for condition in condition_1:
                for operator in OPERATORS:
                    split_condition = condition.split(operator)
                    if len(split_condition) > 1 or condition == operator:
                        operator_1 = operator
                        split_condition = [i for i in split_condition if i]
                        break
                    else:
                        split_condition = [condition]
                for column in split_condition:
                    if isInt(column):
                        parsed_condition_1.append(int(column))
                    else:
                        column_prefix = None
                        for table in tables:
                            for i in schema[table]:
                                if i == column or table+'.'+i == column:
                                    if column_prefix:
                                        print("ERROR","Column ",column, "unresolved in the WHERE clause,may refer to multiple columns")
                                        exit(-1)
                                    column_prefix = table+'.'+i
                        if not column_prefix:
                            print("ERROR","Column ",column, "unresolved in the WHERE clause, column not found")
                            exit(-1)
                        parsed_condition_1.append(column_prefix)
            if len(parsed_condition_1) != 2 or not operator_1:
                print("ERROR:","Check conditional arguments 1 in WHERE clause")
                exit(-1)
            operator_2 = None
            parsed_condition_2 = []
            for condition in condition_2:
                for operator in OPERATORS:
                    split_condition = condition.split(operator)
                    if len(split_condition) > 1 or condition == operator:
                        operator_2 = operator
                        split_condition = [i for i in split_condition if i]
                        break
                    else:
                        split_condition = [condition]
                for column in split_condition:
                    if isInt(column):
                        parsed_condition_2.append(int(column))
                    else:
                        column_prefix = None
                        for table in tables:
                            for i in schema[table]:
                                if i == column or table+'.'+i == column:
                                    if column_prefix:
                                        print("ERROR","Column ",column, "unresolved in the WHERE clause,may refer to multiple columns")
                                        exit(-1)
                                    column_prefix = table+'.'+i
                        if not column_prefix:
                            print("ERROR","Column ",column, "unresolved in the WHERE clause, column not found")
                            exit(-1)
                        parsed_condition_2.append(column_prefix)
            if len(parsed_condition_2) != 2 or not operator_2:
                print("ERROR:","Check conditional arguments 1 in WHERE clause")
                exit(-1)
        else:
            operator_1 = None
            parsed_condition_1 = []
            for condition in conditions:
                for operator in OPERATORS:
                    split_condition = condition.split(operator)
                    if len(split_condition) > 1 or condition == operator:
                        operator_1 = operator
                        split_condition = [i for i in split_condition if i]
                        break
                    else:
                        split_condition = [condition]
                for column in split_condition:
                    if isInt(column):
                        parsed_condition_1.append(int(column))
                    else:
                        column_prefix = None
                        for table in tables:
                            for i in schema[table]:
                                if i == column or table+'.'+i == column:
                                    if column_prefix:
                                        print("ERROR","Column ",column, "unresolved in the WHERE clause,may refer to multiple columns")
                                        exit(-1)
                                    column_prefix = table+'.'+i
                        if not column_prefix:
                            print("ERROR","Column ",column, "unresolved in the WHERE clause, column not found")
                            exit(-1)
                        parsed_condition_1.append(column_prefix)
            if len(parsed_condition_1) != 2 or not operator_1:
                print("ERROR:","Check conditional arguments 1 in WHERE clause")
                exit(-1)

        if operator_1 =='=' and \
           not isinstance(parsed_condition_1[0],int) and \
           not isinstance(parsed_condition_1[1],int):
           if column_prefixed.count(parsed_condition_1[1]):
               column_prefixed.remove(parsed_condition_1[1])

        dict_conditions['conjuction'] = conjuction
        dict_conditions['condition_1'] = parsed_condition_1
        dict_conditions['operator_1'] = operator_1
        if conjuction:
            dict_conditions['condition_2'] = parsed_condition_2
            dict_conditions['operator_2'] = operator_2
    return column_prefixed, tables, dict_conditions,aggregate, distinct_flag
