import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    # join based on student_id, then group based on student_id and subject_name
    # use cross to merge all outcome
    df1 = students.merge(subjects, how = 'cross')

    df2 = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams = ('subject_name', 'count')).reset_index()

    # merge result
    result = df1.merge(df2, on =['student_id','subject_name'], how = 'left').sort_values(by = ['student_id', 'subject_name'])

    # fill null values with 0 and select required cols
    return result.fillna(0)[['student_id','student_name','subject_name','attended_exams']]