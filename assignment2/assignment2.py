#task 2
import csv

def read_employees():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv') as file:
            employee_info = csv.reader(file)
            #loop the rows
            for index, row in enumerate(employee_info):
                if index == 0:
                    data["fields"] = row
                else:
                    rows.append(row)  
            data['rows'] = rows
            return data
    except Exception as e:
        print(f"Error occurred: {e}")

#employee data
employees = read_employees()

#task 3
def column_index(header):
    return employees["fields"].index(header)

employee_id_column = column_index('employee_id')
print(employee_id_column)

#task 4
def first_name(employee_index):
    get_index = column_index('first_name')
    #retrieve the name
    get_first_name = employees["rows"][employee_index][get_index]
    return get_first_name
    
#task 5
def employee_find(employee_id):
    #callback for a filter function
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    #filter(function, iterable)
    #list() builds a list
    matches=list(filter(employee_match, employees["rows"]))
    return matches

#task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#task 7
def sort_by_last_name():
    employees['rows'].sort(key = lambda row: row[column_index('last_name')])
    return employees['rows']

#task 8
def employee_dict(row):
    single_employee_info = dict(zip(employees['fields'], row))
    single_employee_info.pop("employee_id")
    return single_employee_info


