from schemaParser import schemaParser
from loadTable import tableLoader
from aggregateFunctions import aggregateHandler
from joinTables import joinTables
from printTable import printTable
from queryParser import queryParser
from parseTable import selectColumns, selectDistinct, selectRecords

META_FILE = "../files/metadata.txt"
TABLE_DIR = '../files'

if __name__ == "__main__":
    schema = schemaParser(META_FILE)

    query = "select max(table1.B) from table1,table2 where table1.B=table2.B"
    columns,tables,conditions,aggregate,distinct = queryParser(query, schema)
    jointTable = joinTables(tables, schema, TABLE_DIR)
    if aggregate:
        print(aggregate,'(',columns[0],')','->',aggregateHandler(columns[0],aggregate,jointTable))
    else:
        reducedTable = selectRecords(columns, jointTable, conditions)
        reducedTable = selectColumns(columns, reducedTable)
        if distinct:
            reducedTable = selectDistinct(columns, reducedTable)
        printTable(reducedTable)
