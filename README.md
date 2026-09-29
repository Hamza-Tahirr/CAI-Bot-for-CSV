# CAI Bot for CSV

A small Streamlit app that lets you upload a CSV file and ask questions about it in plain English. The questions are answered by a LangChain CSV agent that uses an OpenAI model to write and run pandas code on your data.

## Features

- Upload any CSV file from the browser
- Ask questions about the data in natural language and get the answer on the page
- The agent works out answers by running pandas code on the loaded DataFrame
- The agent's intermediate steps are printed to the terminal for debugging
- Clear error message in the app if the OpenAI API key is missing

## Tech stack

- Python 3.10+
- Streamlit for the web interface
- LangChain (`langchain-experimental` CSV agent, `langchain-openai`)
- OpenAI completion model (`gpt-3.5-turbo-instruct`, the `langchain-openai` default) at temperature 0
- pandas
- python-dotenv for loading the API key

## Project structure

```
CAI-Bot-for-CSV/
├── main.py            # Streamlit app
├── data.csv           # sample dataset to try the app with
├── requirements.txt
├── .env.example       # template for the OpenAI API key
└── LICENSE
```

## Setup

1. Clone the repository and create a virtual environment:

   ```bash
   git clone https://github.com/Hamza-Tahirr/CAI-Bot-for-CSV.git
   cd CAI-Bot-for-CSV
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and put your OpenAI API key in it:

   ```
   OPENAI_API_KEY=your-openai-api-key
   ```

   You can also set `OPENAI_API_KEY` as a normal environment variable instead.

## Usage

```bash
streamlit run main.py
```

Open the local URL that Streamlit prints, upload a CSV file and type a question, for example "How many rows are there?" or "What is the average value of column X?".

## Sample data

`data.csv` is the Breast Cancer Wisconsin (Diagnostic) dataset from the UCI Machine Learning Repository. It has 569 rows with an `id`, a `diagnosis` column (`M` for malignant, `B` for benign) and 30 numeric features computed from cell nucleus images. You can try questions such as "How many malignant cases are there?" or "What is the mean radius_mean for benign cases?".

## Note on security

The CSV agent runs Python code written by the model on your machine (this is why `allow_dangerous_code=True` is set in `main.py`). Run the app locally and only with data you trust. Do not expose it publicly as is.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
