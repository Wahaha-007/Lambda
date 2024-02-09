'''
# Code the see boto3 help
import boto3
s3_client = boto3.client('s3')
help(s3_client.get_object )
'''
import boto3
from  botocore.errorfactory import ClientError

s3_client = boto3.client('s3')

'''
# 1. Test code for bookmark writing
bookmark_contents = '2024-01-30-0.json.gz'
 
s3_client.put_object(
    Bucket='delab-github-mana00',
    Key='sandbox/bookmark',
    Body=bookmark_contents.encode('utf-8')
    )

'''
# 2. Test code for bookmark reading
try:
    bookmark_file = s3_client.get_object(
        Bucket='delab-github-mana00',
        Key='sandbox/bookmark'
    )
    prev_file = bookmark_file['Body'].read().decode('utf-8')
    print(prev_file)

except ClientError as e:
    if e.response['Error']['Code'] == 'NoSuchKey':
        # Catch exception
        # prev_file = baseline_file
        print('No such a key')
        # pass
    else:
        raise      