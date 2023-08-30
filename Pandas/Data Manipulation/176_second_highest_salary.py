import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    # drop duplicate salary values
    unique_salaries = employee['salary'].drop_duplicates()

    # sort salary values from highest to lowest
    # use nlargest(2) to find out the highest and second highest salaries, and use .iloc[-1] to locate the second highest salary
    second_highest = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None

    # if there is no second highest salary, then return None
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    result = pd.DataFrame({'SecondHighestSalary': [second_highest]})

    return result

