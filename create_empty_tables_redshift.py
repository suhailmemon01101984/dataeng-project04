#had to choose new redshift coz my previous trial had expired. this time, the new redshift in region: us-west-1
#first had to go under vpcs and create 3 subnets. used this link to get the ip ranges for each of the subnet: https://www.davidc.net/sites/default/subnets/subnets.html
#then launch amazon redshift with all defaults.
#then go under your default-namespace --> actions --> edit admin credentials --> check the box for customize admin user creds --> input username as suhailmemon84-admin and choose
#manually add the admin pwd and put in the password you want.
#use query data functionality and connect with the admin username and password to make sure you can connect
#go into security groups and add an inbound rule to allow all inbound traffic at this link: https://us-west-1.console.aws.amazon.com/ec2/home?region=us-west-1#SecurityGroups
#inbound rule should be: all tcp traffic, source: custom, put 0.0.0.0/0 in the search bar
#go into redshift serverless under your default workgroup: https://us-west-1.console.aws.amazon.com/redshiftv2/home?region=us-west-1#serverless-workgroup?workgroup=default-workgroup
#and turn Publicly accessible to ON


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

####create empty tables

cursor.execute("""drop table if exists dev.public.dimension_date""")
cursor.execute("""drop table if exists dev.public.dimension_hospital""")
cursor.execute("""drop table if exists dev.public.fact_covid""")
cursor.execute("""drop table if exists dev.public.dimension_region""")

cursor.execute("""\
create table if not exists dev.public.dimension_date(
index integer not null,
fips integer not null,
date date not null,
month integer not null,
year integer not null,
dayofweek integer not null,
is_weekend varchar(5) not null,
primary key(index)
)
distkey(date)""")


cursor.execute("""\
create table if not exists dev.public.dimension_hospital(
index integer not null,
fips integer,
state varchar(100) not null,
hos_lat float not null,
hos_lang float not null,
hq_address varchar(2000) not null,
hospital_type varchar(200) not null,
hospital_name varchar(1000) not null,
hq_city varchar(100) not null,
hq_state varchar(100) not null,
primary key(index)
)
distkey(fips)""")


cursor.execute("""\
create table if not exists dev.public.fact_covid(
index integer not null,
fips integer not null,
state varchar(100) not null,
region varchar(100) not null,
confirmed integer,
death integer,
recovered integer,
active integer,
positive integer,
negative integer,
hospitalizedcurrently integer,
hospitalized integer,
hospitalizeddischarged integer,
primary key(index)
)
distkey(index)""")



cursor.execute("""\
create table if not exists dev.public.dimension_region(
index integer,
fips integer,
state varchar(100),
region varchar(100),
lat float,
lang float,
county varchar(100),
state_abb varchar(100),
primary key(index)
)
distkey(index)""")

cursor.close()
conn.close()
