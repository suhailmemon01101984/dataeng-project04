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

cursor.execute("""\
create table if not exists dev.public.category(
catid integer not null,
catgroup varchar(10),
catname varchar(10),
catdesc varchar(50),
primary key(catid)
)
distkey(catid)""")

cursor.close()
conn.close()
