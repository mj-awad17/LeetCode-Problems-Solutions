import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """ Update() function used to update dataframe value"""
    modify = employees["salary"]*2
    employees.update(modify)
    return employees