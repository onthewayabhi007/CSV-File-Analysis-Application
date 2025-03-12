import gradio as gr
from utils import upload_csv, display_features, perform_eda, plot_graph, llm_query
from models.query_processor import CSVFile, QueryRequest, PlotRequest, EDAResponse, LLMResponse, PlotResponse

try:
    # Gradio Interface for Upload
    upload_interface = gr.Interface(
        fn=upload_csv,
        inputs=gr.File(label='Upload CSV'),
        outputs=gr.Textbox(label='Upload Status'),
        title='Upload CSV File'
    )

    # Gradio Interface for Features Display
    feature_interface = gr.Interface(
        fn=display_features,
        inputs=None,
        outputs=gr.Textbox(label='Available Features'),
        title='Feature List'
    )

    # Gradio Interface for EDA
    eda_interface = gr.Interface(
        fn=perform_eda,
        inputs=None,
        outputs=gr.Textbox(label='EDA Summary'),
        title='Exploratory Data Analysis (EDA)'
    )

    # Gradio Interface for LLM Query
    query_interface = gr.Interface(
        fn=llm_query,
        inputs=gr.Textbox(label='Ask a Question from the Data'),
        outputs=gr.Textbox(label='LLM Answer'),
        title='Query the Data with LLM'
    )

    # Gradio Interface for Graph Plotting
    plot_interface = gr.Interface(
        fn=plot_graph,
        inputs=[
            gr.Textbox(label='Feature X'),
            gr.Textbox(label='Feature Y'),
            gr.Radio(['Scatterplot', 'Lineplot', 'Barplot', 'Heatmap'], label='Select Graph Type')
        ],
        outputs=gr.Image(type="filepath", label='Graph'),
        title='Data Visualization'
    )

    # Combining all interfaces into a Tabbed Interface
    demo = gr.TabbedInterface(
        interface_list=[upload_interface, feature_interface, eda_interface, plot_interface, query_interface],
        tab_names=["Upload CSV", "Features", "EDA", "Visualization", "LLM Query"]
    )

    # Launch the Gradio App
    if __name__ == "__main__":
        demo.launch()
        
except Exception as e:
    print(f"Error while launching the Gradio app: {str(e)}")
