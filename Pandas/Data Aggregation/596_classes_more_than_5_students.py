import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    # group by class, then filter out count() > 5
    class_counts = courses.groupby('class')['student'].count().reset_index()

    # filter classes with at least 5 students
    result = class_counts[class_counts['student'] >= 5][["class"]]

    return result