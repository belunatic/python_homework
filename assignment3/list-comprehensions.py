import csv

employees_list =[]

with open('../csv/employees.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        employees_list.append(row)

# print(employees_list)

employee_names = [ f'{x[1]} {x[2]}' for idx, x in enumerate(employees_list) if idx != 0]

# print(employee_names)

employee_name_with_e = [x for x in employee_names if 'e' in x]

print(employee_name_with_e)
