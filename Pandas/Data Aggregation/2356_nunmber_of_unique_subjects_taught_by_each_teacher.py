import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    # group by teacher_id and use .nunique()
    # remember to use.reset_index() to remove group labels
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    
    # rename col
    result.rename(columns = {'subject_id': 'cnt'}, inplace = True)

    return result