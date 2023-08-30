import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    # drop duplicate salary values
    unique_salaries = employee['salary'].drop_duplicates()

    # sort unique salary values from highest to lowest
    sorted_salaries = unique_salaries.sort_values(ascending = False) 

    # if N exceeds the # of unique salaries, return None (eg., 10 rows of salaries, ask 12th highest)
    if N > len(sorted_salaries):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    
    # locate the Nth highest salary from the sorted salaries
    nth_highest = sorted_salaries.iloc[N-1]

    return pd.DataFrame({'Nth Highest Salary': [nth_highest]})