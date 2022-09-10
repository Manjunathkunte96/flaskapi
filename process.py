# 1) GET all employee
# 2) GET employee by id
# 3) Create employee

from db import mysqlconnect


def get_all_employee():

    results_list = []
    cur = mysqlconnect()
    cur.execute('select * from emp_details')
    output = cur.fetchall()
    cur.close()
    for row in output:
        results = {}
        results['id']=row[0]
        results['name']=row[1]
        results_list.append(results)
    return results_list

def get_employee_by_id(id):
    return

def create_employee(emp):
    return

print(get_all_employee())