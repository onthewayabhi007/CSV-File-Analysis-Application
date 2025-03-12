# CSV Analysis Application

## Introduction
This application allows users to upload CSV files and perform various analytical operations, including Exploratory Data Analysis (EDA), data visualization, and querying the data using a language model (LLM). It is designed to streamline data analysis tasks and make insights easily accessible, even for non-technical users.

## Tech Stack
- **Python:** Core programming language.
- **Pandas:** For data manipulation and analysis.
- **Seaborn and Matplotlib:** Data visualization libraries.
- **Gradio:** Creating interactive UI components.
- **scikit-learn:** Used for statistical operations and data processing.
- **Ollama2:**  LLM for query responses.
- **Pydantic:** Data validation and settings management.

## Features
1. **CSV Upload:** Upload your CSV file for analysis.
2. **Feature Categorization:** Automatically categorize features as numerical or categorical.
3. **Exploratory Data Analysis (EDA):** Summarize key statistical information about the dataset.
4. **Visualization:** Generate various plots like scatterplot, lineplot, barplot, and heatmap.
5. **LLM Query:** Ask natural language questions about your data and get insightful answers.

## Installation
1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/yourusername/csv_analysis_app.git
   cd csv_analysis_app
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Ollama server:
   ```bash
   ollama serve
   ```
5. Run the application:
   ```bash
   python3 app.py
   ```

## Usage
1. **Upload CSV:** Click on 'Upload CSV' to upload your data file.
2. **View Features:** Navigate to the 'Features' tab to see categorized numerical and categorical features.
3. **Perform EDA:** Go to the 'EDA' tab and get a statistical summary.
4. **Visualize Data:** Choose features and graph types under 'Visualization' to generate plots.
5. **Query Data with LLM:** Use natural language to ask questions under the 'LLM Query' tab.

## Challenges and Solutions
- **Global Variable Management:** Initially faced issues with data persistence across different modules which is solved by using a global variable to store the uploaded DataFrame.
- **Data Loading Errors:** Encountered issues with loading files through Gradio which was addressed by correctly handling file paths and using Gradio’s file object handling.
- **Gradio and Ollama Integration Issues:** Faced problems where responses appeared correctly in Jupyter Notebook but not in the Gradio interface. Resolved it by ensuring consistent API endpoint configuration and proper integration between Ollama and Gradio.
- **Dependency Management:** Managing various libraries and their versions caused conflicts, resolved them by using a virtual environment and specifying exact versions in `requirements.txt`.
- **Server Configuration Errors:** Faced server connectivity issues when running the Ollama server. Resolved by checking firewall settings and ensuring that the correct port was being used.
- **Latency Issues:** The response time for LLM queries was initially slow. Optimized performance by streamlining data processing and minimizing unnecessary calculations.-

## Models and Techniques
1. **Data Analysis:** Pandas for data manipulation and basic statistics.
2. **Visualization:** Seaborn and Matplotlib for dynamic graph plotting.
3. **LLM Integration:** Utilized Ollama2 and Ollama for data-related question answering.

## Demo Video
[Click here to watch the demo](https://drive.google.com/file/d/1JeC_7hi5vVjXDTXJqM8RgPmnx-XMglR7/view?usp=sharing)

## Area of Improvement
- **Response Time:** Despite optimizations, the response time of the LLM queries is still relatively slow, which may affect the user experience. Further performance tuning or exploring alternative LLM models could help address this.
- **Accuracy of Answers:** Some responses from the LLM model may lack precision or relevance. Fine-tuning the model or employing post-processing techniques might improve the accuracy and consistency of answers.

## Contributing
Feel free to submit issues, fork the repository, and make pull requests.
