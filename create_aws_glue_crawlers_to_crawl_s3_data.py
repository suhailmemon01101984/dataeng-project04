#####before running this code you need to make sure of the following things:
#1. create the role suhailmemon84-glue-s3-glue-access in aws console for service: aws glue and give it s3fullaccess, glueconsolefullaccess and glueservicerole
#2. grant the user: suhailmemon84-admin the role: s3fullaccess and glueconsolefullaccess plus this inline policy to allow the user to pass roles
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "Statement1",
#             "Effect": "Allow",
#             "Action": [
#                 "iam:GetRole",
#                 "iam:PassRole"
#             ],
#             "Resource": [
#                 "arn:aws:iam::236765750193:role/suhailmemon84-glue-s3-glue-access"
#             ]
#         }
#     ]
# }
#3. finally go under s3 and create a bucket: s3://suhailmemon84-athena-output-location/ and plug this bucket path on aws athena --> query editor --> settings.
# aws athena will use the above bucket to output the results of whatever queries you run on athena
#4. go to aws console --> aws glue --> data catalog-->databases --> add database --> create the database: suhailmemon84-dev. this is the database
# which the crawler will use to create the tables under after it's crawling is complete
#5. once you run this code, go to https://us-east-1.console.aws.amazon.com/glue/home?region=us-east-1#/v2/data-catalog/crawlers and monitor
# your crawler and once it complets, go to aws athena --> query editor and verify under the database: suhailmemon84-dev to ensure your tables are created properly by the crawler


import boto3
glue_client=boto3.client('glue')

glue_client.create_crawler(
    Name='enigma-jhu-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/enigma-jhu'
            }
        ]
    }

)

glue_client.create_crawler(
    Name='enigma-nytimes-us-county-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='enigma-nytimes-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/enigma-nytimes-data-in-usa/csv/us_county'
            }
        ]
    }

)

glue_client.create_crawler(
    Name='enigma-nytimes-us-states-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='enigma-nytimes-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/enigma-nytimes-data-in-usa/csv/us_states'
            }
        ]
    }

)


glue_client.create_crawler(
    Name='rearc-covid-19-testing-states-daily-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='rearc-covid-19-testing-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/rearc-covid-19-testing-data/csv/states_daily'
            }
        ]
    }

)

glue_client.create_crawler(
    Name='rearc-covid-19-testing-us-daily-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='rearc-covid-19-testing-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/rearc-covid-19-testing-data/csv/us_daily'
            }
        ]
    }

)

glue_client.create_crawler(
    Name='rearc-covid-19-testing-us-total-latest-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='rearc-covid-19-testing-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/rearc-covid-19-testing-data/csv/us-total-latest'
            }
        ]
    }

)


glue_client.create_crawler(
    Name='rearc-usa-hospital-beds-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/rearc-usa-hospital-beds'
            }
        ]
    }

)

glue_client.create_crawler(
    Name='static-datasets-countrycode-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='static-datasets-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/static-datasets/csv/countrycode'
            }
        ]
    }

)

glue_client.create_crawler(
    Name='static-datasets-countypopulation-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='static-datasets-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/static-datasets/csv/CountyPopulation'
            }
        ]
    }

)


glue_client.create_crawler(
    Name='static-datasets-stateabv-crawler',
    Role='suhailmemon84-glue-s3-glue-access',
    DatabaseName='suhailmemon84-dev',
    TablePrefix='static-datasets-',
    Targets=
    {
        'S3Targets':
        [
            {
                'Path':'s3://suhailmemon84-covid-de-project/static-datasets/csv/state-abv'
            }
        ]
    }

)


glue_client.start_crawler(Name='enigma-jhu-crawler')
glue_client.start_crawler(Name='enigma-nytimes-us-county-crawler')
glue_client.start_crawler(Name='enigma-nytimes-us-states-crawler')
glue_client.start_crawler(Name='rearc-covid-19-testing-states-daily-crawler')
glue_client.start_crawler(Name='rearc-covid-19-testing-us-daily-crawler')
glue_client.start_crawler(Name='rearc-covid-19-testing-us-total-latest-crawler')
glue_client.start_crawler(Name='rearc-usa-hospital-beds-crawler')
glue_client.start_crawler(Name='static-datasets-countrycode-crawler')
glue_client.start_crawler(Name='static-datasets-countypopulation-crawler')
glue_client.start_crawler(Name='static-datasets-stateabv-crawler')