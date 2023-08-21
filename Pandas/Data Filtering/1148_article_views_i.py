import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    # filter rows where author_id and viewer+id are same
    author_viewer = views[views['author_id'] == views['viewer_id']]

    # get unique author_id from filtered data
    unique_authors = author_viewer['author_id'].unique()

    # sort and rename column
    unique_authors = sorted(unique_authors)

    df = pd.DataFrame({'id':unique_authors})

    return df
    
