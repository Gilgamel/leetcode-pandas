import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    # immediate -> delivery date = order date
    # scheduled -> otherwise

    # use .shape[0] to get number of rows
    immediate_count = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]

    # calculate the total count of orders
    total_orders = delivery.shape[0]

    # calculate the % of immediate orders
    immediate_percentage = (immediate_count / total_orders) * 100

    # create dataframe and use round to keep 2 decimal
    result = pd.DataFrame({'immediate_percentage': [round(immediate_percentage, 2)]})

    return result

