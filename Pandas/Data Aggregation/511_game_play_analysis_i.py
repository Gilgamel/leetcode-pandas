import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    # sort values based on palyer_id and event_date
    activity = activity.sort_values(by = ['player_id', 'event_date'])

    # group by player_id and select the min event_date for each player
    result = activity.groupby('player_id')['event_date'].min().reset_index()

    # rename col
    result.rename(columns = {'event_date': 'first_login'}, inplace = True)

    return result