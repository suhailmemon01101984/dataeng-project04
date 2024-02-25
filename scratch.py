#2. grant the user: suhailmemon84-admin the role: AmazonAthenaFullAccess
import awswrangler as wr
import pandas as pd

df=wr.athena.read_sql_query('SELECT * FROM "static-datasets-state_abv" limit 10', database="suhailmemon84-dev")
print(df)
