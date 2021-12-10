from config import settings

from streamlit_stackoverflow import data_handling


def test_preprocess_data():
    df = data_handling.preprocess_data()

    # Assert no ED_LEVEL has NaN
    mask = df[settings.ED_LEVEL].isna()
    assert mask.sum() == 0

    # Assert no AGE has NaN
    mask = df[settings.AGE].isna()
    assert mask.sum() == 0

    # Assert no YEARS_CODE has NaN
    mask = df[settings.YEARS_CODE].isna()
    assert mask.sum() == 0

    # Assert no YEARS_CODE_PRO has NaN
    mask = df[settings.YEARS_CODE_PRO].isna()
    assert mask.sum() == 0

    # Assert no EMPLOYMENT has NaN
    mask = df[settings.EMPLOYMENT].isna()
    assert mask.sum() == 0

    # Assert no EMPLOYMENT has NaN
    mask = df[settings.EMPLOYMENT].isna()
    assert mask.sum() == 0

    # Assert no USED_LANGUAGES has NaN
    mask = df[settings.USED_LANGUAGES].isna()
    assert mask.sum() == 0

    # Assert no DESIRED_LANGUAGES has NaN
    mask = df[settings.DESIRED_LANGUAGES].isna()
    assert mask.sum() == 0

    # Assert no MENTAL_HEALTH has NaN
    mask = df[settings.MENTAL_HEALTH].isna()
    assert mask.sum() == 0

    import ipdb; ipdb.set_trace()
