import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from config import settings

from streamlit_stackoverflow.single_dimensional_analysis import (
    bar_plot, pie_plot
)


NUM_COUNTRIES = 5


def multi_dimensional_section(df: pd.DataFrame) -> None:
    """Plots and analyses with multiple variable"""
    st.header("Análise multidimensional")
    st.markdown(
        """
        Esta seção concentra resultados envolvendo mais de uma variável.
        """
    )

    _salary_analyses(df)
    _professional_analyses(df)
    _python_analyses(df)


def _salary_analyses(df_raw: pd.DataFrame) -> None:
    """Year salary analysis"""

    st.subheader("Salário anual convertido")

    # Remove NaN salaries as they are useless to us
    df = df_raw[~df_raw[settings.YEARLY_SALARY].isna()]
    _salary_age(df)
    _salary_edlevel(df)
    _salary_country(df)
    _salary_mentalhealth(df)


def _salary_age(df: pd.DataFrame) -> None:
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


def _salary_edlevel(df: pd.DataFrame) -> None:
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


def _salary_country(df: pd.DataFrame) -> None:
    """Combine year salary with country"""
    st.markdown("#### Salário por país")
    st.markdown(
        f"""
        Conforme visto na primeira seção, há muitos países disponíveis, e assim
        visualizar as faixas salarias em cada um traria mais ruído que
        informação. Sendo assim, vamos focar nos {NUM_COUNTRIES} países que
        mais responderam às pesquisas.

        Seguindo o padrão nas outras sub-seções, os numerosos outliers
        dificultam a análise, e por isso podemos concentrar a atenção no painel
        seguinte. A tendência central parece indicar que os Estados Unidos
        apresentam níveis de salários mais elevados, apesar de que com a alta
        variabilidade apenas com um teste de hipóteses poderíamos confirmar
        isso. Por outro lado, apenas esta análise visual indica que os salários
        na Índia são significativamente mais baixos que nos outros países.
        """
    )

    # Group data by country
    df_most_common_countries = _get_data_most_common_countries(df)

    # Plot boxplots
    ax = df_most_common_countries.boxplot(
        column=settings.YEARLY_SALARY, by=settings.COUNTRY, rot=90
    )
    ax.set_title(f"Salário nos {NUM_COUNTRIES} países mais respondidos")
    st.pyplot(ax.get_figure())

    ax2 = df_most_common_countries.boxplot(
        column=settings.YEARLY_SALARY,
        by=settings.COUNTRY,
        rot=90,
        showfliers=False,
    )
    ax2.set_title(f"Salário nos {NUM_COUNTRIES} países sem outliers")
    st.pyplot(ax2.get_figure())



def _salary_mentalhealth(df: pd.DataFrame) -> None:
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


def _professional_analyses(df_raw: pd.DataFrame) -> None:
    """Analyses of professional people"""

    st.subheader("Análise de pessoas com trabalho profissional")

    st.markdown(
        """
        Como visto na primeira seção, mais de 60% dos participantes está
        empregado em um _full time_ job. Vamos nos aprofundar um pouco nesta
        categoria.
        """
    )

    df = df_raw[df_raw[settings.EMPLOYMENT] == settings.EMPLOYED_FULL_TIME]

    _professional_and_edlevel(df)
    _professional_and_companysize(df)


def _professional_and_edlevel(df: pd.DataFrame) -> None:
    """Relationship of education level with professional people"""

    st.markdown("#### Níveis de escolaridade")
    st.markdown(
        """
        Dentre as pessoas com full-time job, vemos que quase a metade possui
        graduação, e este número é seguido de mestres. O perfil se mantém o
        mesmo quando consideramos todas as pessoas, como mostrado na primeira
        seção.
        """
    )

    df_group = df.groupby(by=settings.ED_LEVEL).size().sort_values()

    bar_plot(
        df_group,
        title="Participantes com full-time job por Escolaridade",
    )
    pie_plot(
        df_group,
        title=(
            "Porcentagem de participantes com full-time job por Escolaridade"
        ),
    )


def _professional_and_companysize(df: pd.DataFrame) -> None:
    """Relationship of company size with professional people"""

    st.markdown("#### Tamanho da empresa")
    st.markdown(
        """
        Vemos nos gráficos a seguir que a maior parte dos participantes com
        trabalho _full-time_ estão ou em empresas com 20 a 500 funcionários, e
        em terceiro lugar há um salto para companhias enormes, com mais de dez
        mil pessoas. A minoria trabalha sozinho ou não sabe o tamanho de suas
        companhias.
        """
    )

    df_group = df.groupby(by=settings.ORG_SIZE).size().sort_values()

    bar_plot(
        df_group,
        title="Tamanho da empresa de participantes com full-time job",
    )
    pie_plot(
        df_group,
        title=(
            "Porcentagem do tamanho da empresa por participante com full-time"
            "job"
        ),
    )


def _python_analyses(df_raw: pd.DataFrame) -> None:
    """Analyses including people that work with Python"""
    st.subheader("Análise de programadores em Python")

    st.markdown(
        """
        Nesta última seção vamos investigar um pouco mais no grupo de
        participantes que programam em Python.
        """
    )

    _python_opsys(df_raw)
    _python_salary_global(df_raw)
    _python_salary_brazil(df_raw)
    _python_salary_most_common_countries(df_raw)


def _python_salary_global(df: pd.DataFrame) -> None:
    """Salary of Python developers"""
    st.markdown("#### Faixa de salário dentre programadores de Python")
    st.markdown(
        """
        Considerando todos participantes, o boxplot a seguir compara as faixas
        salariais entre programadores que trabalham ou não com Python. Por
        comodidade, já removemos os outliers uma vez que eles obstruem este
        tipo de análise.

        Como se vê, não parece haver diferença significativa entre os grupos, o
        que é um bom indicativo de que independente da linguagem escolhida é
        possível prosperar nesta área.
        """
    )

    mask = df[settings.USED_LANGUAGES].str.contains("Python")
    df[settings.USE_PYTHON] = False
    df[settings.USE_PYTHON][mask] = True

    ax = df.boxplot(
        column=settings.YEARLY_SALARY,
        by=settings.USE_PYTHON,
        rot=90,
        showfliers=False,
    )
    ax.set_title(
        "Comparação de salários entre quem trabalha ou não com Python"
    )
    st.pyplot(ax.get_figure())


def _python_salary_brazil(df: pd.DataFrame) -> None:
    """Salary of Python developers in Brazil"""
    st.markdown(
        """
        Focando a análise no Brasil, podemos tomar a mesma conclusão anterior.
        Porém, há um adendo importante: nossa faixa salarial é extremamente
        menor. Na seção anterior, vimos que os EUA possuem um salário mediano
        de cerca de 130 mil dólares por ano, os outros países estão em 80 mil,
        enquanto a Índia paga os funcionários menos de 30 mil tipicamente.
        Nossa faixa salarial encontra-se próxima, senão menor, que a da Índia.
        """
    )

    df_brazil = df[df[settings.COUNTRY] == settings.BRAZIL]
    mask = df_brazil[settings.USED_LANGUAGES].str.contains("Python")
    df_brazil[settings.USE_PYTHON] = False
    df_brazil[settings.USE_PYTHON][mask] = True

    ax = df_brazil.boxplot(
        column=settings.YEARLY_SALARY,
        by=settings.USE_PYTHON,
        rot=90,
        showfliers=False,
    )
    ax.set_title(
        "Comparação de salários brasileiros entre quem trabalha ou não com "
        "Python"
    )
    st.pyplot(ax.get_figure())


def _python_salary_most_common_countries(df: pd.DataFrame) -> None:
    """Salary of Python developers in most common countries"""
    st.markdown(
        """
        Vamos repetir a análise anterior para os países que mais responderam.
        Como se vê, podemos tomar a mesma conclusão. Não parece haver diferença
        significativa nos salários em nenhum dos seis países considerados
        (contando o Brasil) com respeito a usar ou não Python.
        """
    )

    df_most_common_countries = _get_data_most_common_countries(df)
    mask = df_most_common_countries[
        settings.USED_LANGUAGES
    ].str.contains("Python")
    df_most_common_countries[settings.USE_PYTHON] = False
    df_most_common_countries[settings.USE_PYTHON][mask] = True

    ax = df_most_common_countries.boxplot(
        column=settings.YEARLY_SALARY,
        by=[settings.COUNTRY, settings.USE_PYTHON],
        rot=90,
        showfliers=False,
    )
    ax.set_title(
        "Comparação de salários dos países mais respondidos entre quem "
        "trabalha ou não com Python"
    )
    st.pyplot(ax.get_figure())


def _python_opsys(df_raw: pd.DataFrame) -> None:
    """OS used by Python developers"""

    st.markdown("#### Sistema operacional usado entre programadores de Python")
    st.markdown(
        """
        Vemos abaixo que Windows é o sistema mais popular dentro programadores
        Python (40,2%), seguido de sistemas baseados em Linux (32,5%). Esta
        resposta pode ser um tanto quanto surpreendente, uma vez que é comum
        pensar que programadores tendem a preferir Linux. Sistemas baseados em
        BSD costumam ser mais usados em servidores, então o baixo número neste
        caso parece fazer sentido.
        """
    )
    df = df_raw[df_raw[settings.USED_LANGUAGES].str.contains("Python")]

    df_group = df.groupby(by=settings.OP_SYS).size().sort_values()
    bar_plot(
        df_group,
        title="Sistema Operacional de Programadores Python",
    )
    pie_plot(
        df_group,
        title="Porcentagem de Sistema Operacional de Programadores Python",
    )


def _get_data_most_common_countries(df: pd.DataFrame) -> pd.DataFrame:
    """Get a dataframe with only the most answered countries"""
    df_group = df.groupby(by=settings.COUNTRY).size().sort_values()
    most_common_countries = df_group.keys()[-NUM_COUNTRIES:]
    return df[
        df[settings.COUNTRY].isin(most_common_countries)
    ]
