#1. grant the user: suhailmemon84-admin the role: AmazonAthenaFullAccess
import awswrangler as wr
import pandas as pd
import s3fs

#create fact_covid in s3
df_enigma_jhu=wr.athena.read_sql_query('SELECT fips,province_state as state,country_region as region,confirmed,deaths as death,recovered,active FROM "enigma_jhu"', database="suhailmemon84-dev")
df_rearc_covid_test_states_daily=wr.athena.read_sql_query('SELECT fips,positive,negative,hospitalizedcurrently,hospitalized, hospitalizeddischarged FROM "rearc-covid-19-testing-states_daily"', database="suhailmemon84-dev")
df_fact_covid=df_enigma_jhu.merge(df_rearc_covid_test_states_daily,how="inner",on="fips")
fs = s3fs.S3FileSystem(anon=False)
with fs.open('s3://suhailmemon84-covid-de-project/output/fact_covid.csv', 'w') as f:
    df_fact_covid.to_csv(f)


#create dimension_hospital in s3
df_rearc_usa_hospital_beds=wr.athena.read_sql_query('SELECT fips,state_name as state,latitude as hos_lat,longtitude as hos_lang,hq_address,hospital_type,hospital_name,hq_city,hq_state FROM "rearc_usa_hospital_beds"', database="suhailmemon84-dev")
fs = s3fs.S3FileSystem(anon=False)
with fs.open('s3://suhailmemon84-covid-de-project/output/dimension_hospital.csv', 'w') as f:
    df_rearc_usa_hospital_beds.to_csv(f)


#create dimension_region in s3
df_dim_region=wr.athena.read_sql_query('SELECT "enigma_jhu".fips,province_state as state,country_region as region,latitude as lat,longitude as lang,county,state as state_abb FROM "enigma_jhu" join "enigma-nytimes-us_county" on "enigma_jhu".fips="enigma-nytimes-us_county".fips', database="suhailmemon84-dev")
fs = s3fs.S3FileSystem(anon=False)
with fs.open('s3://suhailmemon84-covid-de-project/output/dimension_region.csv', 'w') as f:
    df_dim_region.to_csv(f)


#create dimension_date in s3
df_dim_date=wr.athena.read_sql_query('SELECT fips,date FROM "rearc-covid-19-testing-states_daily"', database="suhailmemon84-dev")
df_dim_date['date']=pd.to_datetime(df_dim_date['date'], format='%Y%m%d')
df_dim_date['month'] = pd.DatetimeIndex(df_dim_date['date']).month
df_dim_date['year'] = pd.DatetimeIndex(df_dim_date['date']).year
df_dim_date['dayofweek'] = pd.DatetimeIndex(df_dim_date['date']).dayofweek
df_dim_date['is_weekend'] = df_dim_date['dayofweek']>4
fs = s3fs.S3FileSystem(anon=False)
with fs.open('s3://suhailmemon84-covid-de-project/output/dimension_date.csv', 'w') as f:
    df_dim_date.to_csv(f)
