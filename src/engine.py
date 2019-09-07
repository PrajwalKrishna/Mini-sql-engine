from schemaParser import schemaParser
from loadTable import tableLoader
from aggregateFunctions import aggregateHandler
from joinTables import joinTables
from printTable import printTable
from queryParser import queryParser
from parseTable import selectColumns, selectDistinct

META_FILE = "../files/metadata.txt"
TABLE_DIR = '../files'

if __name__ == "__main__":
    schema = schemaParser(META_FILE)

    query = "select distinct A,C from table1, table2 wHere A>C"
    # query = "select A, C from table1,table3, table2 wHere 3"
    columns,tables,conditions,aggregate,distinct = queryParser(query, schema)

    jointTable = joinTables(tables, schema, TABLE_DIR)
    if aggregate:
        print(aggregate,'(',columns[0],')','->',aggregateHandler(columns[0],aggregate,jointTable))
    else:
        reducedTable = selectColumns(columns, jointTable)
        if distinct:
            reducedTable = selectDistinct(columns, reducedTable)
        printTable(reducedTable)
