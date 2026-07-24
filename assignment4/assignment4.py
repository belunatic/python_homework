import pandas as pd

# task 1 Introduction to Panda

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    }

#convert data to dataframe
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

#add new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

#increment a dataframe
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_with_salary['Age'] + 1
print(task1_older)

#write to csv
task1_older.to_csv('employees.csv', index=False)
print(task1_older)

#Task 2 - Loading Data from CVS and JSON

#load from CSV
task2_employees = pd.read_csv('./employees.csv')
print(task2_employees)

#load from JSON
json_employees = pd.read_json('./additional_employees.json')
print(json_employees)

#combine data frames
more_employees = pd.concat([task2_employees,json_employees,], ignore_index=True)
print(more_employees)