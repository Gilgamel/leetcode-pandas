import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    # filter invalid tweet (content len greater than 15)
    invalid_tweet = tweets[tweets['content'].str.len() > 15]

    invalid_tweet = invalid_tweet[['tweet_id']]

    return invalid_tweet