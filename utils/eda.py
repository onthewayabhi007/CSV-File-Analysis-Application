import pandas as pd
from utils.file_handler import load_dataframe

def perform_eda() -> str:
    try:
        # Load the dataframe
        df = load_dataframe()

        # Perform EDA and round numerical values to 2 decimal places
        eda_summary = df.describe().round(2).to_string()
        return f"EDA Report Summary:\n\n{eda_summary}"
    except Exception as e:
        return f"Error during EDA: {str(e)}"