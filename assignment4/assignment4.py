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

#Task 3 - Data inspection

#head()
first_three = more_employees.head(3)
print(first_three)

#tail()
last_two = more_employees.tail(2)
print(last_two)

#shape()
employee_shape = more_employees.shape
print(employee_shape)

#info
print(more_employees.info())

#Task 4 - Data Cleaning

#read from csv
dirty_data = pd.read_csv('./dirty_data.csv', sep=',')
print(dirty_data)

#copy df
clean_data = dirty_data.copy()
print(clean_data)

#drop_duplicates
clean_data =clean_data.drop_duplicates()
print(clean_data)

#numerical age 
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print(clean_data)

clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
print(clean_data)

# numerical salary and replace unknown / nan with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown','n/a'],pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary']= clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data)

#convert Hire Date to datetime
clean_data['Hire Date'] = clean_data['Hire Date'].str.strip()
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed')
print(clean_data)

#strip whitespace and make it uppercase
clean_data[['Name', 'Department']]= clean_data[['Name', 'Department']].apply(lambda col: col.str.strip())
clean_data[['Name', 'Department']]= clean_data[['Name', 'Department']].apply(lambda col: col.str.upper())
print(clean_data)
