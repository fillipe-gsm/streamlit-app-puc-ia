"""An overview of the data"""
import pandas as pd
import streamlit as st
from config import settings


def introduction_section(df: pd.DataFrame) -> None:
    """Shows introduction section information"""
    st.header("Introdução")

    st.markdown(
        """
        Este app apresenta análises de consultas realizadas no Stack Overflow
        no ano de 2021.
        """
    )

    # The whole data is too large, so show a portion of it
    if st.checkbox(
        "Clique aqui para ver uma amostra dos dados brutos",
        value=False,
    ):
        st.dataframe(df[:settings.data_max_rows_display])

    st.markdown("Aqui está um breve resumo dos dados:")
    st.markdown(
        f"""
        - Quantidade de registros: {df.shape[0]}
        - Quantidade de colunas: {df.columns.size}
        """
    )
