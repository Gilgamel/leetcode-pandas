import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    # group based on customer_number
    ords = orders.groupby('customer_number')['order_number'].count().reset_index()

    # find out the customer with the largest number of orders
    max_ords = ords[ords['order_number'] == ords['order_number'].max()][['customer_number']]
    
    return max_ords