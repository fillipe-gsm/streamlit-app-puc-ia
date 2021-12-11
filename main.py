import streamlit as st

from streamlit_stackoverflow.data_handling import preprocess_data
from streamlit_stackoverflow.introduction import introduction_section
from streamlit_stackoverflow.single_dimensional_analysis import (
    single_dimensional_section
)
from streamlit_stackoverflow.multi_dimensional_analysis import (
    multi_dimensional_section
)


def create_app() -> None:
    """Main function to create the whole app"""
    st.title("Trabalho Prático 2: Análise de dados do StackOverflow para 2021")
    df = preprocess_data()

    introduction_section(df)
    single_dimensional_section(df)
    multi_dimensional_section(df)


if __name__ == "__main__":
    create_app()
