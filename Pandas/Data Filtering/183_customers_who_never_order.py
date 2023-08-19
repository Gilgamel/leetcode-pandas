import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    # select the rows which 'id' is not present in orders['customerID']
    # ~: 这是一个逻辑运算符，用于对布尔序列进行取反操作，即将 True 转换为 False，False 转换为 True。

    never_o = customers[~customers['id'].isin(orders['customerId'])]

    # build dataframe
    df = never_o[['name']].rename(columns={'name':'Customers'})

    return df