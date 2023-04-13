import pandas as pd

#df = pd.read_csv("vandalism.csv")

# Clean and transform the data
def transform_data(df):
    df = df.rename(columns={"actdate" : "date", "acttime" : "time"})
    df["date"] = pd.to_datetime(df["date"])  # Convert the date column to datetime format
    df.at[517, 'time'] = str(df.at[517, 'time']).zfill(4) # Fix values with typos
    df.at[883, 'time'] = str(df.at[883, 'time']).zfill(4)
    df['time'] = pd.to_datetime(df['time'], format='%H%M').dt.time
    df['date'] = pd.to_datetime(df['date']).dt.date # Extract date from date column without time
    df['zip'] = df['zip'].astype(str).replace('\.0', '', regex=True)

    df.to_csv("vandalism_cleaned.csv", index=False)

    return df