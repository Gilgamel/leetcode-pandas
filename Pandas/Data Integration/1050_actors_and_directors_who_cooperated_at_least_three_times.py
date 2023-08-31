import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    # group based on actor_id and director_id , then count > 3
    result = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()

    return result[result['timestamp'] >= 3][['actor_id', 'director_id']]
