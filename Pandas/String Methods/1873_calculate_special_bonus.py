import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # create new column called bonus with value 0
    employees['bonus'] = 0

    # calculate bonus based on the conditions
    # employees['employee_id'] % 2 != 0 -> odd number id
    # filter out name that is not start with 'M'
    employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']

    # select employee_id and bonus from dataset
    # sort value based on employee_id

    df = employees[['employee_id', 'bonus']].sort_values(by = 'employee_id', ascending = True)
    
    return df

    




# reference
# https://www.exxactcorp.com/blog/Deep-Learning/how-to-speed-up-python-pandas-by-over-300x
# https://tryolabs.com/blog/2023/02/08/top-5-tips-to-make-your-pandas-code-absurdly-fast
