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


employees = read_employees()

print(employees)