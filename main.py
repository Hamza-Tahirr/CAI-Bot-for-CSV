import os

import streamlit as st
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import OpenAI


def main():
    load_dotenv()

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV")

    if not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY is not set. Add it to a .env file or your environment.")
        st.stop()

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:
        # The agent answers by running pandas code on the data, which
        # langchain_experimental only allows with an explicit opt-in.
        agent = create_csv_agent(
            OpenAI(temperature=0),
            csv_file,
            verbose=True,
            allow_dangerous_code=True,
        )

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question:
            with st.spinner(text="In progress..."):
                response = agent.invoke({"input": user_question})
                st.write(response["output"])


if __name__ == "__main__":
    main()
