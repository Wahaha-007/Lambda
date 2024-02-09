import os
import boto3
import requests
 
# os.environ.setdefault('AWS_DEFAULT', 'da')
 
s3_client = boto3.client('s3')

''' 
# Test List Object

s3_objects = s3_client.list_objects(
  Bucket='delab-github-mana00'
)

print(s3_objects['Contents'][1])

''' 

# Upload Object

file = '2021-01-29-0.json.gz'
res = requests.get(f'https://data.gharchive.org/{file}')

if res.status_code == 200: 
  upload_res = s3_client.put_object(  # Write to S3
      Bucket='delab-github-mana00',
      Key='2021-01-29-0.json.gz',
      Body=res.content # ByteStream
   )
  
  with open(file, 'wb') as f:         # Write to local file
        f.write(res.content)

  print(f"File '{file}' downloaded and saved to S3 and the local disk.")
  print(upload_res)
else :
  print(f"Failed to download the file. Status code: {res.status_code}")