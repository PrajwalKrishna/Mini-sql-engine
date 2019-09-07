FUNCTIONS = ["max","min","sum","average"]

def col_max(table, column):
    temp = []
    for record in table:
        temp.append(record[column])
    return max(temp)

def col_min(table, column):
    temp = []
    for record in table:
        temp.append(record[column])
    return min(temp)

def col_sum(table, column):
    temp = []
    for record in table:
        temp.append(record[column])
    return sum(temp)

def col_average(table, column):
    temp = []
    for record in table:
        temp.append(record[column])
    return sum(temp)/len(temp)

def aggregateHandler(column,aggregate,table):
    if aggregate == 'max':
        return col_max(table, column)
    elif aggregate == 'min':
        return col_min(table, column)
    elif aggregate == 'sum':
        return col_sum(table, column)
    elif aggregate == 'average':
        return col_average(table, column)
