import pandas as pd
from models.query_processor import CSVFile

# Global variable to store the uploaded DataFrame
uploaded_df = None

def upload_csv(file) -> CSVFile:
    global uploaded_df
    try:
        file_path = file.name if hasattr(file, 'name') else file
        uploaded_df = pd.read_csv(file_path)

        # Save file path in Pydantic model
        csv_file = CSVFile(file_path=file_path)
        return f"File uploaded successfully\nFile Path: {file_path}"
    except Exception as e:
        raise ValueError(f"Error loading file: {str(e)}")

def load_dataframe() -> pd.DataFrame:
    global uploaded_df
    if uploaded_df is None:
        raise ValueError("⚠️ No CSV file has been uploaded yet.")
    return uploaded_df

def display_features() -> str:
    try:
        # Load the dataframe from the uploaded DataFrame
        df = load_dataframe()
        
        # Categorize features
        numerical_features = df.select_dtypes(include=['number']).columns.tolist()
        categorical_features = df.select_dtypes(exclude=['number']).columns.tolist()
        
        # Format the output
        output = f"Numerical Features: {', '.join(numerical_features)}\n"
        output += f"Categorical Features: {', '.join(categorical_features)}"
        return output
    except Exception as e:
        return f"Error displaying features: {str(e)}"
