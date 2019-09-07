from loadTable import tableLoader
from itertools import product

def joinTables(tableNames,schema, TABLE_DIR):
    tables = [tableLoader(tableName,schema[tableName],TABLE_DIR) for tableName in tableNames]
    product_table = list(product(*tables))
    joint_table = []
    for i in product_table:
        record = {}
        for j in i:
            for k in j:
                record[k] = j[k]
        joint_table.append(record)
    return joint_table
