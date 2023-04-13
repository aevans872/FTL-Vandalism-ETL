# Import the required library
import requests
import pandas as pd
import io
def extract_data(url):
    response = requests.get(url)  # Get the file
    with open("vandalism_raw.csv", "wb") as f:  # save file locally
        f.write(response.content)
    df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    return df