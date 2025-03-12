import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.file_handler import load_dataframe

def plot_graph(feature_x: str, feature_y: str, graph_type: str) -> str:
    try:
        df = load_dataframe()

        plt.figure(figsize=(8, 6))

        if graph_type == 'Scatterplot':
            sns.scatterplot(data=df, x=feature_x, y=feature_y)
        elif graph_type == 'Lineplot':
            sns.lineplot(data=df, x=feature_x, y=feature_y)
        elif graph_type == 'Barplot':
            sns.barplot(data=df, x=feature_x, y=feature_y)
        elif graph_type == 'Heatmap':
            # Automatically select numerical features for the heatmap
            numerical_df = df.select_dtypes(include=['number'])
            plt.figure(figsize=(10, 8))
            sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
            plt.title('Heatmap of Numerical Features Correlation')

        plot_path = 'plot.png'
        plt.savefig(plot_path)
        plt.close()
        return plot_path
    except Exception as e:
        return f"Error during plotting: {str(e)}"