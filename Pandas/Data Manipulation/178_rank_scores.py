import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    # rank from highest to lowest -> ascending = False
    # tie btwn two scores, then have same ranking
    # no holes btwn ranks -> rank 3, rank 3, rank 4
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html

    # use .rank to assign ranks to the scores
    # 'dense' like ‘min’, but rank always increases by 1 between groups
    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)

    # drop id col and sort values based on score 
    result = scores.drop('id', axis = 1).sort_values(by = 'score', ascending = False)

    return result





