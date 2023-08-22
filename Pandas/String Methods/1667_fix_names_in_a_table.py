import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    # apply str.capitalize() to fix the names
    # str.capitalize() function: capitalize the first letter, and lowercase rest of str
    users['name'] = users['name'].str.capitalize()

    # sort result order by user_id
    df = users.sort_values(by = 'user_id', ascending = True)

    return df

