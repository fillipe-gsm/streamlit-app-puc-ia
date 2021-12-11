"""Analyses on a single variable"""
from typing import Callable, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from config import settings


def single_dimensional_section(df: pd.DataFrame) -> None:
    """Plots and analyses with only variable"""
    st.header("Análise unidimensional")
    st.markdown(
        """
        Esta seção apresenta resultados focando em apenas umas variável por
        vez.
        """
    )

    _education_levels(df)
    _years_code(df)
    _employment(df)
    _country(df)
    _languages(df)


def _education_levels(df: pd.DataFrame) -> None:
    """Education levels analyses"""

    st.subheader("Nível de escolaridade")
    # Show education levels
    ed_levels = df[settings.ED_LEVEL].unique()
    st.markdown(
        f"""
        Há um total de {ed_levels.size} níveis, sendo eles:
        """
    )
    ed_leves_str = "\n".join(f"- {ed_level}" for ed_level in ed_levels)
    st.markdown(ed_leves_str)

    # Plot bar chart
    st.markdown(
        """
        O painel abaixo mostra a quantidade de participantes para cada nível,
        seguido do percentual no gráfico de pizza.
        Como se vê, a maior parte das pessoas possui graduação completa,
        correspondendo a cerca de 42,4% do total, seguido de um mestrado
        completo, representando 21%.

        Como se vê, poucas pessoas ou deixaram este campo em branco ou possuíam
        um nível diferente dos disponíveis, totalizando 1914 ou 2,3%.
        """
    )

    df_group = df.groupby(by=settings.ED_LEVEL).size().sort_values()
    bar_plot(
        df_group,
        title="Participantes por Nível de Escolaridade",
    )

    pie_plot(
        df_group,
        title="Porcentagem de participantes por Nível de Escolaridade",
    )


def _years_code(df: pd.DataFrame) -> None:
    """Years of code analyses"""

    st.subheader("Tempo de programação")

    # Years of code
    st.markdown(
        """
        O gráfico abaixo indica que os grupos de pessoas que mais aparecem
        têm 5 ou 10 anos de prática. Em contrapartida, participantes com mais
        de 40 anos de programação são mais raros.

        Apesar disso, é interessante ver como há pessoas que provavelmente
        iniciaram esta vida sem as vantagens da internet e linguagens mais
        "simples" continuam ativas no site.
        """
    )

    df_group = df.groupby(by=settings.YEARS_CODE).size().sort_values()

    bar_plot(
        df_group,
        title="Participantes por tempo de programação",
        callback=_reduce_font_size,
    )

    # Years of code pro
    st.markdown(
        """
        Quando consideramos tempo de prática profissional (provavelmente em
        empresas ou universidades), o quadro permanece similar com exceção de
        que a esmagadora maior parte dos participantes não forneceu seus dados.
        É possível que grande parte não esteja trabalhando
        profissionalmente ainda, ou que talvez a definição de "pro" não estava
        clara, ou que simplesmente esqueceram-se de preencher este dado.

        Excluindo esta parte, podemos ver, como antes, que a maior parte dos
        participantes possui menos de 10 anos de experiência profissional,
        enquanto minoria está no outro extremo com mais de 40 anos.
        """
    )

    df_group2 = df.groupby(by=settings.YEARS_CODE_PRO).size().sort_values()

    bar_plot(
        df_group2,
        title="Participantes por tempo de programação profissional",
        callback=_reduce_font_size,
    )


def _employment(df: pd.DataFrame) -> None:
    """Employment analysis"""

    st.subheader("Empregabilidade")

    st.markdown(
        r"""
        A maior parte dos participantes possui um emprego "regular", quer
        dizer, _full time_, ocupando 64,2% das observações. Isto é seguido de
        estudantes (14,1%), e possivelmente quase todos em algum curso de
        pós-graduação, comparando com o gráfico da primeira seção.

        Menos de 3% dos participantes está nas 4 categorias à esquerda do
        gráfico, que podemos agrupar como "pessoas programando por hobby
        apenas".
        """
    )

    df_group = df.groupby(by=settings.EMPLOYMENT).size().sort_values()

    bar_plot(
        df_group,
        title="Participantes por tipo de empregabilidade",
    )

    pie_plot(
        df_group,
        title="Porcentagem de participantes por tipo de empregabilidade",
    )


def _country(df: pd.DataFrame) -> None:
    """Country analysis"""

    st.subheader("País")

    df_group = df.groupby(by=settings.COUNTRY).size().sort_values()
    st.markdown(
        f"""
        Determinar a quantidade de pessoas por país que respondeu à pesquisa
        pode ser complicado, uma vez que há um total de {df_group.size} países.

        Contudo, é possível ver que a maior parte das respostas envolve pessoas
        dos Estados Unidos (~18%), seguido da Índia (~13%).
        """
    )

    bar_plot(
        df_group,
        title="Participantes por País",
        callback=_reduce_font_size,
    )

    st.markdown(
        """
        Podemos então focar nos Estados Unidos. O gráfico abaixo mostra a
        distribuição de participantes por estado, excluindo os resultados sem
        resposta, o que provavelmente seria de pessoas fora dos EUA que
        decidiram não responder.

        Neste caso, a maior parte das pessoas reside na Califórnia e a minoria
        em _American Samoa_. O fato de o _Silicon Valley_ estar localizado
        neste estado pode ter relação com este número maior, mas seria
        necessário outro estudo para confirmar algum tipo de causa ou outro
        possível fator.
        """
    )

    # Group by state but removing the NaN
    df_group2 = df.groupby(by=settings.US_STATE).size().sort_values()
    df_group2.pop(settings.default_str_nan)
    bar_plot(
        df_group2,
        title="Participantes por estado nos Estados Unidos",
        callback=_reduce_font_size,
    )

    pie_plot(
        df_group2,
        title="Porcentagem de participantes por estado nos Estados Unidos",
    )


def _languages(df: pd.DataFrame) -> None:
    """Language analysis"""

    st.subheader("Linguages de Programação")

    st.markdown(
        """
        Com respeito a linguagens de programação trabalhadas, cada
        participantes possui uma lista de itens, e assim seria muito complicada
        uma análise individual.

        Uma vez que o curso focou na linguagem Python, vamos também nos
        concentrar nela. Como vemos no gráfico abaixo, quase metade dos
        participantes trabalha com Python, o que reforça sua popularidade.
        """
    )

    mask = df[settings.USED_LANGUAGES].str.contains("Python")

    pie_values = [mask.sum(), (~mask).sum()]  # use Python, do not use Python
    pie_labels = ["Python", "Other languages"]
    fig, ax = plt.subplots()
    ax.pie(
        pie_values,
        labels=pie_labels,
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title("Participantes que trabalham com Python")
    st.pyplot(fig)

    st.markdown(
        """
        Uma informação interessante consiste nas linguagens com as quais os
        participantes _gostariam_ de trabalhar. Segundo o gráfico abaixo, este
        número é levemente menor, mas ainda significativo. Aliada à conclusão
        anterior, isto também reforça a prospecção de que Python continuará
        sendo relevante no futuro.
        """
    )

    mask2 = df[settings.DESIRED_LANGUAGES].str.contains("Python")

    pie_values2 = [mask2.sum(), (~mask2).sum()]  # want Python, do not want it
    pie_labels2 = ["Python", "Other languages"]
    fig2, ax2 = plt.subplots()
    ax2.pie(
        pie_values2,
        labels=pie_labels2,
        autopct="%1.1f%%",
        startangle=90,
    )
    ax2.set_title("Participantes que querem trabalhar com Python")
    st.pyplot(fig2)


def bar_plot(
    df_group: pd.DataFrame, title: str, callback: Optional[Callable] = None
):
    """Creat a bar plot grouping data by specific column"""
    fig, ax = plt.subplots()
    ax.bar(df_group.keys(), df_group.values)
    ax.set_title(title)
    ax.set_xticklabels(labels=df_group.keys(), rotation=90)

    if callback:
        callback(ax)

    st.pyplot(fig)


def pie_plot(df_group: pd.DataFrame, title: str):
    """Create a pie plot"""
    fig, ax = plt.subplots()
    ax.pie(
        df_group.values,
        labels=df_group.keys(),
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title(title)
    st.pyplot(fig)


def _reduce_font_size(ax, font_size: int = 5):
    """Callback to reduce xlabel font size"""
    for item in ax.get_xticklabels():
        item.set_fontsize(font_size)
