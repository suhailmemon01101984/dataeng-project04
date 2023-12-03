import boto3

s3=boto3.resource('s3')
srcbucket=s3.Bucket('covid19-lake')
keys=[]

for obj in srcbucket.objects.filter(Prefix='enigma-jhu/'):
    #print(obj.key)
    copy_source={'Bucket':'covid19-lake','Key':obj.key}
    destbucket=s3.Bucket('suhailmemon84-covid-de-project')
    destbucket.copy(copy_source,obj.key)
    print(obj.key + '- File Copied')


for obj in srcbucket.objects.filter(Prefix='enigma-nytimes-data-in-usa/'):
    #print(obj.key)
    copy_source={'Bucket':'covid19-lake','Key':obj.key}
    destbucket=s3.Bucket('suhailmemon84-covid-de-project')
    destbucket.copy(copy_source,obj.key)
    print(obj.key + '- File Copied')

for obj in srcbucket.objects.filter(Prefix='rearc-covid-19-testing-data/'):
    #print(obj.key)
    copy_source={'Bucket':'covid19-lake','Key':obj.key}
    destbucket=s3.Bucket('suhailmemon84-covid-de-project')
    destbucket.copy(copy_source,obj.key)
    print(obj.key + '- File Copied')

for obj in srcbucket.objects.filter(Prefix='rearc-usa-hospital-beds/'):
    #print(obj.key)
    copy_source={'Bucket':'covid19-lake','Key':obj.key}
    destbucket=s3.Bucket('suhailmemon84-covid-de-project')
    destbucket.copy(copy_source,obj.key)
    print(obj.key + '- File Copied')

for obj in srcbucket.objects.filter(Prefix='static-datasets/'):
    #print(obj.key)
    copy_source={'Bucket':'covid19-lake','Key':obj.key}
    destbucket=s3.Bucket('suhailmemon84-covid-de-project')
    destbucket.copy(copy_source,obj.key)
    print(obj.key + '- File Copied')
