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
                print(len(rows))
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

#task 4
def first_name(employee_index):
    get_index = column_index('first_name')
    #retrieve the name
    get_first_name = employees["rows"][employee_index][get_index]
    return get_first_name
    
print(first_name(1))