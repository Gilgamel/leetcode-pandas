import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    # use groupby and find out the highest salary

    # use .empty to check if there is empty value in employee or department
    if employee.empty or department.empty:
        return pd.DataFrame(columns = ['Department', 'Employee', 'Salary'])

    # merge employee and department dataframe based on 'departmentId' and 'id'
    merged_df = employee.merge(department, left_on = 'departmentId', right_on = 'id', suffixes = ('_employee', '_department'))

    # use groupby to group data based on 'departmentID'
    highest_salary_df = merged_df.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])

    # reset the index of highest_salary_df to remove the group labels
    highest_salary_df = highest_salary_df.reset_index(drop=True)

    # select the rquired cols
    result = highest_salary_df[['name_department', 'name_employee', 'salary']]

    # rename col 
    result.columns = ['Department' , 'Employee', 'Salary']

    return result
