import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://@localhost:5432/Test')


# Load dataframe
def dataframe():
    comments_df = pd.read_pickle("../Sentiment Analysis/comments_with_textblob_dvader_df.pkl")
    return comments_df


if __name__ == '__main__':
    df = dataframe()
    # df = df.head()
    df.to_sql('data', engine, if_exists='replace')
    print("Process completed")
#%%
