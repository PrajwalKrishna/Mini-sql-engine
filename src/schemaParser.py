begin_identifier = "<begin_table>"
end_identifier = "<end_table>"

def schemaParser(META_FILE):
    with open(META_FILE, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    schema = {}
    flag = 0
    columns = []
    tableName = None
    for line in lines:
        if line == begin_identifier:
            flag = 1
            tableName = None
            columns = []
        elif line == end_identifier:
            flag = 0
            if not tableName:
                pass
            if not columns:
                pass
            if tableName in schema.keys():
                pass
            schema[tableName] = columns
        elif flag == 1:
            tableName = line
            flag = 2
        elif flag == 2:
            columns.append(line)
    return schema
