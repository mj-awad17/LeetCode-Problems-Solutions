import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    col_names = ["student_id","age"]
    data = pd.DataFrame(student_data, columns=col_names)
    return data