import sys
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

    if len(sys.argv) != 2 :
        print("Error: Incorrect usage")
        print("Usage: python3 20171091.py <sql-query>")
    elif sys.argv[1][-1] != ';':
        print("Error: Sql query not terminated")
    else:
        try:
            query = sys.argv[1]
            query = query[:-1]
            if(len(query)==0):
                print("Error: Empty query encountered")
                exit(-1)
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
        except Exception:
            traceback.print_exc()
