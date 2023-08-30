import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:

    # group by make_name and date_id 
    result = daily_sales.groupby(['date_id', 'make_name']).nunique().reset_index()

    # rename col
    result.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']

    return result