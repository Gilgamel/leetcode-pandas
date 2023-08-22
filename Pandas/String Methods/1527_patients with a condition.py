import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    # use regex expression r'\bDIAB1' to filter data
    # \b 表示单词边界，而 'DIAB1' 是要匹配的字符串。正则表达式中的 \b 表示单词边界，用于匹配单词的开始或结束位置。具体来说，它匹配一个位置，该位置要么位于一个字符串的开头，要么位于一个单词字符（字母、数字、下划线）和非单词字符（如空格、标点符号）之间的位置。
    patients_diab1 = patients[patients['conditions'].str.contains(r'\bDIAB1')]

    return patients_diab1