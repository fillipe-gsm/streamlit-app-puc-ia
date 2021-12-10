import pandas as pd
import pytest
from config import settings


@pytest.fixture
def df_data():
    return pd.read_csv(settings.data_file)
