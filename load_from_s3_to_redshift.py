###pre requisite: login to aws console and go under roles and created the custom role: suhailmemon84-reshift-s3-readonly-access. also attach the policy: AmazonS3ReadOnlyAccess to this role
###this role allows redshift read access to s3 via the attached policy: AmazonS3ReadOnlyAccess
###explanation as to why a role is needed here: https://medium.com/@lucadefra92/stage-data-from-s3-to-redshift-a6c8f80e3b7
### once you have the role get the role arn. in my case it was-> arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access
#### then associate redshift with the role you created. go under redshift click your name space --> security & encryption --> associate iam role --> associate the role you created above with redshift and save

import redshift_connector
conn = redshift_connector.connect(
     host='default-workgroup.236765750193.us-west-1.redshift-serverless.amazonaws.com',
     database='dev',
     port=5439,
     user='suhailmemon84-admin',
     password='mypwd123'
  )
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("truncate table dev.public.dimension_date")
#copy command. specify region where the bucket is since bucket region is different from redshift region. also set ignoreheader to 1 to make sure it ignores the header before loading
cursor.execute("copy dev.public.dimension_date from 's3://suhailmemon84-covid-de-project/output/dimension_date.csv' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' REGION 'us-east-1' IGNOREHEADER 1 delimiter ',';")


cursor.execute("truncate table dev.public.dimension_hospital")
#copy command. specify region where the bucket is since bucket region is different from redshift region. also set ignoreheader to 1 to make sure it ignores the header before loading
cursor.execute("copy dev.public.dimension_hospital from 's3://suhailmemon84-covid-de-project/output/dimension_hospital.csv' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' REGION 'us-east-1' IGNOREHEADER 1 delimiter ',';")


cursor.execute("truncate table dev.public.fact_covid")
#copy command. specify region where the bucket is since bucket region is different from redshift region. also set ignoreheader to 1 to make sure it ignores the header before loading
cursor.execute("copy dev.public.fact_covid from 's3://suhailmemon84-covid-de-project/output/fact_covid.csv' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' REGION 'us-east-1' IGNOREHEADER 1 delimiter ',';")

cursor.execute("truncate table dev.public.dimension_region")
#copy command. specify region where the bucket is since bucket region is different from redshift region. also set ignoreheader to 1 to make sure it ignores the header before loading
cursor.execute("copy dev.public.dimension_region from 's3://suhailmemon84-covid-de-project/output/dimension_region.csv' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' REGION 'us-east-1' IGNOREHEADER 1 delimiter ',';")


cursor.close()
conn.close()
