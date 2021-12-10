from streamlit_stackoverflow import introduction


def test_introduction_section(df_data):
    """Just ensure no errors are raised :("""
    introduction.introduction_section(df_data)
