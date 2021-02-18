import boto3
client = boto3.client('s3')
s3_resource = boto3.resource('s3')

for buckets in s3_resource.buckets.all():
    if buckets.name[:5]=='techh':
        bucket_name = buckets.name
#    else:
#       bucket_name = ' '

print("Bucket_name:",bucket_name)

for list in client.list_objects(Bucket=bucket_name)['Contents']:

    print(list)
    s3_object = list['Key']
    print(s3_object)

#for s3_object in bucket_name.objects.all():
#    print(s3_object)
#bucket_name = client.getobject["Records"][0]["s3"]["bucket"]["name"]
#s3_file_name = client.getobject["Records"][0]["s3"]["object"]["key"]
#resp = client.get_object(Bucket=bucket_name, Key=s3_file_name)

#print(resp)
