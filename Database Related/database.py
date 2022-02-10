import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://@localhost:5432/Test')
azure_engine = create_engine('postgresql://tsuihoiming:Qw645987321@fyp-psql.postgres.database.azure.com/Development'
                             '?sslmode=require')


# Load dataframe
def dataframe():
    df = pd.read_pickle("../Pickles/list.pkl")
    return df


if __name__ == '__main__':
    res_df = dataframe()
    # df = df.head()
    res_df.to_sql('reddit_community_distribution', azure_engine, if_exists='replace')
    print("Process completed")
# %%
