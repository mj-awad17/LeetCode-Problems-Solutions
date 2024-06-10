import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    idx = "month"
    col = "city"
    val = "temperature"
    return weather.pivot(index=idx, columns=col,values=val)
    