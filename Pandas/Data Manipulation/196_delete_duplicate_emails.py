import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    
    # sort data based on id 
    person.sort_values(by = 'id', ascending = True, inplace = True)

    # remove duplicate
    person.drop_duplicates(subset = 'email', inplace = True)

# 先排序再去掉重复的邮箱是根据 submit 以后的报错而决定的。