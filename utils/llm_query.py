import ollama
import pandas as pd
from utils.file_handler import load_dataframe

def llm_query(question: str) -> str:
    try:
        df = load_dataframe()
        
        # Handle greetings separately
        if question.lower() in ['hi', 'hello', 'hey', 'good morning', 'good evening']:
            return "Hello! Please ask a specific question related to the uploaded data."

        data_preview = df.to_string(index=False)
        prompt = f"Here is the data from the uploaded CSV:\n{data_preview}\n\nAnswer the following question based on this data:\n{question}"
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])

        response_text = response.get("message", {}).get("content", "No response received.")
        return response_text
    except Exception as e:
        return f"Error with LLM query: {str(e)}"