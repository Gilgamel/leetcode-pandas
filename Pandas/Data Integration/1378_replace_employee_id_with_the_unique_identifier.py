import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:

    # merge two tables based on 'id'
    # left to keep all info (name) from employees table
    merged = employees.merge(employee_uni, on = 'id', how = 'left')

    # return result with the 'unique_id' col
    result = merged[['unique_id','name']]

    return result