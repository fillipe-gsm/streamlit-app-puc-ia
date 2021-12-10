"""Preprocess data before presenting it"""
import pandas as pd
from config import settings


def preprocess_data() -> pd.DataFrame:
    """Remove NaN and other important stuff"""
    df = pd.read_csv(settings.data_file)

    _override_nas(df, column=settings.ED_LEVEL)
    _override_nas(df, column=settings.AGE)
    _override_nas(df, column=settings.YEARS_CODE)
    _override_nas(df, column=settings.YEARS_CODE_PRO)
    _override_nas(df, column=settings.EMPLOYMENT)
    _override_nas(df, column=settings.US_STATE)
    _override_nas(df, column=settings.USED_LANGUAGES)
    _override_nas(df, column=settings.DESIRED_LANGUAGES)
    _override_nas(df, column=settings.MENTAL_HEALTH)
    _override_nas(df, column=settings.ORG_SIZE)
    _override_nas(df, column=settings.OP_SYS)

    return df


def _override_nas(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column][df[column].isna()] = settings.default_str_nan
