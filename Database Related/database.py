import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://@localhost:5432/Test')
azure_engine = create_engine(
    'postgresql://tsuihoiming:r*x93Rd6ZVxXgccpwgvyr&4mXRo!Pb@fyp-psql.postgres.database.azure.com/Development'
    '?sslmode=require')


# Load dataframe
def dataframe():
    df = pd.read_pickle("/Users/isaac/DataSpell-EAP Projects/Reddit Data/term_document_matrix.pkl")
    return df


if __name__ == '__main__':
    res_df = dataframe()
    # df = df.head()
    res_df.to_sql('term_document_matrix', azure_engine, if_exists='replace')
    print("Process completed")
# %%
