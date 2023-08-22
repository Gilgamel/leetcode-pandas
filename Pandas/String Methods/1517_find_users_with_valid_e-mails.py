import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    # https://regexr.com/
    # regex pattern ^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$
    # [A-Za-z] match any single uppercase or lowercase letter. The e-mail prefix name must start with a letter (no matter upper case or lower case)
    # [A-Za-z0-9]* match any number of characters following the first letter in the email prefix name. 
    
    valid_emails = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$')]

    return valid_emails