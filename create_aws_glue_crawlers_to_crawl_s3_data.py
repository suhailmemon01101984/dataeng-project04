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

glue_client.start_crawler(Name='enigma-jhu-crawler')