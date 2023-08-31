import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    # group based on sell_date
    # .agg() 允许你在分组后的数据上应用不同的聚合函数
    grouped = activities.groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()

    # rename col
    grouped.columns = ['sell_date', 'num_sold', 'products']

    # sort result

    result = grouped.sort_values(by = 'sell_date')

    return result
