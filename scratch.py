#2. grant the user: suhailmemon84-admin the role: AmazonAthenaFullAccess
import awswrangler as wr
import pandas as pd
import s3fs

df1=wr.athena.read_sql_query('SELECT fips,province_state as state,country_region as region,confirmed,deaths as death,recovered,active FROM "enigma_jhu"', database="suhailmemon84-dev")
#print(df1)

df2=wr.athena.read_sql_query('SELECT fips,positive,negative,hospitalizedcurrently,hospitalized, hospitalizeddischarged FROM "rearc-covid-19-testing-states_daily"', database="suhailmemon84-dev")
#print(df2)

fact_covid_df=df1.merge(df2,how="inner",on="fips")
#print(fact_covid_df)


fs = s3fs.S3FileSystem(anon=False)
with fs.open('s3://suhailmemon84-covid-de-project/output/fact_covid.csv', 'w') as f:
    fact_covid_df.to_csv(f)
