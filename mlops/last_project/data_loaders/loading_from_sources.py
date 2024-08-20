import requests
from io import BytesIO
from typing import List

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:
    dfs: List[pd.DataFrame] = []
    year= 2024
    months_range=(1,2)
    type_of_taxi="green"

    file_name=f"{type_of_taxi}-{year}-{months_range[0]}-{months_range[1]}.pq"
    ## Here you can specify the range of the data you need to concat all datasets into one
    for year, months in [(year, months_range)]:
        for i in range(*months):
            response = requests.get(
                f'https://github.com/mage-ai/datasets/raw/master/taxi/{type_of_taxi}'
                f'/{year}/{i:02d}.parquet'
            )

            if response.status_code != 200:
                raise Exception(response.text)

            df = pd.read_parquet(BytesIO(response.content))
            dfs.append(df)

    return pd.concat(dfs), file_name
