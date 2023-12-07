def initialize_tables(num_partitions):
    hash_tables = []
    for _ in range(num_partitions):
        hash_tables.append({})
    return hash_tables


def build_hash_table(table, joinKey, num_partitions):
    
    hash_table = initialize_tables(num_partitions)
    for row in table:
        hash_value = hash(row[joinKey])
        partition = hash_value % num_partitions
        if hash_value not in hash_table[partition]:
            hash_table[partition][hash_value] = []
        hash_table[partition][hash_value].append(row)
    return hash_table
    

def hash_join(table1, table2, joinKey, num_partitions):

    hash1 = build_hash_table(table1, joinKey, num_partitions)

    results= []

    for row2 in table2:
        
        hash_value = hash(row2[joinKey])
        partition = hash_value % num_partitions
        
        for row1 in hash1[partition].get(hash_value,[]):
            if row1[joinKey] == row2[joinKey]:
                results.append({**row1,**row2})
    return results



if __name__ == "__main__":
    employees = [
        {'EmpID': 1, 'EmpName': 'Alice', 'DepartmentID': 100},
        {'EmpID': 2, 'EmpName': 'Bob', 'DepartmentID': 200},
        {'EmpID': 3, 'EmpName': 'Charlie', 'DepartmentID': 100},
        {'EmpID': 4, 'EmpName': 'David', 'DepartmentID': 300},
    ]

    departments = [
        {'DepartmentID': 100, 'DepartmentName': 'HR'},
        {'DepartmentID': 200, 'DepartmentName': 'IT'},
        {'DepartmentID': 300, 'DepartmentName': 'Finance'},
    ]

    num_partitions = 3 #Different DepartmentIDs
    print("🚀 ~ file: HashJoin.py:46 ~ num_partitions:", num_partitions)
    
    joinKey = 'DepartmentID'
    result = hash_join(employees, departments, 'DepartmentID', num_partitions)
    print(result)
