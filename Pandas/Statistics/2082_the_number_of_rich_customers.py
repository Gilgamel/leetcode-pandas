import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:

    # rich = at least one bill > 500
    # filter out data that amount > 500
    rich_customers = store[store['amount'] > 500]

    # get the unique customer (based on customer ID)
    # .nunique() return the # of unique 
    num_rich_customers = rich_customers['customer_id'].nunique()

    result = pd.DataFrame({'rich_count': [num_rich_customers]})

    return result

