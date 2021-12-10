import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from config import settings


def multi_dimensional_section(df: pd.DataFrame) -> None:
    """Plots and analyses with multiple variable"""
    st.header("Análise multidimensional")
    st.markdown(
        """
        Esta seção concentra resultados envolvendo mais de uma variável.
        """
    )

    _year_salary(df)


def _year_salary(df_raw: pd.DataFrame) -> None:
    """Year salary analysis"""

    st.subheader("Salário anual convertido")

    # Remove NaN salaries as they are useless to us
    df = df_raw[~df_raw[settings.YEARLY_SALARY].isna()]
    _year_age_salary(df)
    _year_edlevel_salary(df)
    _year_mentalhealth_salary(df)


def _year_age_salary(df: pd.DataFrame) -> None:
    """Combine year with age"""
    st.markdown("#### Salário por idade")
    st.markdown(
        """
        Talvez o indicativo de maior interesse seja o salário anual dos
        participantes. Vamos começar determinando qual a sua relação com a
        faixa de idade.

        Como se vê, todas as faixas são dominadas por outliers nos dados. A
        maior aberração parece ocorrer na faixa de 55-64 anos com um salário
        anual acima de 40 milhões de dólares. Mas claro, não parece justo tirar
        conclusões baseadas em dados muito fora da curva.
        """
    )

    ax = df.boxplot(column=settings.YEARLY_SALARY, by=settings.AGE, rot=90)
    ax.set_title("Salário por faixa de idade")
    st.pyplot(ax.get_figure())

    st.markdown(
        """
        Sendo assim, o próximo gráfico remove estes outliers. A tendência
        central parece subir com a experiência, o que é animador. Nas faixas
        envolvendo 35 anos ou mais, a grande variabilidade dos dados não parece
        sugerir que haja diferença significativa entre os salários, mas
        conseguimos ver um aumento pronunciado nesta faixa quando comparado com
        cargos de participantes abaixo de 24 anos.
        """
    )

    ax2 = df.boxplot(
        column=settings.YEARLY_SALARY,
        by=settings.AGE,
        rot=90,
        showfliers=False,
    )
    ax2.set_title("Salário por faixa de idade sem outliers")
    st.pyplot(ax2.get_figure())


def _year_edlevel_salary(df: pd.DataFrame) -> None:
    """Combine year with education level"""
    st.markdown("#### Salário por escolaridade")
    st.markdown(
        """
        Como antes, os dados são dominados por outliers. O mais alto deles,
        surpreendemente, pertence a um participante com apenas o nível primário
        de escolaridade. De todo modo, para evitar conclusões errôneas, o
        próximo gráfico mostra as mesmas informações sem os outliers.

        É possível observar que, dada a grande variabilidade em todos os
        grupos, não parece haver diferença significativa em nenhum deles. Ou
        seja, o salário típico não parece depender dos níveis de escolaridade
        dos participantes. Talvez a própria existência do StackOverflow seja
        suficiente para explicar isso: grande parte da informação necessária
        para aprender e a tirar dúvidas encontra-se disponível, e assim as
        barreiras para entrar na área são fortemente reduzidas.
        """
    )

    ax = df.boxplot(
        column=settings.YEARLY_SALARY, by=settings.ED_LEVEL, rot=90
    )
    ax.set_title("Salário por escolaridade")
    st.pyplot(ax.get_figure())

    ax2 = df.boxplot(
        column=settings.YEARLY_SALARY,
        by=settings.ED_LEVEL,
        rot=90,
        showfliers=False,
    )
    ax2.set_title("Salário por escolaridade sem outliers")
    st.pyplot(ax2.get_figure())


def _year_mentalhealth_salary(df: pd.DataFrame) -> None:
    """Combine year with mental health"""
    st.markdown("#### Salário por saúde mental")

    most_significant_level = (
        "I have a concentration and/or memory disorder (e.g. ADHD);"
        "I have autism / an autism spectrum disorder (e.g. Asperger's);"
        "Or, in your own words:"
    )
    st.markdown(
        f"""
        Finalmente, uma combinação talvez um pouco controversa mas curiosa é a
        relação entre o salário e a saúde mental de cada participante. O perfil
        esperado com vários outliers se mantém, como mostrado na primeira
        figura, com uma exceção do nível "{most_significant_level}", que não
        possui dados aberrantes.

        Evitarei tirar qualquer conclusão aqui por não compreender muito bem o
        significado destes itens; porém, é ao menos interessante perceber como
        participantes que se enquadram em determinadas categorias possuem uma
        faixa de salário consiste o suficiente para não apresentar outliers
        como o restante.
        """
    )

    ax = df.boxplot(
        column=settings.YEARLY_SALARY, by=settings.MENTAL_HEALTH, rot=90
    )
    ax.set_title("Salário por saúde mental")
    # Reduce font size
    for item in ax.get_xticklabels():
        item.set_fontsize(5)
    st.pyplot(ax.get_figure())

    ax2 = df.boxplot(
        column=settings.YEARLY_SALARY,
        by=settings.MENTAL_HEALTH,
        rot=90,
        showfliers=False,
    )
    ax2.set_title("Salário por saúde mental sem outliers")
    for item in ax2.get_xticklabels():
        item.set_fontsize(5)
    st.pyplot(ax2.get_figure())
